import cv2
import numpy as np

def empty(a):
    pass


#Here we have imported a image

img=cv2.imread("Resourses/farm.jpg")
cv2.namedWindow("image")
cv2.resizeWindow("image",640,240)
cv2.createTrackbar("Hue min","image",0,179,empty)
cv2.createTrackbar("Hue max","image",179,179,empty)
cv2.createTrackbar("Saturation min","image",0,255,empty)
cv2.createTrackbar("Saturation max","image",255,255,empty)
cv2.createTrackbar("value min","image",0,255,empty)
cv2.createTrackbar("value max","image",255,179,empty)


imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:

    h_min=cv2.getTrackbarPos("Hue min","image")
    h_max=cv2.getTrackbarPos("Hue max","image")
    s_min=cv2.getTrackbarPos("Saturation min","image")
    s_max=cv2.getTrackbarPos("Saturation max","image")
    v_min=cv2.getTrackbarPos("value min","image")
    v_max=cv2.getTrackbarPos("value max","image")

    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    lower1=np.array([0,103,0])
    upper1=np.array([179,172,175])
    

    mask=cv2.inRange(imgHSV,lower,upper)
    mask1=cv2.inRange(imgHSV,lower1,upper1)
    imgResult=cv2.bitwise_and(img,img,mask=mask1)

    cv2.imshow("Original image",img)
    cv2.imshow("HSV image",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Mask1",mask1)
    cv2.imshow("Resultant image",imgResult)
    
    cv2.waitKey(1)
