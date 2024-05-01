import cv2
import time


# with open("main.py") as file:
#     exec(file.read())

def takeImage(exposure):
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
    time.sleep(exposure)
    ret,frame = cap.read() # return a single frame in variable `frame`
    cv2.imwrite('images/c1.png', frame)

def getImage(img):
    return img

takeImage(2)



# while(True):
#     cv2.imshow('img1',frame) #display the captured image
#     if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
#         cv2.imwrite('images/c1.png',frame)
#         cv2.destroyAllWindows()
#         break
#
# cap.release()






