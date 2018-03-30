import cv2
import numpy as np
from matplotlib import pyplot as plt

######Simple Thresholding
# img=cv2.imread('../../img/gradient.png',0)
# ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC) 
# ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

#####Adaptive Thresholding
# img=cv2.imread('../../img/sudoku.png',0)
# # img=cv2.medianBlur(img,5)

# ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# titles=['Origin Image','Global Thresholding(v=127)','Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']
# images=[img,th1,th2,th3]

# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

#####Otsu's Binarization
img = cv2.imread('../../img/sudoku.png',0)
# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

#####otsu's method in python implemention
# img = cv2.imread('../../img/sudoku.png',0)
# blur = cv2.GaussianBlur(img,(5,5),0)
# # find normalized_histogram, and its cumulative distribution function
# hist = cv2.calcHist([blur],[0],None,[256],[0,256])
# hist_norm = hist.ravel()/hist.max()
# Q = hist_norm.cumsum()
# bins = np.arange(256)
# fn_min = np.inf
# thresh = -1
# for i in range(1,256):
#     p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
#     q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
#     b1,b2 = np.hsplit(bins,[i]) # weights
#     # finding means and variances
#     m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
#     v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
#     # calculates the minimization function
#     fn = v1*q1 + v2*q2
#     if fn < fn_min:
#         fn_min = fn
#         thresh = i
# # find otsu's threshold value with OpenCV function
# ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# print( "{} {}".format(thresh,ret) )