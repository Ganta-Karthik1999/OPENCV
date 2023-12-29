import cv2
import numpy as np

img=cv2.imread('Resourses/lena.png')

horizontal=np.hstack((img,img))

vertical=np.vstack((img,img))



cv2.imshow("Horizontal stack",horizontal)
cv2.imshow("vertical stack",vertical)

cv2.waitKey(0)