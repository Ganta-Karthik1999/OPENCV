import cv2
import numpy as np

img=cv2.imread("Resourses/card.png")
img_reshape=cv2.resize(img,(512,512))

cv2.imshow("Image",img_reshape)
cv2.waitKey(0)
