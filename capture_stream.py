import cv2
import numpy as np
import time

url_cable  = 'http://169.254.220.11:5000/video'

data = np.zeros((480, 640))
cv2.namedWindow('win')
cv2.imshow('win', data)
while True:
    start_time = time.time()
    cap = cv2.VideoCapture(url_cable)
    ret, frame = cap.read()

    cv2.imshow('win', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    cap.release()
    print("FPS:"+str(1.0/(time.time() - start_time)))