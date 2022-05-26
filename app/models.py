
from django.db import models
from cv2 import cv2
import numpy as np
# Create your models here.

class img(models.Model):
    img_cus = models.ImageField(upload_to="User_Search/", null=True)

