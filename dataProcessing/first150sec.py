import cv2
import numpy as np

# Replace this with the path to your video file
input_video_path = 'ES 13 Rosenborg - Lillestrøm.mov'

# This will be the output video file with selected frames
output_video_path = 'hel kamp.mp4'

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Couldn't open video file.")
    exit()

# Get the video's frames per second (fps)
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate the frame indices for the 30th and 33rd minute
start_frame = int(0 * 60 * fps)
end_frame = int(100 * 60 * fps)

# Calculate the step to get 100 evenly spaced frames between the 30th and 33rd minute
step = (end_frame - start_frame) // 150

# Create a list of frame indices to extract
frame_indices = list(range(start_frame, end_frame, step))[:150]  # Limit to 100 frames

# Get the video's width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec to be used to save the video. *'mp4v' is for .mp4 format
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Read and write each selected frame to the new video file
for frame_index in frame_indices:
    # Set the current position of the video file to the specific frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    
    # Read the frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print(f"Error: Couldn't read frame {frame_index}.")
        continue

    # Write the frame to the new video file
    out.write(frame)

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()

print(f"Done! {len(frame_indices)} frames saved to {output_video_path}.")
