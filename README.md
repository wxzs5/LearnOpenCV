# OpenCV Python Tutorials Source Code

## Also available in :cn: [中文](Chinese.md)

## :memo:Introduction
Help you quickly familiar with OpenCV API. All code tested in **python3**. you can clone the code and read the [official tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) to learn OpenCV. This repository formerly is my own learning OpenCV code, and  I also fixed some bugs merged into [official OpenCV master branch](https://github.com/opencv/opencv). Every ```.py``` file in this repo corresponding to a page in the official tutorials. So you can read the tutorial and test the code side by side.

## :question: Why this work
* Official tutorial not offer test pictures in code, this project gathered it.
* OpenCV source code offer demo code, but not corresponding to the official tutorials.
* Some other OpenCV tutorial are mainly focused on C++.

## :page_facing_up: How to use

* Install pip
    *  If you are in linux e.g in Ubuntu. you can run the fellowing command in terminal:
    ```bash
    sudo apt-get install python3-pip
    sudo pip3 install --upgrade pip
    ```
    * if you are in windows environment pip will be automatically installed when you install python.

* Install opencv-python package
Using ```pip``` package manager to install opencv python bindings.
```bash
sudo pip3 install opencv-python opencv-contrib-python
```

* Clone the repo
```bash
git clone https://github.com/wxzs5/LearnOpenCV.git
```

* Just run!
for example:
```bash
python3 Chap1-GuiFeatures/1-Images/imread.py
```
or you can run it in your own IDE,Editor and what ever you want.
* Attention!
    * **Some python files has multi sections of code. Sections are organized exclusive. So you should uncomment the code section you want to run and comment the other sections** 
    * these sections often has this format head:
    ```python
    ################################################
    # Title
    ################################################
    ```
    ![](http://p1t73p0s6.bkt.clouddn.com/18-4-3/16430034.jpg)

## Others
* If this repo help you learn opencv,please give a **star** and to help more people.
* Welcome to submit PRs and post issues. 




