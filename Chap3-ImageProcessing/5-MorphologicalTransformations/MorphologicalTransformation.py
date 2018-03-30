import cv2
import numpy as np
from matplotlib import pyplot as plt

# #####Erosion
# img=cv2.imread('../../img/j.png',0)
# kernel=np.ones((5,5),np.uint8)
# erosion=cv2.erode(img,kernel,iterations=1)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(erosion),plt.title('erosion img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Dilation
# img=cv2.imread('../../img/j.png',0)
# kernel=np.ones((5,5),np.uint8)
# dilation=cv2.dilate(img,kernel,iterations=1)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(dilation),plt.title('dilation img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Opening
# img=cv2.imread('../../img/jopen.png',0)
# kernel=np.ones((5,5),np.uint8)
# opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(opening),plt.title('Opening img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Closing
# img=cv2.imread('../../img/jclose.png',0)
# kernel=np.ones((5,5),np.uint8)
# closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(closing),plt.title('Closing img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Morphological Gradient
# img=cv2.imread('../../img/j.png',0)
# kernel=np.ones((5,5),np.uint8)
# gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(gradient),plt.title('gradient img'),plt.xticks([]),plt.yticks([])
# plt.show()

# #####Top Hat
# img=cv2.imread('../../img/j.png',0)
# kernel=np.ones((9,9),np.uint8)
# tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(tophat),plt.title('tophat img'),plt.xticks([]),plt.yticks([])
# plt.show()

#####Black Hat
img=cv2.imread('../../img/j.png',0)
kernel=np.ones((9,9),np.uint8)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.subplot(121),plt.imshow(img),plt.title('source img'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blackhat),plt.title('blackhat img'),plt.xticks([]),plt.yticks([])
plt.show()