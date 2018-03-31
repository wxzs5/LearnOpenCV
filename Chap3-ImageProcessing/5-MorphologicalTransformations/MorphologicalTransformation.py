import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# #####Erosion
# img=cv.imread('../../img/j.png',0)
# kernel=np.ones((5,5),np.uint8)
# erosion=cv.erode(img,kernel,iterations=1)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(erosion),plt.title('erosion img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Dilation
# img=cv.imread('../../img/j.png',0)
# kernel=np.ones((5,5),np.uint8)
# dilation=cv.dilate(img,kernel,iterations=1)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(dilation),plt.title('dilation img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Opening
# img=cv.imread('../../img/jopen.png',0)
# kernel=np.ones((5,5),np.uint8)
# opening=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(opening),plt.title('Opening img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Closing
# img=cv.imread('../../img/jclose.png',0)
# kernel=np.ones((5,5),np.uint8)
# closing=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(closing),plt.title('Closing img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Morphological Gradient
# img=cv.imread('../../img/j.png',0)
# kernel=np.ones((5,5),np.uint8)
# gradient=cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(gradient),plt.title('gradient img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Top Hat
# img=cv.imread('../../img/j.png',0)
# kernel=np.ones((9,9),np.uint8)
# tophat=cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(tophat),plt.title('tophat img'),plt.xticks([]),plt.yticks([])
# plt.show()

#####Black Hat
img=cv.imread('../../img/j.png',0)
kernel=np.ones((9,9),np.uint8)
blackhat=cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)
plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blackhat),plt.title('blackhat img'),plt.xticks([]),plt.yticks([])
plt.show()