# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('sudoku.png',0)
# laplacian=cv.Laplacian(img,cv.CV_64F)
# sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
# sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

# plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title('Original'),plt.xticks([]),plt.yticks([])
# plt.subplot(222),plt.imshow(laplacian,cmap='gray'),plt.title('Laplician'),plt.xticks([]),plt.yticks([])
# plt.subplot(223),plt.imshow(sobelx,cmap='gray'),plt.title('Sobelx'),plt.xticks([]),plt.yticks([])
# plt.subplot(224),plt.imshow(sobely,cmap='gray'),plt.title('Sobely'),plt.xticks([]),plt.yticks([])
# plt.show()

#####Bilateral Satuation
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('../../img/sudoku.png',0)
# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)
# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()