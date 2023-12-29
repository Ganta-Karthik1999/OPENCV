import numpy as np
from PIL import Image
import cv2


def empty(a):
    pass


yellow=[120,160,200] #BGR colorspace
cap=cv2.VideoCapture(0)
#address="https://10.0.0.81:8080/video"
#cap.open(address)

cv2.namedWindow("image")
cv2.resizeWindow("image",640,240)
cv2.createTrackbar("Hue min","image",0,179,empty)
cv2.createTrackbar("Hue max","image",179,179,empty)
cv2.createTrackbar("Saturation min","image",0,255,empty)
cv2.createTrackbar("Saturation max","image",255,255,empty)
cv2.createTrackbar("value min","image",0,255,empty)
cv2.createTrackbar("value max","image",255,179,empty)



while True:
    ret,frame=cap.read()
    imgHSV= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue min","image")
    h_max=cv2.getTrackbarPos("Hue max","image")
    s_min=cv2.getTrackbarPos("Saturation min","image")
    s_max=cv2.getTrackbarPos("Saturation max","image")
    v_min=cv2.getTrackbarPos("value min","image")
    v_max=cv2.getTrackbarPos("value max","image")

    # print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    
    lower1=np.array([0,18,40])
    upper1=np.array([39,255,179])
    mask1=cv2.inRange(imgHSV,lower1,upper1)
    

    mask=cv2.inRange(imgHSV,lower,upper)
    
    imgResult=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Original image",frame)
    cv2.imshow("HSV image",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Resultant image",imgResult)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    print(bbox)
    if bbox is not None:
        x1,y1,x2,y2=bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    cv2.imshow('Frame',frame)

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()