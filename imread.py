##Using OpenCV frame
# import numpy as np
# import cv2
# img=cv2.imread('lenna.jpg')
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##Using matplotlib
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# img = cv2.imread('lenna.jpg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

##Write a image
import numpy as np
import cv2

img=cv2.imread('lenna.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)&0xff
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lennaGray.png',img)
    cv2.destroyAllWindows()
