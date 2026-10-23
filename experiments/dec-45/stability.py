"""Gaze jitter while staring at one fixed point. Needs no reference video, so it
compares native recordings from different cameras/resolutions."""
import statistics as st
import sys

import numpy as np

import run


def main():
    lm, pipe = run.make_landmarker(), run.load_l2cs()
    print("| video | frames | face det. | jitter mean (deg) | median | p95 | iris px |")
    print("|---|---|---|---|---|---|---|")
    for path in sys.argv[1:]:
        rows, _ = run.process(path, 1, lm, pipe)
        g = [(r["pitch_deg"], r["yaw_deg"]) for r in rows if r["l2cs_detected"]]
        if not g:
            print(f"| {path} | {len(rows)} | 0% | - | - | - | - |")
            continue
        # Deviation from the median gaze direction = jitter during a steady fixation
        med = (st.median(p for p, _ in g), st.median(y for _, y in g))
        e = np.array([run.ang_err(x, med) for x in g])
        iris = [r["iris_px"] for r in rows if r["mp_detected"]]
        print(f"| {path} | {len(rows)} | {len(g) / len(rows):.0%} | {e.mean():.2f} | {np.median(e):.2f} "
              f"| {np.percentile(e, 95):.2f} | {np.mean(iris):.1f} |")


if __name__ == "__main__":
    main()
