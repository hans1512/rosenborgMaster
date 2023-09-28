import os

import cv2
import shutil


def create_folder_structure(name):
    # Get current directory and create a folder with the given name
    current_dir = os.getcwd()
    path = os.path.join(current_dir, name)
    os.mkdir(path)
    sub_path = os.path.join(path, "obj_train_data")
    os.mkdir(sub_path)

    # Create the necessary files inside the parent folder
    data = os.path.join(path, "obj.data")
    data_file = open(data, "a")
    names = os.path.join(path, "obj.names")
    names_file = open(names, "a")
    train = os.path.join(path, "train.txt")
    train_file = open(train, "a")

    return data_file, names_file, train_file, sub_path


def write_data(predictions, file_name):
    data_file, names_file, train_file, sub_path = create_folder_structure(file_name + "_training_data")
    seen = []
    class_names = []
    # YOLO saves labels starting with frame "1"
    # Therefore we start counting at 1, so labels and images coincide when considering the file names
    image_counter = 1
    source_folder = predictions[0].save_dir + "\\labels"

    for prediction in predictions:
        name = file_name + "_" + str(image_counter)
        # Write each frame of the prediction to the correct folder
        image_path = sub_path + "\\" + name + ".jpg"
        cv2.imwrite(image_path, prediction.orig_img)

        # Move the labels text file from the predict dir
        # to the obj_train_data directory so it can be imported in cvat
        text_label_path = "\\" + name + ".txt"
        shutil.move(source_folder + text_label_path, sub_path + text_label_path)

        train_file.write("obj_train_data/" + name + ".jpg" + "\n")
        classes = prediction.boxes.cls
        for cls in classes:
            if not seen.__contains__(int(cls)):
                class_names.append(prediction.names[int(cls)])
                seen.append(cls)
        image_counter += 1

    nmbr_classes = len(seen)
    for name in class_names:
        names_file.write(name + "\n")

    data_file.write("classes = " + str(nmbr_classes))
    data_file.write("\nnames = obj.names")
    data_file.write("\ntrain = train.txt")
