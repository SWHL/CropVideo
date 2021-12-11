# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: main.py
# @Time: 2021/06/27 08:53:22
# @Author: Max
import argparse
from pathlib import Path
import sys

from tqdm import tqdm
from moviepy import editor


def mkdir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


class ClipVideo(object):
    def __init__(self) -> None:
        pass

    def __call__(self, clip_info_path):
        print('Reading the clip info')
        video_path, clip_info_list = self.read_clip_info(clip_info_path)

        save_clip_dir = Path('video_clip') / Path(video_path).stem
        mkdir(save_clip_dir)

        with editor.VideoFileClip(video_path) as cliper:
            for one_clip_info in tqdm(clip_info_list):
                clip_video_name, clip_start, clip_end = one_clip_info

                save_clip_path = str(save_clip_dir / clip_video_name)
                self.save_clip_video(cliper, save_clip_path,
                                     clip_start, clip_end)
        print('The cropped video has been saved '
             f'under video_clip/{Path(video_path).stem}')

    @staticmethod
    def read_clip_info(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            clip_info = list(map(lambda x: x.rstrip(), f))

        video_path = clip_info[0]
        clip_info_list = list(map(lambda x: x.split(','), clip_info[1:]))
        return video_path, clip_info_list

    @staticmethod
    def save_clip_video(cliper, clip_video_name, clip_start, clip_end):
        save_suffix = clip_video_name.split('.')[-1]

        clip_video = cliper.subclip(clip_start, clip_end)

        with editor.CompositeVideoClip([clip_video]) as final_video:
            if save_suffix == 'mp4':
                final_video.write_videofile(clip_video_name)
            elif save_suffix == 'gif':
                final_video.write_gif(clip_video_name, fps=8)
            else:
                raise ValueError(f'not support {save_suffix}!')


def main():
    clip_videoer = ClipVideo()

    clip_info_path = sys.argv[1]
    if Path(clip_info_path).is_file():
        clip_videoer(clip_info_path)
    else:
        print(f'{clip_info_path} is not a file!')
        sys.exit(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('clip_info_path', type=str, default='clip_info.txt')
    args = parser.parse_args()

    clip_videoer = ClipVideo()
    clip_videoer(args.clip_info_path)

