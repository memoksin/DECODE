# DEC-39: gaze pilot (known screen points)

Plan and results: [docs/dec-39-gaze-pilot.md](../../docs/dec-39-gaze-pilot.md).

## Record

`pilot.html` shows 9 calibration + 8 evaluation points (2 s each, 2 rounds, ~80 s) and records the webcam
in the browser with `MediaRecorder` (same path as DEC-44). It downloads `pilot-<time>.webm` and `pilot-<time>.json`
(point positions and times, camera settings, screen, browser, measured fps).

Camera access needs a secure page, so serve it from localhost:

```
cd experiments/dec-39
python -m http.server 8039
```

Open http://localhost:8039/pilot.html in Chrome or Edge, fill the form, open the camera, start.
Move both files into `experiments/dec-39/rec/` (git-ignored: recordings stay local).

Times in the JSON are ms since the `MediaRecorder` start event, about video t=0.
Use frames from `use_from_ms` to `offset_ms` of each point (first 0.5 s dropped).
File names use UTC time. `preview_fps` is only what the page displayed; take the real fps from the webm with `ffprobe`.

Tested 19 Nov 2026 with a fake 720p canvas camera (no real camera): 34 points, ~71 s, VP9 webm + JSON saved.
On this laptop Windows scaling is 125% (`device_pixel_ratio` 1.25): CSS 1536×864 = 1920×1080 physical px.

## Analyse

`analyze.py` runs MediaPipe and L2CS-Net on the same frames (only frames inside a point's
`use_from_ms`–`offset_ms` window), maps each model's output to screen px with a ridge-regularised
quadratic fitted on the 9 `calib` points, and measures the error on the 8 `eval` points.

- MediaPipe features: iris position inside each eye (along the eye corners and vs. lid centre, both eyes averaged) + head yaw/pitch from the face transformation matrix.
- L2CS features: pitch/yaw from L2CS-Net Gaze360 ResNet50.
- Errors in physical px and degrees (needs `--diag-in` and the distance typed into the page), per frame and per shown point (median of its frames).

Uses the DEC-45 environment and weights (set them up first as in `experiments/dec-45/README.md`):

```
cd experiments/dec-39
uv run --project ../dec-45 --python 3.12 python analyze.py rec/pilot-X.webm --diag-in 15.6
```

Writes `rec/pilot-X-features.csv` + `rec/pilot-X-info.json` (cache; `--reuse` re-evaluates without the models)
and `results-pilot-X.md` here (summary table, safe to commit).

Self-check (numpy only, no models): `python analyze.py --test`.
It checks the regression, the px→degree maths, that eval points are held out, and a model with no face.

End-to-end run, 19 Nov 2026 (İrem's HP ProBook 450 G10, i7-1355U, CPU only), on a synthetic 72 s 1280×720 VP9 webm
(ffmpeg `testsrc2`, no face) with a JSON in the page's format:
- Video read and timing work: 1530 of 2160 frames analysed = 34 points × 1.5 s × 30 fps; real fps 30.0.
- No face: both models report 0 % and the table says so, no crash. L2CS's `Pipeline.step` raises `ValueError` when RetinaFace finds no face; `analyze.py` counts that frame as "no face".
- Time per frame: MediaPipe 14 ms, L2CS 316 ms (RetinaFace on the full frame). One pilot ≈ 10 min.
- Not checked yet: MediaPipe eye/head features with a real face, and Chrome's own webm timestamps. Look at the first real recording.

## Setup on Windows (19 Nov 2026)

- `winget install astral-sh.uv` and `winget install Gyan.FFmpeg` (user scope). Open a new terminal so PATH updates.
- Inside the Claude desktop app, `AppData` writes are redirected, which breaks `uv`'s Python install.
  Fix: put uv's Python and cache in the home folder before `uv sync`:
  `$env:UV_PYTHON_INSTALL_DIR="$HOME\.uv\python"; $env:UV_CACHE_DIR="$HOME\.uv\cache"`. A normal terminal does not need this.
- Then `cd experiments/dec-45; uv sync --python 3.12` (~1–2 GB download) and the two weights into `experiments/dec-45/models/`:
  - https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task
  - https://huggingface.co/py-feat/l2cs/resolve/main/l2cs_gaze360_resnet50.safetensors
- Versions: torch 2.5.1+cpu, mediapipe 0.10.21, opencv 4.11.0, Python 3.12.16, ffmpeg 9.0.2.
