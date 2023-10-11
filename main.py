import torch.version
import gc
from super_gradients.training import models, Trainer
from torchinfo import summary
from ultralytics import NAS, YOLO

from export_YOLO_annotations import write_data
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
    yolov8 = YOLO('runs/detect/NewDataset5008/wights/best.pt')
    results = yolov8.train(
        data='Hans300Training/data.yaml',
        imgsz=[1980, 1020],
        epochs=1,
        batch=1,
        name='NewestTest')

    predict_file = "30Sec.mp4"
    predictions = yolov8(predict_file, save=True, save_txt=True, conf=0.3)

  #  file_without_extension = predict_file.split(".")[0]

   # write_data(predictions, file_without_extension)


if __name__ == "__main__":
    print("Hello")
    define_YOLO()
