import torch.version
import gc
from super_gradients.training import models, Trainer
from ultralytics import NAS, YOLO


def define_NAS():
    device = 'cuda' if torch.cuda.is_available() else "cpu"
    input_video_path = "30Sec.mp4"
    output_video_path = input_video_path + "-detections.mp4"
    device = 0
    yolo_nas_l = models.get("yolo_nas_l", pretrained_weights="coco")
    url = "frame99.jpg"
    torch.cuda.empty_cache()
    #Using cuda
    yolo_nas_l.to(device).predict(input_video_path).save(output_video_path)
    # Not using cuda
    # yolo_nas_l.predict(input_video_path).save(output_video_path)


def define_YOLO():
    ah = torch.cuda.is_available()
    cuda_id = torch.cuda.current_device()
    name = torch.cuda.get_device_name(cuda_id)
    print(name)
    yolov8 = YOLO('runs/detect/yolov8n_custom10/weights/best.pt')
    CHECKPOINT_DIR = 'checkpoints'
    trainer = Trainer(experiment_name="yolo_player_detectionv1", ckpt_root_dir=CHECKPOINT_DIR)

    # results = yolov8.train(
    #     data='data.yaml',
    #     imgsz=640,
    #    epochs=10,
    #     batch=8,
    #    name='yolov8n_custom')

    yolov8.predict("frames/frame2.jpg", save=True, conf=0.3)


if __name__ == "__main__":
    define_NAS()
