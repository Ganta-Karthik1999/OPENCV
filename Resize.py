import cv2
import numpy as np

#Here we have imported a image

img=cv2.imread("Resourses/lambo.png")

print(img.shape)

img_reshape=cv2.resize(img,(300,200))
print(img_reshape.shape)

cv2.imshow("Lambo image",img)
cv2.imshow("Lambo reshaped image",img)
cv2.waitKey(0)
