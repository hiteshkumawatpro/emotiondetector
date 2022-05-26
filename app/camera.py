from socket import fromshare
from tkinter import Frame
import cv2
import numpy as np
class VideoCamera(object):
    
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    def __del__(self):
        self.cap.release()
    def get_frame(self):
        ret, frame = self.cap.read()
       
        frame_flip = cv2.flip(frame, 1)
        ret, framee = cv2.imencode('.jpg', frame_flip)
        return framee.tobytes(),frame
    
       

        
