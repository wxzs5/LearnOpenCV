# #####Draw Histogram Graph
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv.imread('../../img/wiki.jpg',0)
# hist,bins= np.histogram(img.flatten(),256,[0,256])

# cdf=hist.cumsum()
# cdf_normalized=cdf*float(hist.max())/cdf.max()

# plt.plot(cdf_normalized,color='b')
# plt.hist(img.flatten(),256,[0,256],color='r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'),loc='upper left')
# plt.show()

# ######Using OpenCV method
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img=cv.imread('../../img/wiki.jpg',0)
# equ=cv.equalizeHist(img)
# res=np.hstack((img,equ))
# cv.imshow('result',res)
# cv.waitKey(0)
# cv.destroyAllWindows()

#####Adaptive Histogram Equalization(CLAHE)
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('../../img/tuska.jpg',0)

clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1=clahe.apply(img)
res=np.hstack((img,cl1))
cv.imshow('clahe',res)
cv.waitKey(0)
cv.destroyAllWindows()

