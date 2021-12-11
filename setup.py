# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: setup.py
# @Author: SWHL
# @Contact: liekkaskono@163.com
import setuptools

setuptools.setup(
    name='ClipVideo',
    version='0.0.1',
    platforms='Any',
    description='Clip Video',
    author='SWHL',
    author_email='liekkaskono@163.com',
    url='https://github.com/SWHL/VideoOCR',
    license='Apache-2.0',
    py_modules="ClipVideo",
    include_package_data=True,
    install_requires=["moviepy"],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':['ClipVideo=ClipVideo.clip_video:main']
    }
)