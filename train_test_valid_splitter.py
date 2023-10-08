import os
import shutil
import random

# Function to ensure the directory exists, if not, create it
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to split the dataset into train, valid, and test sets
def split_dataset(orig_folder):
    curr = os.getcwd()
    source_images_folder = os.path.join(curr, orig_folder, "images")
    source_labels_folder = os.path.join(curr, orig_folder, "labels")

    # Creating paths for the train, valid, and test sets for both images and labels
    sets = ['train', 'valid', 'test']
    folders = {s: {'images': os.path.join(curr, orig_folder, s, "images"),
                   'labels': os.path.join(curr, orig_folder, s, "labels")} for s in sets}

    # Ensure all directories exist
    for set_name, dirs in folders.items():
        ensure_dir(dirs['images'])
        ensure_dir(dirs['labels'])

    # Get the list of all files (assuming they have the same names, just different extensions)
    file_list = [f.rsplit('.', 1)[0] for f in os.listdir(source_images_folder) if f.endswith('.jpg')]
    random.shuffle(file_list)

    # Split ratios
    total_files = len(file_list)
    num_test = num_valid = total_files // 10  # 10% for test and valid each
    num_train = total_files - num_test - num_valid  # 80% for training

    # Distributing files into the respective sets
    splits = {'train': file_list[:num_train],
              'valid': file_list[num_train:num_train + num_valid],
              'test': file_list[num_train + num_valid:]}

    # Copying files to their respective directories
    for set_name, files in splits.items():
        for file_name in files:
            # Copy image files
            shutil.copy(os.path.join(source_images_folder, file_name + '.jpg'),
                        os.path.join(folders[set_name]['images'], file_name + '.jpg'))
            # Copy label files
            shutil.copy(os.path.join(source_labels_folder, file_name + '.txt'),
                        os.path.join(folders[set_name]['labels'], file_name + '.txt'))

    print("Dataset splitting complete.")

# Call the function with the name of your original folder containing the 'images' and 'labels' subfolders
split_dataset("matiasAnnotations")
