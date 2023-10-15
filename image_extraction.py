import random

import cv2


def ya():
    vidcap = cv2.VideoCapture('videos/Hans_Annotations.mp4')
    success, image = vidcap.read()
    count = 1

    print(success)

    while count < 10000:
        cv2.imwrite("HansAnnotations_training_data/images/Hans_Annotations_" + str(count) + ".jpg", image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

ya()