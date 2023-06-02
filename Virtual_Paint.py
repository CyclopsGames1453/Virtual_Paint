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

#set color ranges
myColors=[[110/2,70,70,170/2,255,255],#green
          ]

#bgr
myColorValues = [[0,255,0],#green
                 ]

myPoints = [] #[x,y,colorID]

#find color ranges in myColors
def findColor(img,colors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in colors:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)  
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)

        if x!=0 or y != 0:
            newPoints.append([x,y,count])
            
        count+=1
        #cv2.imshow("mask",mask)

    return newPoints

#update draw on canvas
def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)

#find draw object
def getContours(img):
    countours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

# create window
cv2.namedWindow("frame")

#update camera
while cam.isOpened():
    ret,frame=cam.read()

    if not ret:
        print("! Camera cannot be read !")
        break
    
    cv2.resize(frame,(frameWidth,frameHeight))

    #paint canvas
    imgResult = frame.copy()
    newPoints = findColor(frame,myColors)

    if len(newPoints) > 0:
        for newp in newPoints:
            myPoints.append(newp)

    if len(myPoints) > 0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("frame",imgResult)

    #It reset paint when you press the r key.
    if  cv2.waitKey(1) & 0xFF == ord("r"):
        print("reset my points")
        myPoints = []

    #It turns off when you press the q key.
    elif  cv2.waitKey(1) & 0xFF == ord("q"):
        print("logged out")
        break

cv2.destroyAllWindows()
