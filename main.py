import torch.version
import gc
from super_gradients.training import models, Trainer
from torchinfo import summary
from ultralytics import NAS, YOLO


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
    yolov8 = YOLO('runs/detect/yolov8n_cuda3/weights/best.pt')
    CHECKPOINT_DIR = 'checkpoints'
    trainer = Trainer(experiment_name="yolo_player_detectionv1", ckpt_root_dir=CHECKPOINT_DIR)

    results = yolov8.train(
        data='yolov8_training/data.yaml',
        imgsz=[1980, 1020],
        epochs=2,
        batch=2,
        name='yolov8n_cuda')

    yolov8.predict("30sec.mp4", save=True, conf=0.3)


if __name__ == "__main__":
    print("Hello")
    define_YOLO()
