from socket import fromshare
from tkinter import Frame
from cv2 import cv2
import numpy as np
from fer import FER
from deepface import DeepFace
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
    def get_emotions(self):
        ret , frame = self.cap.read()
        result = DeepFace.analyze(frame,actions = ['emotion'])
        # print result
        print(result)

        
