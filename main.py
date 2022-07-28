import cv2
import playsound
import time
from email_tester import SendMail

mouth_cascade = cv2.CascadeClassifier('Mouth.xml')
cap = cv2.VideoCapture(0)
ds_factor = 0.5
md = 0
capture=0
p_number=0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    md=0

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
    for (x,y,w,h) in mouth_rects:
        y = int(y - 0.15*h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
        md=1
        break


    cv2.imshow('Mouth Detector', cv2.flip(frame,1))

    if(md==1):
        capture += 1
        if(capture == 5):
            cv2.imwrite("person "+ str(p_number)+".png",frame)
            SendMail("person " + str(p_number)+".png")
            print("Image sent")
            capture = 0
            p_number += 1

        else:
            playsound.playsound('Camera Shot.mp3', False)
            playsound.playsound('wear_a_mask.mp3', False)
            time.sleep(3)
        md=0



    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
