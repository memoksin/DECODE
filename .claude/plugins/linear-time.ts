// OpenCode plugin (loaded via .opencode -> .claude): runs the same Linear time rules as the Claude Code hook.
// Supports OpenCode V2 (setup) and V1 (server).
import { spawnSync } from "node:child_process"
import { readFileSync } from "node:fs"
import { join } from "node:path"

// Same text Claude Code injects on every prompt (UserPromptSubmit hook).
const reminder = (dir: string) => {
  try {
    return readFileSync(join(dir, ".claude/hooks/time-reminder.md"), "utf8")
  } catch (e) {
    console.error("time-reminder.md missing:", e)
    return ""
  }
}

const asked = new Set<string>()

const isSaveIssue = (tool: string) => /linear/i.test(tool) && /save_issue$/.test(tool)

function rules(dir: string, args: unknown): { deny?: string; note?: string } {
  const script = join(dir, ".claude/hooks/linear-time-rules.py")
  const input = JSON.stringify({ tool_input: args })
  // python3 is missing or a Store stub on most Windows machines.
  let r = spawnSync("python3", [script], { input, encoding: "utf8" })
  if (r.status !== 0 || r.error) r = spawnSync("python", [script], { input, encoding: "utf8" })
  // Same as Claude Code: a broken hook warns but does not block the tool.
  if (r.status !== 0 || r.error) {
    console.error("linear-time-rules.py failed:", r.error ?? r.stderr)
    return {}
  }
  if (!r.stdout.trim()) return {}
  const out = JSON.parse(r.stdout).hookSpecificOutput ?? {}
  if (out.permissionDecision === "deny") return { deny: out.permissionDecisionReason, note: out.additionalContext }
  if (out.permissionDecision !== "ask") return { note: out.additionalContext }
  // OpenCode has no prompt here: block the first try so the agent asks the user, allow the retry.
  const key = JSON.stringify(args)
  if (asked.has(key)) return { note: out.additionalContext }
  asked.add(key)
  return { deny: `${out.permissionDecisionReason} Tell the user this estimate, wait for their OK, then retry.` }
}

export default {
  id: "decode.linear-time",
  async setup(ctx: any) {
    const dir = ctx.location.directory
    await ctx.session.hook("context", (event: any) => {
      const text = reminder(dir)
      if (text) event.system.push({ type: "text", text })
    })
    await ctx.tool.hook("execute.before", (event: any) => {
      if (!isSaveIssue(event.tool)) return
      const { deny } = rules(dir, event.input)
      if (deny) throw new Error(deny)
    })
    await ctx.tool.hook("execute.after", (event: any) => {
      if (!isSaveIssue(event.tool) || event.status !== "completed") return
      const { note } = rules(dir, event.input)
      if (!note) return
      const r = event.result ?? {}
      event.result = {
        ...r,
        content: typeof r.content === "string" || r.content == null
          ? `${r.content ?? ""}\n\n${note}`
          : [...r.content, { type: "text", text: note }],
      }
    })
  },
  async server(input: any) {
    const dir = input.directory
    return {
      "experimental.chat.system.transform": async (_: any, out: any) => {
        const text = reminder(dir)
        if (text) out.system.push(text)
      },
      "tool.execute.before": async (i: any, out: any) => {
        if (!isSaveIssue(i.tool)) return
        const { deny } = rules(dir, out.args)
        if (deny) throw new Error(deny)
      },
      "tool.execute.after": async (i: any, out: any) => {
        if (!isSaveIssue(i.tool)) return
        const { note } = rules(dir, i.args ?? {})
        if (note && typeof out.output === "string") out.output += `\n\n${note}`
      },
    }
  },
}
