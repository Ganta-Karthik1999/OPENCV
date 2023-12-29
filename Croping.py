import cv2
import numpy as np

#Here we have imported a image

img=cv2.imread("Resourses/lambo.png")

imcrop=img[0:200,200:500]

print(img.shape)
cv2.imshow("Original image",img)
cv2.imshow("Cropped image",imcrop)
cv2.waitKey(0)
