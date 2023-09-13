import random

import cv2
def ya():
    vidcap = cv2.VideoCapture('ES 19 Hamkam - Rosenborg.mov')
    success, image = vidcap.read()
    count = 0

    print(success)

    while count < 10000:
        rand = random.randint(0, 10)
        if (rand == 9):
            cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

ya()