# import cv2
# import numpy as np 

# img=cv2.imread('lenna.jpg')
# px=img[100,100]
# print(px)

# blue=img[100,100,0]
# print(blue)

import cv2
import numpy as np
from matplotlib import pylab as plt 

BLUE=[255,0,0]
img1=cv2.imread('opencv-logo.jpg')

replicate=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE) 
reflect=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray',),plt.title('Original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('Replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('Reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('Reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('Wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('Constant')

plt.show()