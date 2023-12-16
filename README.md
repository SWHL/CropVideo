### Cut Video
该仓库依托于[moviepy](https://github.com/Zulko/moviepy)库实现长视频自定义时间点多段切分

⚠️注意：不支持`rmvb`格式视频裁剪

#### 安装
```bash
pip install crop_video
```

#### 命令行使用
```bash
# 视频路径 开始时间 结束时间 保存裁剪视频路径
$ crop_video 1.mp4 00:00:00 00:00:20 result.mp4
```

#### Python脚本使用
```python
from crop_video import CropVideo

cutter = CropVideo()

video_path = "tests/test_files/1.mp4"
cutter(video_path, "00:00:00", "00:00:10", "output/2.mp4")
```
