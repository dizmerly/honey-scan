import cv2
import time
import requests
import base64
from api_key import API_TOKEN
import json




def takeImage(exposure):
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    time.sleep(exposure)
    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.imwrite('images/c1.png', frame)

def getImage(img):
    return img

def scanItem():
    with open("main.py") as file:
        exec(file.read())


while (True):
    q1 = input("Take an image? y/n or STOP\n")
    if(q1 == "y"):
        print("Place item in front of camera\n")
        takeImage(1)
        q2 = input("Run program? y/n \n")
        if (q2 == "y"):
            scanItem()
    elif(q1 == "n"):
        print(0)
    elif(q1 == "STOP"):
        break







