# #####Draw Histogram Graph
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('res/wiki.jpg',0)
# hist,bins= np.histogram(img.flatten(),256,[0,256])

# cdf=hist.cumsum()
# cdf_normalized=cdf*float(hist.max())/cdf.max()

# plt.plot(cdf_normalized,color='b')
# plt.hist(img.flatten(),256,[0,256],color='r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'),loc='upper left')
# plt.show()

# ######Using OpenCV method
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img=cv2.imread('res/wiki.jpg',0)
# equ=cv2.equalizeHist(img)
# res=np.hstack((img,equ))
# cv2.imshow('result',res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#####Adaptive Histogram Equalization(CLAHE)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('res/tuska.jpg',0)

clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1=clahe.apply(img)
res=np.hstack((img,cl1))
cv2.imshow('clahe',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

