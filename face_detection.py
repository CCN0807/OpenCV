from tkinter import font
import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector

video = cv.VideoCapture(0)
blank = np.zeros((500,500, 3), dtype='uint8')

haar_cascade = cv.CascadeClassifier('hear_face.xml')

hand_detect = HandDetector(detectionCon=0.8, maxHands=2)

operator = 0 # 0 is sum, 1 is minus, 2 is times, 3 is divided
operator_check = True
value = 0

if not video.isOpened():
    print("cannot open cam")
    exit()


while True:
    ret, frame = video.read()

    if not ret:
        print("Frame is not received")
        break

    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    hands, img = hand_detect.findHands(frame)

    for hand in hands:
        lmList = hand["lmList"]
        bbox = hand["bbox"]
        centerPoint = hand["center"]
        handTpye = hand["type"] 

        fingers = hand_detect.fingersUp(hand)
        number = 0
        for finger in fingers:
            if finger == 1:    
                number += 1

        if handTpye == "Left" and operator_check == True:
            if operator == 0:
                value = value + number
            if operator == 1:
                value = value - number
            if operator == 2:
                value = value * number
            if operator == 3:
                value = value/number
            
            operator_check = False
        
        elif handTpye == "Right":
            operator = number

            operator_check = True


        print(f"current value: {value}, current hand: {handTpye} operator: {operator}, check: {operator_check}")
        cv.putText(img, f"value: {value}, operator: {operator}, hand: {handTpye}", (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv.LINE_AA)    

    

    if(len(face_rect) != 0):
        for (x, y, w, h) in face_rect:
            center = (int(x + w/2), int(y +h/2))
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)
            cv.imshow('Detected faces', frame)


    if cv.waitKey(1) == ord('q'):
        break


cv.waitKey(0)
