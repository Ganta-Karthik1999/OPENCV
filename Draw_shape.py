import cv2
import numpy as np


img =np.zeros((512,512,3),np.uint8)

print(img.shape)

#img[100:500,100:500]=255,0,0

cv2.line(img,(0,0),(300,300),(255,0,0),3)
#cv2.rectangle(img,(0,0),(300,300),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPEN CV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(59,80,102))

cv2.imshow("Image",img)
cv2.waitKey(0)