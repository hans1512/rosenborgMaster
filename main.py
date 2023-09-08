import ultralytics as ultralytics
from ultralytics import NAS
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2
import image_display


def define_model():
    model = NAS("yolo_nas_m.pt")
    model.info()
    image = Image.open("frame99.jpg")
    image_array = np.asarray(image)

    results = model.predict(image).show()

    image_display.plot_bboxes(image_array, results[0].boxes.boxes, score=False)

define_model()
