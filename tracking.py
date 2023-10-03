import cv2
import numpy as np
from pathlib import Path

from boxmot import DeepOCSORT
from ultralytics import YOLO

tracker = DeepOCSORT(
    model_weights=Path('osnet_x0_25_msmt17.pt'),  # which ReID model to use
    device='cuda:0',
    fp16=True,
)

file_name = "2sec.mp4"

input_video = cv2.VideoCapture(file_name)

output_video = file_name.split(".")[0] + "_tracking_output.mp4"

width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID'
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

color = (0, 0, 255)  # BGR
thickness = 2
fontscale = 0.5

yolov8 = YOLO('best.pt')

while True:
    ret, im = input_video.read()

    if not ret:
        break

    predicted = yolov8.predict(im, conf=0.3)

    dets = predicted[0].boxes.data.cpu().numpy()

    # substitute by your object detector, input to tracker has to be N X (x, y, x, y, conf, cls)
    # dets = np.array([[144, 212, 578, 480, 0.82, 0],
    #                  [425, 281, 576, 472, 0.56, 65]])

    tracks = tracker.update(dets, im)  # --> (x, y, x, y, id, conf, cls, ind)

    xyxys = tracks[:, 0:4].astype('int')  # float64 to int
    ids = tracks[:, 4].astype('int')  # float64 to int
    confs = tracks[:, 5]
    clss = tracks[:, 6].astype('int')  # float64 to int
    inds = tracks[:, 7].astype('int')  # float64 to int

    # in case you have segmentations or poses alongside with your detections you can use
    # the ind variable in order to identify which track is associated to each seg or pose by:
    # segs = segs[inds]
    # poses = poses[inds]
    # you can then zip them together: zip(tracks, poses)

    # print bboxes with their associated id, cls and conf
    if tracks.shape[0] != 0:
        for xyxy, id, conf, cls in zip(xyxys, ids, confs, clss):
            im = cv2.rectangle(
                im,
                (xyxy[0], xyxy[1]),
                (xyxy[2], xyxy[3]),
                color,
                thickness
            )
            cv2.putText(
                im,
                f'id: {id}, conf: {conf}, c: {cls}',
                (xyxy[0], xyxy[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                fontscale,
                color,
                thickness
            )

    out.write(im)

input_video.release()
out.release()
cv2.destroyAllWindows()
