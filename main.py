import ultralytics as ultralytics
import torch
from super_gradients.training import models
from ultralytics import NAS
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2


def define_model():
    yolo_nas_m = models.get("yolo_nas_m", pretrained_weights="coco")

    url = "frame99.jpg"
    yolo_nas_m.predict(url, conf=0.25).show()


define_model()
