import cv2
# Replace with the actual file paths
image_file = 'matiasAnnotations/matiasAnnotations_255.jpg'
yolo_boxes_file = 'matiasAnnotations_1.txt'

# Read the image
image = cv2.imread(image_file)
height, width, _ = image.shape

# Function to convert YOLO bounding box format to (x, y, w, h)
def yolo_to_opencv(yolo_box, img_width, img_height):
    x_center, y_center, box_width, box_height = yolo_box
    x_center *= img_width
    y_center *= img_height
    box_width *= img_width
    box_height *= img_height
    x = int(x_center - box_width / 2)
    y = int(y_center - box_height / 2)
    w = int(box_width)
    h = int(box_height)
    return x, y, w, h

# Read YOLO format bounding boxes from the file and draw them on the image
with open(yolo_boxes_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])  # If you need the class ID
        yolo_box = [float(x) for x in parts[1:]]
        x, y, w, h = yolo_to_opencv(yolo_box, width, height)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Change color and thickness as needed

# Show the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', image)

# Wait for a key press and then close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()