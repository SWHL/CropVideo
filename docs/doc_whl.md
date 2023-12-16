#### Installation
```bash
pip install crop_video
```

#### Use by CLI
```bash
# video_path start_time end_time save_path
$ crop_video 1.mp4 00:00:00 00:00:20 result.mp4
```

#### Use by python
```python
from crop_video import CropVideo

cutter = CropVideo()

video_path = "tests/test_files/1.mp4"
cutter(video_path, "00:00:00", "00:00:10", "output/2.mp4")
```