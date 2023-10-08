import random

import cv2


def ya():
    vidcap = cv2.VideoCapture('dataProcessing/matiasAnnotations.mp4')
    success, image = vidcap.read()
    count = 1

    print(success)

    while count < 10000:
        cv2.imwrite("matiasAnnotations_training_data/obj_train_data/matiasAnnotations_" + str(count) + ".jpg", image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

