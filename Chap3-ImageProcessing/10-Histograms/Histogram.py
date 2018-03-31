########################################################################
# Using Matplotlib
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('../../img/apple.jpg', 0)
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()

########################################################################
# Draw every channel
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('../../img/apple.jpg')
# color = ('b', 'g', 'r')
# for i, col in enumerate(color):
#     histr = cv.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr, color=col)
#     plt.xlim([0, 255])
# plt.show()

########################################################################
# Using OpenCV
########################################################################
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../../img/apple.jpg', 0)
# creat a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[20:220, 20:220] = 255
masked_img = cv.bitwise_and(img, img, mask=mask)
# Calculate histogram with/without mask
hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask), plt.xlim([0, 256])
plt.show()
