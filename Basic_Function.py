import cv2
import numpy as np



kernal=np.ones((5,5),np.uint8)
# Here we have imported a image
img=cv2.imread("Resourses/lena.png")



#This function will convert the image to grap scale image
imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#This function will blur the image
imblur=cv2.GaussianBlur(img,(7,7),0)

#This function will detect the edge of the image
# Note if we imporve the value of the 150 and 200 we can get less or more edges of the images
imedge=cv2.Canny(img,150,200)

# Here we are imceasing the thinkness of the edges 
# note if we imporve the  iteration we can improve the width of the edges
imdialation=cv2.dilate(imedge,kernal,iterations=1)

# Here we are decrease the thinkness of the edges 
# note if we imporve the  iteration we can improve the width of the edges
imerode=cv2.erode(imdialation,kernal,iterations=1)

cv2.imshow("Gray image",imGray)
cv2.imshow("Blur image",imblur)
cv2.imshow("edge image",imedge)
cv2.imshow("dialiated  image",imdialation)
cv2.imshow("Eroded  image",imerode)


cv2.waitKey(0)
