### ClipVideo
- 该仓库依托于`moviepy`库实现长视频自定义时间点多段切分
- 支持whl安装

#### TODO
- [ ] 剪辑video保存为gif时，很大，甚至比同等剪辑时间的MP4还要大
- [ ] 发现moviepy不能处理rmvb格式视频

#### 安装
```sh
pip install whl/ClipVideo-0.0.1-py3-none-any.whl -i https://pypi.douban.com/simple/
```

#### 使用方法
- 命令行使用
    ```bash
    # clip_info_str: "视频路径,保存裁剪视频名称,开始时间,结束时间"
    ClipVideo --clip_info_str "assets/1.mp4,1_part.mp4,00:00:00,00:00:20"
    ```
- 代码调用
    ```python
    from ClipVideo import ClipVideo

    cliper = ClipVideo()
    cliper(clip_info_path='clip_info.txt')
    ```

#### clip_info.txt组成
- 第一行是剪辑视频的全路径
- 剩余行：
    - 保存剪辑后的video名称,剪辑开始时间,剪辑结束时间
- 例子如下：
    ```text
    assets/1.mp4
    11.mp4,00:00:01,00:00:05
    12.mp4,00:00:06,00:00:08
    ```

#### 参数说明
|参数名称|参数介绍|
|:---:|:---:|
|--clip_info_str|按照字符串方式传入，具体字符串类型可以参考上面**命令行调用**部分|
|--clip_info_path|以txt格式传入，可以同时对同一个视频做多次裁剪，txt写法参考上部分|
|--save_dir|裁剪后的视频保存路径,默认是当前目录下创建`video_clip`目录存储|