########################################################################
# Brute-Force Matching with ORB Descriptors
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img1 = cv.imread('../../img/book1.jpg', 0)
# img2 = cv.imread('../../img/book2.jpg', 0)

# orb = cv.ORB_create()

# # find keypoints
# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

# # create BFMatcher
# bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# # match descriptors
# matches = bf.match(des1, des2)

# # Sort result by distance
# matches = sorted(matches, key=lambda x: x.distance)

# # draw first 10 matches
# img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# plt.imshow(img3), plt.show()

########################################################################
# Brute-Force Matching with SIFT Descriptors and Ratio Test
########################################################################
# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt

# img1 = cv.imread('../../img/book1.jpg', 0)
# img2 = cv.imread('../../img/book2.jpg', 0)

# sift = cv.xfeatures2d.SIFT_create()

# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)

# # BFMatcher with default params
# bf = cv.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)

# # Apply ratio test
# good = []
# for m, n in matches:
#     if m.distance < 0.75 * n.distance:
#         good.append([m])

# # cv.drawMatchesKnn expects list of lists as matches.
# img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good[:20], None, flags=2)

# plt.imshow(img3), plt.show()

########################################################################
# FLANN based Matcher(More faster than BF matcher)
########################################################################
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('../../img/book1.jpg', 0)
img2 = cv.imread('../../img/book2.jpg', 0)

# Initiate SIFT detector
sift = cv.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=0)

img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

plt.imshow(img3), plt.show()
