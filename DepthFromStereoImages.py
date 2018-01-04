#OpenCV samples contain an example of generating disparity map and its 3D reconstruction. Check stereo_match.py in OpenCV-Python samples.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
imgL = cv.imread('res/tsukuba_l.png',0)
imgR = cv.imread('res/tsukuba_r.png',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()


