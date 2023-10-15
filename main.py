import cv2
import torch.version
import gc
from super_gradients.training import models, Trainer
from torchinfo import summary
from ultralytics import NAS, YOLO
from matplotlib import pyplot as plt

import boxmot


def define_NAS():
    device = 'cuda' if torch.cuda.is_available() else "cpu"
    input_video_path = "30Sec.mp4"
    output_video_path = input_video_path + "-detections.mp4"
    device = 0
    yolo_nas_l = models.get("yolo_nas_l", pretrained_weights="coco")
    summary(model=yolo_nas_l,
            input_size=(16, 3, 640, 640),
            col_names=['input_size',
                       'output_size',
                       'num_params',
                       'trainable'],
            col_width=20,
            row_settings=['var_names'])
    url = "frames/frame1181.jpg"
    torch.cuda.empty_cache()
    # Using cuda
    yolo_nas_l.to(device).predict(url).save(output_video_path)
    # Not using cuda
    # yolo_nas_l.predict(input_video_path).save(output_video_path)


# Might work later?
def something():
    nas = NAS("yolo_nas_l.pt")
    nas.info()
    result = nas("frames/frame0.jpg")


def define_YOLO():
    device = 0
    yolov8 = YOLO('yolov8l.pt')
    results = yolov8.train(
        data='yolov8_training/data.yaml',
        imgsz=[1980, 1020],
        epochs=500,
        batch=6,
        name='From_scratch_new_data_V')

    predict_file = "30Sec.mp4"
    predictions = yolov8(predict_file, save=True, save_txt=True, conf=0.3)


#  file_without_extension = predict_file.split(".")[0]

# write_data(predictions, file_without_extension)


def edge_detection():
    img = cv2.imread('RBKScreenshot.PNG', 0)
    edges = cv2.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(edges, cmap='gray')

    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    print("Hello")
    define_YOLO()
