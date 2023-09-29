import os
import shutil
import random


def split(orig_folder):
    # Set the path to your source folder containing files to be split
    curr = os.getcwd()
    source_folder = curr + "/" + orig_folder + "/images"
    lab_folder = curr + "/" + orig_folder + "/labels"

    # Set the paths for the train, test, and valid folders
    train_folder = curr + "/" + orig_folder + "/train/images"
    test_folder = curr + "/" + orig_folder + "/test/images"
    valid_folder = curr + "/" + orig_folder + "/valid/images"

    train_folder_lab = curr + "/" + orig_folder + "/train/labels"
    test_folder_lab = curr + "/" + orig_folder + "/test/labels"
    valid_folder_lab = curr + "/" + orig_folder + "/valid/labels"

    # Define the split ratios
    train_ratio = 0.8
    test_ratio = 0.1
    valid_ratio = 0.1

    # Get a list of all files in the source folder
    file_list = os.listdir(source_folder)

    # Shuffle the file list randomly
    random.shuffle(file_list)

    # Calculate the number of files for each split
    total_files = len(file_list)
    num_train = int(total_files * train_ratio)
    num_test = int(total_files * test_ratio)
    num_valid = int(total_files * valid_ratio)

    # Split the files into train, test, and valid sets
    train_files = file_list[:num_train]
    test_files = file_list[num_train:num_train + num_test]
    valid_files = file_list[num_train + num_test:]

    # Copy files to the train folder
    for file_name in train_files:
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(train_folder, file_name)

        lab_orig = os.path.join(lab_folder, file_name.split(".")[0] + ".txt")
        lab_dest = os.path.join(train_folder_lab, file_name.split(".")[0] + ".txt")

        shutil.copy(lab_orig, lab_dest)
        shutil.copy(source_path, dest_path)

    # Copy files to the test folder
    for file_name in test_files:
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(test_folder, file_name)

        lab_orig = os.path.join(lab_folder, file_name.split(".")[0] + ".txt")
        lab_dest = os.path.join(test_folder_lab, file_name.split(".")[0] + ".txt")

        shutil.copy(lab_orig, lab_dest)
        shutil.copy(source_path, dest_path)

    # Copy files to the valid folder
    for file_name in valid_files:
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(valid_folder, file_name)

        lab_orig = os.path.join(lab_folder, file_name.split(".")[0] + ".txt")
        lab_dest = os.path.join(valid_folder_lab, file_name.split(".")[0] + ".txt")

        shutil.copy(lab_orig, lab_dest)
        shutil.copy(source_path, dest_path)

    print("Splitting complete.")


split("Hans300Training")
