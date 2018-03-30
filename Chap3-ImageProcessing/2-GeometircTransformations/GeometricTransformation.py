import numpy as np 
from matplotlib import pylab as plt 
import cv2

#####Scaling
# img= cv2.imread('../../img/messi5.jpg')
# res= cv2.resize(img,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_CUBIC)
# # cv2.imwrite('messi5.png',res)
# cv2.imshow('res',res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#####Translation
# img = cv2.imread('../../img/messi5.png',0)
# rows,cols = img.shape

# M= np.float32([[1,0,50],[0,1,50]])
# dst= cv2.warpAffine(img,M,(cols,rows))

# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #####Rotation
# img=cv2.imread('../../img/messi5.png',0)
# rows,cols= img.shape

# M= cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
# dst = cv2.warpAffine(img,M,(cols,rows))

# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #####Affine Transformation
# img=cv2.imread('../../img/messi5.png')
# rows,cols,ch=img.shape

# pts1=np.float32([[50,50],[200,50],[50,200]])
# pts2=np.float32([[10,100],[200,50],[100,250]])

# M= cv2.getAffineTransform(pts1,pts2)

# dst = cv2.warpAffine(img,M,(cols,rows))

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()


#####Perspective Transformation
img=cv2.imread('../../img/messi5.png')
rows,cols,ch =img.shape

pts1= np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2= np.float32([[0,0],[300,0],[0,300],[300,300]])

M=cv2.getPerspectiveTransform(pts1,pts2)
dst= cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
