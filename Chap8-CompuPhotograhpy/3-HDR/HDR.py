import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Loading exposure images into a list
img_fn = ["../../img/img0.png", "../../img/img1.png", "../../img/img2.png", "../../img/img3.png"]
img_list = [cv.imread(fn) for fn in img_fn]
exposure_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)

merge_debvec = cv.createMergeDebevec()
hdr_debvec = merge_debvec.process(img_list, times=exposure_times.copy())
merge_robertson = cv.createMergeRobertson()
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy())

# Tonemap HDR image
tonemap1 = cv.createTonemapDurand(gamma=2.2)
res_debvec = tonemap1.process(hdr_debvec.copy())
tonemap2 = cv.createTonemapDurand(gamma=1.3)
res_robertson = tonemap2.process(hdr_robertson.copy())

# Exposure fusion using Mertens
merge_mertens = cv.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

# Convert datatype to 8-bit and save
res_debvec_8bit = np.clip(res_debvec*255, 0, 255).astype('uint8')
res_robertson_8bit = np.clip(res_robertson*255, 0, 255).astype('uint8')
res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')

plt.subplot(1, 3, 1), plt.imshow(res_debvec_8bit)
plt.title('debvec'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(res_robertson_8bit)
plt.title('robertson'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(res_mertens_8bit)
plt.title('mertens'), plt.xticks([]), plt.yticks([])
plt.show()