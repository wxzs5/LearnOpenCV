########################################################################
# Scaling
########################################################################
# import numpy as np
# from matplotlib import pylab as plt
# import cv2 as cv
# img= cv.imread('../../img/messi5.jpg')
# res= cv.resize(img,None,fx=0.3,fy=0.3,interpolation=cv.INTER_CUBIC)
# # cv.imwrite('messi5.png',res)
# cv.imshow('res',res)
# cv.waitKey(0)
# cv.destroyAllWindows()

########################################################################
# Translation
########################################################################
# import numpy as np
# from matplotlib import pylab as plt
# import cv2 as cv
# img = cv.imread('../../img/messi5.png',0)
# rows,cols = img.shape

# M= np.float32([[1,0,50],[0,1,50]])
# dst= cv.warpAffine(img,M,(cols,rows))

# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

########################################################################
# Rotation
########################################################################
# import numpy as np
# from matplotlib import pylab as plt
# import cv2 as cv
# img=cv.imread('../../img/messi5.png',0)
# rows,cols= img.shape

# M= cv.getRotationMatrix2D((cols/2,rows/2),45,1)
# dst = cv.warpAffine(img,M,(cols,rows))

# cv.imshow('img',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

########################################################################
# Affine Transformation
########################################################################
# import numpy as np
# from matplotlib import pylab as plt
# import cv2 as cv
# img=cv.imread('../../img/messi5.png')
# rows,cols,ch=img.shape

# pts1=np.float32([[50,50],[200,50],[50,200]])
# pts2=np.float32([[10,100],[200,50],[100,250]])

# M= cv.getAffineTransform(pts1,pts2)

# dst = cv.warpAffine(img,M,(cols,rows))

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()


########################################################################
# Perspective Transformation
########################################################################
import numpy as np
from matplotlib import pylab as plt
import cv2 as cv
img = cv.imread('../../img/messi5.png')
rows, cols, ch = img.shape

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
