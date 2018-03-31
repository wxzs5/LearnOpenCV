########################################################################
# 2D Convolution
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('../../img/opencv_logo.png')
# kernel = np.ones((5, 5), np.float32) / 25
# dst = cv.filter2D(img, -1, kernel)

# plt.subplot(121), plt.imshow(img), plt.title(
#     'Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst), plt.title(
#     'Averaging'), plt.xticks([]), plt.yticks([])
# plt.show()

########################################################################
# Blurring (Averaging)
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('../../img/opencv_logo.png')
# blur = cv.blur(img, (5, 5))

# plt.subplot(121), plt.imshow(img), plt.title(
#     'Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(blur), plt.title(
#     'Blurred'), plt.xticks([]), plt.yticks([])
# plt.show()

########################################################################
# Blurring (Gaussian)
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('../../img/opencv_logo.png')
# blur = cv.GaussianBlur(img, (5, 5), 0)

# plt.subplot(121), plt.imshow(img), plt.title(
#     'Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(blur), plt.title(
#     'Gaussian Blurred'), plt.xticks([]), plt.yticks([])
# plt.show()

########################################################################
# Blurring (Median)
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv.imread('../../img/opencv_logo_blur.png')
# median = cv.medianBlur(img, 5)

# plt.subplot(121), plt.imshow(img), plt.title(
#     'Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(median), plt.title(
#     'Median Blurred'), plt.xticks([]), plt.yticks([])
# plt.show()

########################################################################
# Blurring (Bilateral)
########################################################################
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('../../img/opencv_logo.png')
blur = cv.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title(
    'Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title(
    'Bilateral Blurred'), plt.xticks([]), plt.yticks([])
plt.show()
