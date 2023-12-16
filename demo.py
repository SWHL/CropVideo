# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from crop_video import CropVideo

cutter = CropVideo()

video_path = "tests/test_files/1.mp4"
cutter(video_path, "00:00:00", "00:00:10", "output/2.mp4")
