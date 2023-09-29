import os

# Specify the folder path here
folder_path = '../yolov8_training/test/labels'

# Get all files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Iterate through each file
for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    # Open the file in read mode and read lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode to overwrite it
    with open(file_path, 'w') as file:
        for line in lines:
            # Split the line into parts
            parts = line.split()

            # Check if there are any parts and the first part is a number
            if parts and parts[0].isdigit():
                number = int(parts[0])

                # Check if the number is not 0 or 1
                if number != 0 and number != 1:
                    parts[0] = '1'

            # Join the parts back into a line and write to the file
            file.write(' '.join(parts) + '\n')