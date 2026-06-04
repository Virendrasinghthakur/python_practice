# Write a Python Program to play a video in python

import cv2
video=cv2.VideoCapture("C:/Users/Asus/Videos/VID_20240731_183119.mp4")

while True:
    ret,frame=video.read()


    if not ret:
        break

    cv2.imshow("Video",frame)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()