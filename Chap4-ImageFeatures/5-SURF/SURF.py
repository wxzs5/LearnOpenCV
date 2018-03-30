import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#SURF is 3 times faster than SIFT while performance is comparable to SIFT.
#SURF is good at handling images with blurring and rotation, but not good at handling viewpoint change and illumination change.

img = cv.imread('res/fly.jpg',0)
# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv.xfeatures2d.SURF_create(400)
# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)
print( len(kp) )

#### SURF Method
# Check present Hessian threshold
print( surf.getHessianThreshold() )
# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.setHessianThreshold(50000)
# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img,None)
print( len(kp) )

img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)

#### U-SURF Method(it won't find the orientation)
# Check upright flag, if it False, set it to True
print( surf.getUpright() )

surf.setUpright(True)
# Recompute the feature points and draw it
kp = surf.detect(img,None)
img3 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
plt.subplot(121),plt.imshow(img2),plt.title('SURF'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(img3),plt.title('U-SURF'),plt.xticks([]),plt.yticks([])
plt.show()

#### Check the descriptor size and change it to 128 if it is only 64-dim
# Find size of descriptor
print( surf.descriptorSize() )

# That means flag, "extended" is False.
surf.getExtended()

# So we make it to True to get 128-dim descriptors.
surf.setExtended(True) #BUG
kp, des = surf.detectAndCompute(img,None)
print( surf.descriptorSize() )

print( des.shape )
