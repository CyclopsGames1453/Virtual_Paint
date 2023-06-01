import cv2
import numpy as np


#set the camera resolution
#the higher resolution slower the processes
frameWidth = 640
frameHeight = 480

#set the camera
url = 0

#read camera and set camera resolution
cam = cv2.VideoCapture(url)
cam.set(3,frameWidth)
cam.set(4,frameHeight)
cam.set(10,150)

def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,359,nothing)
cv2.createTrackbar("H2","frame",0,359,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)

#update camera
while cam.isOpened():
    ret,frame = cam.read()

    if not ret:
        print("! Camera cannot be read !")
        break

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #create color Trackbars
    H1 = int( cv2.getTrackbarPos("H1","frame") / 2)
    H2 = int( cv2.getTrackbarPos("H2","frame") / 2)
    S1 = cv2.getTrackbarPos("S1","frame")
    S2 = cv2.getTrackbarPos("S2","frame")
    V1 = cv2.getTrackbarPos("V1","frame")
    V2 = cv2.getTrackbarPos("V2","frame")
    
    #set color in color Trackbars
    lower=np.array([H1,S1,V1])
    upper=np.array([H2,S2,V2])

    mask=cv2.inRange(hsv,lower,upper)

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    #It turns off when you press the q key.
    if  cv2.waitKey(1) & 0xFF == ord("q"):
        print("logged out")
        break

cv2.destroyAllWindows()






































