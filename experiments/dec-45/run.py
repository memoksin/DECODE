"""DEC-45: effect of webcam resolution (1080p/720p/480p) on gaze estimation."""
import csv, subprocess, sys, time
from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np
import torch
from safetensors.torch import load_file

HERE = Path(__file__).resolve().parent
MODELS = HERE / "models"
L2CS_W = MODELS / "l2cs_gaze360_resnet50.safetensors"
FACE_TASK = MODELS / "face_landmarker.task"
MAX_SECONDS = 600  # if estimated CPU time exceeds this, use every 2nd frame


def make_versions(src: Path):
    vids = {"1080p": src}
    for h in (720, 480):
        out = src.parent / f"{src.stem.replace('1080p', '')}{h}p.mp4"
        if out == src:
            out = src.parent / f"{src.stem}-{h}p.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", f"scale=-2:{h}",
                        "-an", "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(out)], check=True)
        vids[f"{h}p"] = out
    return vids


def load_l2cs():
    from l2cs import Pipeline
    from l2cs.utils import getArch
    from face_detection import RetinaFace
    dev = torch.device("cpu")
    sd = load_file(str(L2CS_W))
    model = getArch("ResNet50", 90)
    res = model.load_state_dict(sd, strict=False)
    print("L2CS load_state_dict missing:", res.missing_keys, "unexpected:", res.unexpected_keys)
    if res.missing_keys or res.unexpected_keys:
        sys.exit("FAIL: weight keys mismatch")
    model.eval()
    # Pipeline.__init__ only supports torch.load of pickles; build it without that.
    p = Pipeline.__new__(Pipeline)
    p.weights, p.include_detector, p.device, p.confidence_threshold = L2CS_W, True, dev, 0.5
    p.model = model.to(dev)
    p.detector = RetinaFace()
    p.softmax = torch.nn.Softmax(dim=1)
    p.idx_tensor = torch.arange(90, dtype=torch.float32)
    return p


def make_landmarker():
    from mediapipe.tasks import python as mpp
    from mediapipe.tasks.python import vision
    opts = vision.FaceLandmarkerOptions(
        base_options=mpp.BaseOptions(model_asset_path=str(FACE_TASK)),
        running_mode=vision.RunningMode.IMAGE, num_faces=1)
    return vision.FaceLandmarker.create_from_options(opts)


def mp_measure(lm, frame):
    h, w = frame.shape[:2]
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
    if not r.face_landmarks:
        return None
    pts = np.array([[p.x * w, p.y * h] for p in r.face_landmarks[0]])
    d = np.linalg.norm
    iod = d(pts[468] - pts[473])
    iris = np.mean([(d(pts[469] - pts[471]) + d(pts[470] - pts[472])) / 2,
                    (d(pts[474] - pts[476]) + d(pts[475] - pts[477])) / 2])
    return iod, iris


def l2cs_measure(pipe, frame):
    r = pipe.step(frame)
    if len(r.pitch) == 0:
        return None
    b = r.bboxes
    i = int(np.argmax((b[:, 2] - b[:, 0]) * (b[:, 3] - b[:, 1])))
    return float(np.degrees(r.pitch[i])), float(np.degrees(r.yaw[i]))


def vec(p, y):
    p, y = np.radians(p), np.radians(y)
    return np.array([-np.cos(p) * np.sin(y), -np.sin(p), -np.cos(p) * np.cos(y)])


def ang_err(a, b):
    va, vb = vec(*a), vec(*b)
    return float(np.degrees(np.arccos(np.clip(va @ vb, -1, 1))))


def process(path, stride, lm, pipe):
    cap = cv2.VideoCapture(str(path))
    rows, t_proc, idx = [], 0.0, 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % stride == 0:
            t = time.perf_counter()
            m = mp_measure(lm, frame)
            g = l2cs_measure(pipe, frame)
            t_proc += time.perf_counter() - t
            rows.append(dict(frame=idx, mp_detected=int(m is not None),
                             iod_px=m[0] if m else "", iris_px=m[1] if m else "",
                             l2cs_detected=int(g is not None),
                             pitch_deg=g[0] if g else "", yaw_deg=g[1] if g else ""))
        idx += 1
    cap.release()
    return rows, len(rows) / t_proc


def main():
    src = Path(sys.argv[1]).resolve()
    vids = make_versions(src)
    lm, pipe = make_landmarker(), load_l2cs()
    n = int(cv2.VideoCapture(str(src)).get(cv2.CAP_PROP_FRAME_COUNT))
    # timing probe on first frames of 1080p
    cap = cv2.VideoCapture(str(src)); fr = [cap.read()[1] for _ in range(10)]; cap.release()
    t = time.perf_counter()
    for f in fr:
        mp_measure(lm, f); l2cs_measure(pipe, f)
    per = (time.perf_counter() - t) / len(fr)
    est = per * n * (1 + 0.44 + 0.19)
    stride = 2 if est > MAX_SECONDS else 1
    print(f"{n} frames, {per:.2f}s/frame at 1080p, estimated {est/60:.1f} min for all -> processing every {stride} frame(s)")

    res, speed = {}, {}
    for name, path in vids.items():
        print("processing", name, flush=True)
        res[name], speed[name] = process(path, stride, lm, pipe)

    ref = {r["frame"]: r for r in res["1080p"] if r["l2cs_detected"]}
    out = HERE / "results.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["resolution", "frame", "mp_detected", "iod_px", "iris_px", "l2cs_detected",
                    "pitch_deg", "yaw_deg", "ang_err_vs_1080p_deg"])
        errs = {}
        for name, rows in res.items():
            errs[name] = []
            for r in rows:
                e = ""
                if r["l2cs_detected"] and r["frame"] in ref:
                    e = ang_err((r["pitch_deg"], r["yaw_deg"]), (ref[r["frame"]]["pitch_deg"], ref[r["frame"]]["yaw_deg"]))
                    errs[name].append(e)
                w.writerow([name, r["frame"], r["mp_detected"], r["iod_px"], r["iris_px"],
                            r["l2cs_detected"], r["pitch_deg"], r["yaw_deg"], e])

    print(f"\nFrames per resolution: {len(res['1080p'])} (stride {stride}); results in {out.name}\n")
    print("| res | MP det. rate | L2CS det. rate | err mean (deg) | err median | err p95 | n err | iris px | inter-ocular px | fps |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for name, rows in res.items():
        k = len(rows)
        mpr = sum(r["mp_detected"] for r in rows) / k
        l2r = sum(r["l2cs_detected"] for r in rows) / k
        iris = np.mean([r["iris_px"] for r in rows if r["mp_detected"]])
        iod = np.mean([r["iod_px"] for r in rows if r["mp_detected"]])
        e = np.array(errs[name])
        st = f"{e.mean():.2f} | {np.median(e):.2f} | {np.percentile(e, 95):.2f}" if len(e) else "- | - | -"
        print(f"| {name} | {mpr:.1%} | {l2r:.1%} | {st} | {len(e)} | {iris:.1f} | {iod:.1f} | {speed[name]:.2f} |")


if __name__ == "__main__":
    main()
