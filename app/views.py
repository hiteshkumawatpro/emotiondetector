from dis import dis
from logging import getLevelName
from operator import ne
import re
from turtle import home
from urllib import response
from xml.sax.handler import feature_external_ges
from argon2 import hash_password
import cv2, sampsonDistance
from deepface import DeepFace



from django.http.response import HttpResponse
from django.urls.resolvers import URLPattern
from django.http import JsonResponse, request
from matplotlib.pyplot import cla
from app import camera
from app.camera import VideoCamera
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from cv2 import cv2
import numpy

def index(request):
    return render(request, "Home.html")

def page(request):
    return render(request, "EmotionReader.html")


dict = {}


def gen(camera):
    
    while True:
        frame,im = camera.get_frame()
        result = DeepFace.analyze(im, actions=['emotion'] ,enforce_detection=False)
        dict["anger"]   = result['emotion']['angry']
        dict["disgust"] = result['emotion']['disgust']
        dict["fear"]    = result['emotion']['fear']
        dict["happy"]     = result['emotion']['happy']
        dict["sad"] = result['emotion']['sad']
        dict["neutral"]   = result['emotion']['neutral']
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

def video_stream(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')

def da(request):
    data = dict
    return JsonResponse(data)
   
