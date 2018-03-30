#It's very suit for SLAM
import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../../img/blox.jpg',0)
# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.subplot(121),plt.imshow(img),plt.title('Source'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img2),plt.title('ORB'),plt.xticks([]),plt.yticks([])
plt.show()