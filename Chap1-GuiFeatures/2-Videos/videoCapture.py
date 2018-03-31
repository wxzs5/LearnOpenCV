##Using Camera
# import numpy as np
# import cv2 as cv

# cap=cv.VideoCapture(0)

# while(True):
#     ret,frame=cap.read()
#     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     cv.imshow('frame',gray)
#     if cv.waitKey(1)&0xff==ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

#Using video file
import numpy as np
import cv2 as cv
cap=cv.VideoCapture('../../img/bilibili.flv')
while(cap.isOpened()):
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1)&0xff==ord('q'):
        break
cap.release()
cv.destroyAllWindows()

##Saving a video
# import numpy as np
# import cv2 as cv

# cap=cv.VideoCapture(0)

# fourcc=cv.VideoWriter_fourcc(*'XVID')
# out= cv.VideoWriter('output.avi',fourcc,20.0,(640,480))

# while(cap.isOpened()):
#     ret,frame=cap.read()
#     if ret==True:
#         frame=cv.flip(frame,0)
#         out.write(frame)
#         cv.imshow('frame',frame)
#         if cv.waitKey(1)&0xff==ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv.destroyAllWindows()