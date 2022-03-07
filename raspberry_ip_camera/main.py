import numpy as np
from flask import Flask,render_template,Response
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
from camera import VideoCamera
import time
import threading
import os

camera = VideoCamera()
app = Flask(__name__)
def generate_frames(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
    return Response(generate_frames(camera),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=False)
