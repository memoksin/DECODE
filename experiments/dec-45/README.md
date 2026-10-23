# DEC-45: webcam resolution vs gaze estimation
Measures how 1080p / 720p / 480p input changes gaze estimation (pretrained only):
MediaPipe FaceLandmarker (detection, inter-ocular and iris px) and L2CS-Net ResNet50 (pitch/yaw);
angular error is computed against 1080p, matched by frame index.
Setup: `uv sync --python 3.12`; put `face_landmarker.task` (MediaPipe models bucket) and
`l2cs_gaze360_resnet50.safetensors` (huggingface.co/py-feat/l2cs) into `models/` (git-ignored; no pickle weights).
Put the recording at `rec/me-1080p.mp4`; 720p/480p copies are made there with ffmpeg.
Run: `uv run --python 3.12 python run.py rec/me-1080p.mp4`
Output: `results.csv` (per frame) and a markdown summary table on stdout.
Control: `uv run --python 3.12 python control.py .` re-encodes 1080p without scaling and measures the same error (noise floor).
