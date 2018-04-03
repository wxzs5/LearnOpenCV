# OpenCV 教程源码

## :memo:介绍
使用python3帮助你快速熟悉OpenCV的API。这本来是我学习[官方教程](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)写的代码，修改了官方教程中的一部分，把代码提取了出来，还改正了一部分bug,现在已经融合到了官方的主分支里. 你可以边阅读官方的opencv-python教程，边使用这些代码做实验测试，作为学习参考。本仓库的代码都只在**Python3**上测试过。

## :question: 为什么有这个project
* 大家知道OpenCV是和图片紧密贴合的库，而官方教程并没有专门提供实验所需的照片，我这里帮大家把实验所需的照片收集好了，大家不用再到处找实验照片。
* ＯpenCV的源代码库是提供demo的，但是和他的教程却不搭配，这个项目是完全对应官方教程的。
* 其他的OpenCV教程都是关注在Ｃ++上，而Python的教程较少。
* 开源精神！

## :page_facing_up: 如何使用

* 安装 pip
    *  如果你在linux环境下，比如ubuntu下可以在终端中运行:
    ```bash
    sudo apt-get install python3-pip
    sudo pip3 install --upgrade pip
    ```
    * 如果你在windows环境下那么在安装python的时候，pip就自动安装好了。

* 安装opencv-python包
使用pip安装
```bash
sudo pip3 install opencv-python opencv-contrib-python
```

* 下载代码
```bash
git clone https://github.com/wxzs5/LearnOpenCV.git
```

* 然后就可以直接运行
比如:
```bash
python3 Chap1-GuiFeatures/1-Images/imread.py
```
或者你也可以在IDE或编辑器里面运行。

* 注意!
    * **有一些python文件含有多个代码片段，这些代码片段设计得都可以单独运行，所以你使用时要自行选择取消注释你想要运行的代码段** 
    * 这些代码段都按照一下的格式组织:
    ```python
    ################################################
    # Title
    ################################################
    ```
    ![](http://p1t73p0s6.bkt.clouddn.com/18-4-3/16430034.jpg)

## 其他
* 如果你觉得这些代码帮助到了你请给本仓库:star: **star**,让更多人知道，从而帮助更多人，感谢！
* 欢迎提交 PR 和　issues。




