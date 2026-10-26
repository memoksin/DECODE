"""Builds the five SRS UI mockups as HTML and renders them to ../ui-*.png.

Run: python -I build.py   (needs Microsoft Edge or Chrome)
"""
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

ICON = {
    "mic": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>',
    "cam": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/></svg>',
    "end": '<svg viewBox="0 0 24 24" fill="#fff"><path d="M3 14c5-5 13-5 18 0l-2.5 2.5-3-1.5v-2.5c-2.3-.8-4.7-.8-7 0V15l-3 1.5z"/></svg>',
}

HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"><title>{title}</title></head><body>"""


def topbar(view, time):
    return (f'<div class="topbar"><div class="room"><span class="brand">MiroTalk SFU</span>Room 7F3K</div>'
            f'<div class="meta">{view}  ·  {time}</div></div>')


def controls():
    return ('<div class="controls">' + "".join(
        f'<div class="btn-round{" end" if k == "end" else ""}">{ICON[k]}</div>' for k in ["mic", "cam", "chat", "end"]
    ) + "</div>")


def avatar():
    return '<div class="avatar"><div class="head"></div><div class="body"></div></div>'


def video_stage(name):
    return (f'<div class="stage"><div class="tile">{avatar()}<span class="tag">{name}</span></div>'
            f'<div class="self">{avatar()}<span class="tag">You</span></div></div>')


def page(title, view, time, body):
    return HEAD.format(title=title) + topbar(view, time) + body + controls() + "</body></html>"


UI1 = page("UI-1 Session Setup", "Interviewer view", "14:02", '<div class="main">' + video_stage("Candidate 1") + """
<div class="panel">
  <div class="ph"><span class="badge">DECODE</span><h1>New Session</h1></div>
  <div><div class="label">Session name</div><div class="input">Junior developer 1. tur</div></div>
  <div><div class="label">Programming language</div><div class="input">Java <span>▾</span></div></div>
  <div><div class="label">Join link for candidates</div>
    <div class="link"><div class="input">sfu.decode.app/join/7F3K</div><div class="small-btn">Copy</div></div></div>
  <div class="hint">No names or personal data in the session name.</div>
  <div class="sep"></div>
  <div class="row">Candidates joined <b>2</b></div>
  <div class="row">Candidate 1 <span class="ok dot">Camera on · 1080p</span></div>
  <div class="row">Candidate 2 <span class="ok dot">Camera on · 720p</span></div>
  <div class="spacer"></div>
  <div class="actions"><div class="btn secondary">Cancel</div><div class="btn primary">Start Analysis</div></div>
</div></div>""")

UI2 = page("UI-2 Consent", "Candidate view", "14:03", '<div class="main">' + video_stage("Interviewer") + """
<div class="panel">
  <div class="ph"><span class="badge">DECODE</span><h1>Eye Tracking Consent</h1></div>
  <p class="p">The interviewer wants to analyse where you look while you read the code on this page.</p>
  <ul class="bullets">
    <li>Your webcam is used only to estimate gaze.</li>
    <li>Your video is recorded in your browser and uploaded after the session.</li>
    <li>The video is deleted after analysis.</li>
    <li>The result is extra insight, not a hiring decision.</li>
  </ul>
  <div class="check"><span class="box">✓</span>I have read and agree</div>
  <div class="spacer"></div>
  <div class="actions"><div class="btn secondary">Decline</div><div class="btn primary">Accept</div></div>
</div></div>""")

pts = [(80, 130), (640, 130), (1200, 130), (80, 360), (1200, 360), (80, 590), (640, 590), (1200, 590)]
UI3 = page("UI-3 Calibration", "Candidate view", "14:04", '<div class="main"><div class="calib">' + """
  <div class="title"><div class="t"><span class="badge">DECODE</span>Calibration</div><p>Look at the blue dot until it moves.</p></div>
""" + "".join(f'<div class="pt" style="left:{x}px;top:{y}px"></div>' for x, y in pts) + """
  <div class="pt active" style="left:640px;top:360px"></div>
  <div class="foot">Point 5 of 9 <div class="small-btn">Restart</div></div>
</div></div>""")

code = [
    "int search(int[] a, int x) {",
    "    int lo = 0, hi = a.length - 1;",
    "    while (lo &lt;= hi) {",
    "        int mid = (lo + hi) / 2;",
    "        if (a[mid] == x) return mid;",
    "        if (a[mid] &lt; x) lo = mid + 1;",
    "        else hi = mid - 1;",
    "    }",
    "    return -1;",
    "}",
]
code_html = "\n".join(f'<span class="ln">{i}</span>{line}' for i, line in enumerate(code, 1))
UI4 = page("UI-4 Live Session", "Interviewer view", "14:09", """<div class="main"><div class="stage"><div class="codeview">
  <div class="codebar">DECODE code view <span>·  Search.java  ·  shown to Candidate 1</span></div>
  <pre>""" + code_html + """</pre>
  <div class="aoi" style="top:56px;height:44px"><em>Block 1</em></div>
  <div class="aoi" style="top:104px;height:140px"><em>Block 2</em></div>
  <div class="aoi" style="top:248px;height:44px"><em>Block 3</em></div>
  <div class="cam-mini" style="top:56px">""" + avatar() + """<span class="tag">Candidate 1</span></div>
  <div class="cam-mini" style="bottom:16px">""" + avatar() + """<span class="tag">You</span></div>
</div></div>
<div class="panel">
  <div class="ph"><span class="badge">DECODE</span><h1>Live Session</h1><span class="rec">● REC</span></div>
  <div class="row">Session <b>Junior developer 1. tur</b></div>
  <div class="row">Candidate <b>Candidate 1</b></div>
  <div class="row">Language <b>Java</b></div>
  <div class="row">Elapsed <b>04:12</b></div>
  <div class="row">Calibration error <b>1.8°</b></div>
  <div class="sep"></div>
  <div class="row">Face detected <span class="ok dot">Yes</span></div>
  <div class="row">Gaze quality <span class="warn dot">Low</span></div>
  <div class="alert"><b>Gaze quality is low</b>The candidate may have moved. Recalibrate to keep results reliable.</div>
  <div class="spacer"></div>
  <div class="hint">Recording stays in the candidate's browser until the session ends.</div>
  <div class="actions"><div class="btn secondary">Recalibrate</div><div class="btn primary">End Analysis</div></div>
</div></div>""")

UI5 = page("UI-5 Session Report", "Interviewer view", "14:52", '<div class="main">' + video_stage("Candidate 1") + """
<div class="panel">
  <div class="ph"><span class="badge">DECODE</span><h1>Session Report</h1></div>
  <div class="selector"><div><div class="name">Junior developer 1. tur</div><div class="sub">26.10.2026 · 14:05</div></div><span>▾</span></div>
  <div class="stats">
    <div class="stat"><div class="k">Duration</div><div class="v">42 min</div></div>
    <div class="stat"><div class="k">Candidates</div><div class="v">3</div></div>
    <div class="stat"><div class="k">Language</div><div class="v">Java</div></div>
  </div>
  <table>
    <tr><th>Candidate</th><th>Result (confidence)</th></tr>
    <tr class="sel"><td>Candidate 1</td><td><span class="pill exp">Experienced</span><span class="conf">82%</span></td></tr>
    <tr><td>Candidate 2</td><td><span class="pill nov">Novice</span><span class="conf">64%</span></td></tr>
    <tr><td>Candidate 3</td><td><span class="pill exp">Experienced</span><span class="conf">71%</span></td></tr>
  </table>
  <div class="detail-h">Candidate 1 <span class="pill exp">Experienced · 82%</span></div>
  <div class="bar-row"><div class="row">Similarity to experienced path <b>0.72</b></div><div class="bar"><i style="width:72%;background:#16a34a"></i></div></div>
  <div class="bar-row"><div class="row">Similarity to novice path <b>0.41</b></div><div class="bar"><i style="width:41%;background:#9ca3af"></i></div></div>
  <div class="row">Calibration error <b>1.8°</b></div>
  <div class="row">Reliability <span class="ok dot">Good</span></div>
  <div class="spacer"></div>
  <div class="note">Extra insight only. Not a hiring decision.</div>
</div></div>""")

SCREENS = {
    "ui-1-session-setup": UI1,
    "ui-2-consent": UI2,
    "ui-3-calibration": UI3,
    "ui-4-live-session": UI4,
    "ui-5-report": UI5,
}


def main():
    browser = next((b for b in BROWSERS if os.path.exists(b)), None)
    if not browser:
        sys.exit("Edge or Chrome not found")
    for name, html in SCREENS.items():
        src = HERE / f"{name}.html"
        src.write_text(html, encoding="utf-8")
        png = OUT / f"{name}.png"
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=1280,800",
                        "--virtual-time-budget=5000", f"--screenshot={png}", src.as_uri()],
                       check=True, capture_output=True)
        print(name, "->", png.name)


if __name__ == "__main__":
    main()
