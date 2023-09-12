import ultralytics as ultralytics
import torch
from super_gradients.training import models, Trainer
from ultralytics import NAS, YOLO
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2

device = 0 if torch.cuda.is_available() else "cpu"

def define_NAS():
    yolo_nas_m = models.get("yolo_nas_m", pretrained_weights="coco")

    url = "frame99.jpg"
    yolo_nas_m.predict(url, conf=0.25).show()


def define_YOLO():
    yolov8 = YOLO('yolov8n.pt')
    CHECKPOINT_DIR = 'checkpoints'
    trainer = Trainer(experiment_name="yolo_player_detectionv1", ckpt_root_dir=CHECKPOINT_DIR)
    results = yolov8.train(
        data='yoloTraining/data.yaml',
        imgsz=640,
        epochs=10,
        batch=8,
        name='yolov8n_custom')
    url = "frame99.jpg"
    yolov8.predict(url)


define_YOLO()