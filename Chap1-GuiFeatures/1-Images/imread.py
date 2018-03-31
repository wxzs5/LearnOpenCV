##Using OpenCV frame
# import numpy as np
# import cv2 as cv
# img=cv.imread('../../img/lenna.jpg')
# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

##Using matplotlib
# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
# img = cv.imread('../../img/lenna.jpg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

##Write a image
import numpy as np
import cv2 as cv

img=cv.imread('../../img/lenna.jpg',0)
cv.imshow('image',img)
k=cv.waitKey(0)&0xff
if k==27:
    cv.destroyAllWindows()
elif k==ord('s'):
    cv.imwrite('lennaGray.png',img)
    cv.destroyAllWindows()
