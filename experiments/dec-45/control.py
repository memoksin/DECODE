import csv, subprocess, sys, statistics as st
sys.path.insert(0, sys.argv[1])
import run
from pathlib import Path
d = Path(sys.argv[1]); src = d/"rec/me-1080p.mp4"; out = d/"rec/me-1080p-reenc.mp4"
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",str(src),"-an","-c:v","libx264","-crf","18","-pix_fmt","yuv420p",str(out)],check=True)
lm, pipe = run.make_landmarker(), run.load_l2cs()
rows, _ = run.process(out, 2, lm, pipe)
ref = {int(r["frame"]): (float(r["pitch_deg"]), float(r["yaw_deg"])) for r in csv.DictReader(open(d/"results.csv")) if r["resolution"]=="1080p" and r["pitch_deg"]}
e = sorted(run.ang_err((r["pitch_deg"], r["yaw_deg"]), ref[r["frame"]]) for r in rows if r["l2cs_detected"] and r["frame"] in ref)
print(f"CONTROL 1080p re-encoded (crf18, no scaling) vs 1080p: n={len(e)} mean {st.mean(e):.2f} median {st.median(e):.2f} p95 {e[int(.95*len(e))]:.2f} deg")
