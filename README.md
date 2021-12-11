### ClipVideo
- 该仓库依托于`moviepy`库实现长视频自定义时间点多段切分
- 支持whl安装

#### TODO
- [ ] 剪辑video保存为gif时，很大，甚至比同等剪辑时间的MP4还要大
- [ ] 发现moviepy不能处理rmvb格式视频

#### 安装
```sh
pip install whl/ClipVideo-0.0.1-py3-none-any.whl
```

#### 使用方法
- 命令行使用
    ```bash
    # 命令行直接运行
    ClipVideo clip_info.txt
    ```
- 代码调用
    ```python
    from ClipVideo import ClipVideo

    cliper = ClipVideo()
    cliper('clip_info.txt')
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