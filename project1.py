import numpy as np
from PIL import Image
import cv2

def get_limits(color):
    c=np.uint8([[color]])
    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    
    lowerLimit=hsvc[0][0][0]-10,100,100
    upperLimit=hsvc[0][0][0]-10,255,255

    lowerLimit=np.array(lowerLimit,dtype=np.uint8)
    upperLimit=np.array(upperLimit,dtype=np.uint8)

    return lowerLimit,upperLimit

yellow=[107,154,193] #BGR colorspace
cap=cv2.VideoCapture(0)
address="https://10.0.0.81:8080/video"
cap.open(address)

while True:
    ret,frame=cap.read()
    hsvimage= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit=get_limits(color=yellow)
    mask =cv2.inRange(hsvimage,lowerLimit,upperLimit)
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