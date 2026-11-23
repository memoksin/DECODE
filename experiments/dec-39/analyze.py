"""DEC-39 pilot: gaze accuracy of MediaPipe vs L2CS-Net on known screen points.

Each model's output is mapped to screen pixels with a regression fitted on the
9 calibration points only, then the error is measured on the 8 evaluation points.

  analyze.py rec/pilot-X.webm [--diag-in 15.6]   run both models, then evaluate
  analyze.py rec/pilot-X.webm --reuse            evaluate cached features only
  analyze.py --test                              self-check of the maths (numpy only)

The JSON written by pilot.html must sit next to the webm with the same stem.
Models and weights come from experiments/dec-45 (see its README); run with its env:
  uv run --project ../dec-45 --python 3.12 python analyze.py rec/pilot-X.webm --diag-in 15.6
"""
import argparse, csv, json, math, sys, time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
DEC45 = HERE.parent / "dec-45"
RIDGE = 1e-3          # on standardised features
MODELS = ("mediapipe", "l2cs")
# Features per model, used by fit(). First two get a cross term.
FEATS = {"mediapipe": ["mp_eye_u", "mp_eye_v", "mp_head_yaw", "mp_head_pitch"],
         "l2cs": ["l2cs_yaw", "l2cs_pitch"]}


# ---------- maths (numpy only) ----------

def design(F):
    """Quadratic terms per feature + one cross term of the first two. F: (n, k), already standardised."""
    cols = [np.ones(len(F))] + [F[:, j] for j in range(F.shape[1])] + [F[:, j] ** 2 for j in range(F.shape[1])]
    cols.append(F[:, 0] * F[:, 1])
    return np.column_stack(cols)


def fit(F, XY, lam=RIDGE):
    mu, sd = F.mean(0), F.std(0)
    sd[sd == 0] = 1
    A = design((F - mu) / sd)
    W = np.linalg.solve(A.T @ A + lam * len(A) * np.eye(A.shape[1]), A.T @ XY)
    return lambda G: design((G - mu) / sd) @ W


def px_to_deg(pred, target, px_per_cm, dist_cm, center):
    """Angle between eye->target and eye->pred; eye on the normal through the screen centre."""
    def ray(p):
        d = (p - center) / px_per_cm
        return np.column_stack([d, np.full(len(d), dist_cm)])
    a, b = ray(pred), ray(target)
    c = (a * b).sum(1) / np.linalg.norm(a, axis=1) / np.linalg.norm(b, axis=1)
    return np.degrees(np.arccos(np.clip(c, -1, 1)))


def stats(e):
    e = np.asarray(e, float)
    if not len(e):
        return "- | - | -"
    return f"{e.mean():.1f} | {np.median(e):.1f} | {np.percentile(e, 95):.1f}"


def evaluate(rows, meta, diag_in=None):
    """rows: per-frame dicts with point info + features. Returns markdown lines and per-frame preds."""
    dpr = meta["screen"]["device_pixel_ratio"]
    sw, sh = meta["screen"]["inner_w"] * dpr, meta["screen"]["inner_h"] * dpr
    center = np.array([sw / 2, sh / 2])
    dist = meta.get("distance_cm")
    ppcm = None
    if diag_in:
        # physical width from diagonal and the screen's own pixel aspect
        W, H = meta["screen"]["width"] * dpr, meta["screen"]["height"] * dpr
        ppcm = math.hypot(W, H) / (diag_in * 2.54)
    deg_ok = bool(ppcm and dist)

    out = [f"Screen {sw:.0f}×{sh:.0f} px (physical), distance {dist or 'not recorded'} cm, "
           f"{f'{ppcm:.1f} px/cm' if ppcm else 'no --diag-in: no degrees'}", ""]
    hdr = ("| model | set | frames used / total | px mean | px median | px p95 | ° mean | ° median | ° p95 "
           "| per-point median px | per-point median ° |")
    out += [hdr, "|" + "---|" * 11]
    blank = " - |" * 8
    preds = {}
    for m in MODELS:
        cols = FEATS[m]
        ok = [r for r in rows if all(r.get(c) not in ("", None) for c in cols)]
        cal = [r for r in ok if r["set"] == "calib"]
        if len({(r["round"], r["idx"]) for r in cal}) < 6:
            out.append(f"| {m} | too few calibration points with a face | {len(ok)} / {len(rows)} |{blank}")
            continue
        F = lambda rs: np.array([[float(r[c]) for c in cols] for r in rs])
        T = lambda rs: np.array([[float(r["x_px"]), float(r["y_px"])] for r in rs])
        f = fit(F(cal), T(cal))
        for r, p in zip(ok, f(F(ok))):
            preds[(m, r["t_ms"])] = p
        for name, sel in [("calib (fit)", lambda r: r["set"] == "calib"),
                          ("eval", lambda r: r["set"] == "eval"),
                          ("eval round 1", lambda r: r["set"] == "eval" and int(r["round"]) == 1),
                          ("eval round 2", lambda r: r["set"] == "eval" and int(r["round"]) == 2)]:
            rs = [r for r in ok if sel(r)]
            n_all = sum(1 for r in rows if sel(r))
            if not rs:
                out.append(f"| {m} | {name} | 0 / {n_all} |{blank}")
                continue
            P, Tg = f(F(rs)), T(rs)
            e_px = np.linalg.norm(P - Tg, axis=1)
            e_deg = px_to_deg(P, Tg, ppcm, dist, center) if deg_ok else []
            # fixation-level: median prediction per shown point
            groups = {}
            for r, p in zip(rs, P):
                groups.setdefault((r["round"], r["set"], r["idx"]), []).append((p, (float(r["x_px"]), float(r["y_px"]))))
            gp = np.array([np.median([p for p, _ in g], 0) for g in groups.values()])
            gt = np.array([g[0][1] for g in groups.values()])
            g_px = np.linalg.norm(gp - gt, axis=1)
            g_deg = px_to_deg(gp, gt, ppcm, dist, center) if deg_ok else []
            out.append(f"| {m} | {name} | {len(rs)} / {n_all} | {stats(e_px)} | {stats(e_deg)} | "
                       f"{np.median(g_px):.1f} | {f'{np.median(g_deg):.1f}' if deg_ok else '-'} |")
    return out, preds


# ---------- video + models ----------

def load_meta(video):
    j = video.with_suffix(".json")
    if not j.exists():
        sys.exit(f"missing {j.name} next to the video")
    return json.loads(j.read_text(encoding="utf-8"))


def point_at(events, t):
    for e in events:
        if e["use_from_ms"] <= t < e["offset_ms"]:
            return e
    return None


def make_models():
    sys.path.insert(0, str(DEC45))
    import run as dec45  # loads weights from experiments/dec-45/models
    from mediapipe.tasks import python as mpp
    from mediapipe.tasks.python import vision
    opts = vision.FaceLandmarkerOptions(
        base_options=mpp.BaseOptions(model_asset_path=str(dec45.FACE_TASK)),
        running_mode=vision.RunningMode.IMAGE, num_faces=1,
        output_facial_transformation_matrixes=True)
    return vision.FaceLandmarker.create_from_options(opts), dec45.load_l2cs(), dec45


def mp_features(lm, frame, cv2, mp):
    h, w = frame.shape[:2]
    r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
    if not r.face_landmarks:
        return None
    P = np.array([[p.x * w, p.y * h] for p in r.face_landmarks[0]])

    def eye(outer, inner, top, bottom, iris):
        a, b = P[outer], P[inner]
        ax = b - a
        L = np.linalg.norm(ax)
        ax = ax / L
        nrm = np.array([-ax[1], ax[0]])
        rel = P[iris] - a
        mid = (P[top] + P[bottom]) / 2 - a
        return rel @ ax / L, (rel - mid) @ nrm / L   # u: along the eye 0..1, v: up/down vs lid centre

    # left eye: 33 outer, 133 inner, 159 top, 145 bottom, 468 iris; right: 263, 362, 386, 374, 473
    uL, vL = eye(33, 133, 159, 145, 468)
    uR, vR = eye(263, 362, 386, 374, 473)
    M = np.array(r.facial_transformation_matrixes[0])[:3, :3]
    yaw = math.degrees(math.atan2(M[0, 2], M[2, 2]))
    pitch = math.degrees(math.asin(-np.clip(M[1, 2], -1, 1)))
    # mirror the right eye's u so both grow in the same screen direction
    return dict(mp_eye_u=(uL + (1 - uR)) / 2, mp_eye_v=(vL + vR) / 2, mp_head_yaw=yaw, mp_head_pitch=pitch)


def extract(video, meta):
    import cv2
    import mediapipe as mp
    lm, pipe, dec45 = make_models()
    cap = cv2.VideoCapture(str(video))
    rows, t_mp, t_l2, n_frames, t_first, t_last = [], 0.0, 0.0, 0, None, None
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        t = cap.get(cv2.CAP_PROP_POS_MSEC)
        t_first = t if t_first is None else t_first
        t_last, n_frames = t, n_frames + 1
        e = point_at(meta["events"], t - t_first)
        if e is None:
            continue
        s = time.perf_counter(); m = mp_features(lm, frame, cv2, mp); t_mp += time.perf_counter() - s
        s = time.perf_counter()
        try:
            g = dec45.l2cs_measure(pipe, frame)
        except ValueError:  # l2cs Pipeline.step crashes (np.stack of []) when RetinaFace finds no face
            g = None
        t_l2 += time.perf_counter() - s
        dpr = meta["screen"]["device_pixel_ratio"]
        row = dict(t_ms=round(t - t_first, 1), round=e["round"], set=e["set"], idx=e["idx"],
                   x_px=round(e["x_css"] * dpr, 1), y_px=round(e["y_css"] * dpr, 1),
                   frame_w=frame.shape[1], frame_h=frame.shape[0])
        row.update(m or {k: "" for k in FEATS["mediapipe"]})
        row.update(dict(l2cs_pitch=g[0], l2cs_yaw=g[1]) if g else dict(l2cs_pitch="", l2cs_yaw=""))
        rows.append(row)
    cap.release()
    k = max(len(rows), 1)
    info = dict(frames_in_file=n_frames, frames_analysed=len(rows),
                real_fps=round((n_frames - 1) / ((t_last - t_first) / 1000), 2) if n_frames > 1 and t_last > t_first else None,
                ms_per_frame_mediapipe=round(1000 * t_mp / k, 1), ms_per_frame_l2cs=round(1000 * t_l2 / k, 1),
                mp_face_rate=round(sum(r["mp_eye_u"] != "" for r in rows) / k, 3),
                l2cs_face_rate=round(sum(r["l2cs_yaw"] != "" for r in rows) / k, 3))
    return rows, info


def write_csv(path, rows):
    keys = ["t_ms", "round", "set", "idx", "x_px", "y_px", "frame_w", "frame_h"] + FEATS["mediapipe"] + ["l2cs_pitch", "l2cs_yaw"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def read_csv(path):
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["t_ms"] = float(r["t_ms"])
    return rows


# ---------- self-check ----------

def selftest():
    rng = np.random.default_rng(39)
    # px_to_deg: 1 cm off-centre at 60 cm, 40 px/cm -> atan(1/60) = 0.955 deg
    d = px_to_deg(np.array([[1040.0, 500.0]]), np.array([[1000.0, 500.0]]), 40, 60, np.array([1000.0, 500.0]))
    assert abs(d[0] - math.degrees(math.atan(1 / 60))) < 1e-6, d
    # same schedule as pilot.html
    calib = [(x, y) for y in (0.1, 0.5, 0.9) for x in (0.1, 0.5, 0.9)]
    evalp = [(0.3, 0.3), (0.7, 0.3), (0.3, 0.7), (0.7, 0.7), (0.5, 0.25), (0.5, 0.75), (0.25, 0.5), (0.75, 0.5)]
    W, H = 1920, 1080
    meta = dict(distance_cm=60, screen=dict(device_pixel_ratio=1.25, inner_w=1536, inner_h=864, width=1536, height=864))
    rows, t = [], 0.0
    for rnd in (1, 2):
        for s, pts in (("calib", calib), ("eval", evalp)):
            for i, (fx, fy) in enumerate(pts):
                for _ in range(45):
                    x, y = fx * W, fy * H
                    yaw = 25 * (fx - 0.5) + 2 * (fx - 0.5) ** 2 + rng.normal(0, 0.3)   # smooth, slightly non-linear
                    pitch = -15 * (fy - 0.5) + rng.normal(0, 0.3)
                    u = 0.5 + 0.2 * (fx - 0.5) + rng.normal(0, 0.003)
                    v = 0.1 * (fy - 0.5) + rng.normal(0, 0.003)
                    rows.append(dict(t_ms=t, round=rnd, set=s, idx=i, x_px=x, y_px=y,
                                     mp_eye_u=u, mp_eye_v=v, mp_head_yaw=rng.normal(0, 1), mp_head_pitch=rng.normal(0, 1),
                                     l2cs_yaw=yaw, l2cs_pitch=pitch))
                    t += 33.3
    lines, preds = evaluate(rows, meta, diag_in=15.6)
    print("\n".join(lines))
    ev = [r for r in rows if r["set"] == "eval"]
    for m in MODELS:
        e = [np.hypot(*(preds[(m, r["t_ms"])] - [r["x_px"], r["y_px"]])) for r in ev]
        med = float(np.median(e))
        # noise 0.3 deg ~ 15-20 px on this screen; a broken fit gives hundreds
        assert med < 80, (m, med)
        print(f"ok {m}: eval median {med:.1f} px")
    assert all(l.count("|") == 12 for l in lines if l.startswith("| ")), "table columns"
    # held-out check: moving eval targets must not change the calibration fit
    calib_rows = [l for l in lines if "calib (fit)" in l]
    moved = [dict(r, x_px=r["x_px"] + 500) if r["set"] == "eval" else r for r in rows]
    lines2, _ = evaluate(moved, meta, diag_in=15.6)
    assert calib_rows == [l for l in lines2 if "calib (fit)" in l], "eval points leaked into the fit"
    print("ok: eval points are held out")
    # no face in any frame for one model must not crash
    for r in rows:
        r["mp_eye_u"] = ""
    lines, _ = evaluate(rows, meta, diag_in=15.6)
    assert any("too few calibration" in l for l in lines)
    print("ok: missing face handled\nall self-checks passed")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video", nargs="?", type=Path)
    ap.add_argument("--diag-in", type=float, help="screen diagonal in inches, for degrees (HP ProBook 450 G10: 15.6)")
    ap.add_argument("--reuse", action="store_true", help="use the cached features CSV, do not run the models")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")  # Windows console: ×, °
    if a.test:
        return selftest()
    if not a.video:
        ap.error("video path required")
    video = a.video.resolve()
    meta = load_meta(video)
    feats = video.with_name(video.stem + "-features.csv")
    info_path = video.with_name(video.stem + "-info.json")
    if a.reuse:
        rows, info = read_csv(feats), json.loads(info_path.read_text(encoding="utf-8"))
    else:
        rows, info = extract(video, meta)
        write_csv(feats, rows)
        info_path.write_text(json.dumps(info, indent=2), encoding="utf-8")
    lines, _ = evaluate(rows, meta, a.diag_in)
    cam = meta["camera"]["settings"]
    head = [f"# DEC-39 pilot: {video.name}", "",
            f"Recorded {meta.get('wall_start')} by {meta.get('who') or 'not recorded'}; camera {meta['camera']['label']}, "
            f"requested 1920×1080, got {cam.get('width')}×{cam.get('height')}; real fps {info['real_fps']}; "
            f"glasses {meta.get('glasses') or '-'}, light {meta.get('light') or '-'}"
            + (f"; ABORTED: {meta['aborted']}" if meta.get("aborted") else ""), "",
            f"Face found: MediaPipe {info['mp_face_rate']:.0%}, L2CS {info['l2cs_face_rate']:.0%} "
            f"of {info['frames_analysed']} analysed frames ({info['frames_in_file']} in file)", "",
            f"Time per frame (CPU, this machine): MediaPipe {info['ms_per_frame_mediapipe']} ms, L2CS {info['ms_per_frame_l2cs']} ms", ""]
    text = "\n".join(head + lines) + "\n"
    print(text)
    out = HERE / f"results-{video.stem}.md"
    out.write_text(text, encoding="utf-8")
    print(f"written {out.relative_to(HERE)} and {feats.name}")


if __name__ == "__main__":
    main()
