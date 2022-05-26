
from lib2to3.pgen2.token import NAME
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [path("",views.index),
               path("EmotionReader.html", views.page),
               path('video_stream', views.video_stream, name='video_stream'),
              path('d/',views.da,name='da'),
    ]