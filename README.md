<div align="center">
    <div align="center">
    <h1><b><i>Crop ✄ Video 📀</i></b></h1>
    </div>

<a href=""><img src="https://img.shields.io/badge/Python->=3.6,<3.12-aff.svg"></a>
<a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Win%2C%20Mac-pink.svg"></a>
<a href="https://pypi.org/project/crop-video/"><img alt="PyPI" src="https://img.shields.io/pypi/v/crop-video"></a>
<a href="https://pepy.tech/project/crop-video"><img src="https://static.pepy.tech/personalized-badge/crop-video?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads"></a>
<a href="https://semver.org/"><img alt="SemVer2.0" src="https://img.shields.io/badge/SemVer-2.0-brightgreen"></a>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

</div>


### 简介
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
