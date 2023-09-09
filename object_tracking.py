import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

  
tracker = cv2.TrackerCSRT_create();


returned, img = video.read()


bbox = cv2.selectROI("Tracking", img, False)


tracker.init(img, bbox)

print(bbox)

def drawbox(img,bbox):
      x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])   
      cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2,1)
      cv2.putText(img,"succesfuly connected with the server",(200,40),cv2.FONT_HERSHEY_TRIPLEX,0.5,(21, 237, 223 ),2,22,)
while True:
    check,img = video.read()   
    ret,bbox=tracker.update(img)
    if ret:
        drawbox(img,bbox )
    else:
        cv2.putText(img,"connection has been lost with the server",(200,40),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,0),2,22,) 
       

    cv2.imshow("result",img)

            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()







