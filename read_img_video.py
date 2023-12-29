import cv2

# Here we have imported a image
# img=cv2.imread("Resourses/lena.png")

# cv2.imshow("Lena image",img)
# cv2.waitKey(0)

#Here we will import the video

# cap=cv2.VideoCapture("Resourses/test.mp4")

# while True:
#     correct,img1=cap.read()
#     cv2.imshow("This is a test video",img1)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

#Here we will be  using a webcam

cap1=cv2.VideoCapture(0)

cap1.set(3,640)
cap1.set(4,480)
cap1.set(10,100)

while True:
    correct,img2=cap1.read()
    cv2.imshow("This is a test video",img2)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
