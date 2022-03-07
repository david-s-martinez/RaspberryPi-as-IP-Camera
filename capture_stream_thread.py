from threading import Thread
import cv2, time

class ThreadedCamera(object):
    def __init__(self, src = 0):
        self.src = src
        # FPS = 1/X
        # X = desired FPS
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)
        self.thread = Thread(target = self.update, args = ())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            self.capture = cv2.VideoCapture(self.src)
            self.capture.set(cv2.CAP_PROP_BUFFERSIZE,10)
            (self.status, self.frame) = self.capture.read()
            # time.sleep(self.FPS)
            self.capture.release()

    def show_frame(self):
        cv2.imshow('frame', self.frame)
        key = cv2.waitKey(self.FPS_MS)
        if key == 27:
            raise Exception('exit window')

if __name__ == '__main__':
    src = 'http://169.254.220.11:5000/video'
    threaded_camera = ThreadedCamera(src)
    while True:
        try:
            threaded_camera.show_frame()
        except AttributeError:
            pass