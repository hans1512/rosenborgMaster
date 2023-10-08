import cv2
import numpy as np
import random

# Replace this with the path to your video file
input_video_path = '../30Sec.mp4'

# This will be the output video file with random frames
output_video_path = 'maakeFrames.mp4'

# Open the video file
cap = cv2.VideoCapture(input_video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Couldn't open video file.")
    exit()

# Get the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Generate 50 unique random frame indices
random_frame_indices = random.sample(range(total_frames), 50)

# Sort the frame indices to read frames in order
random_frame_indices.sort()

# Get the video's width, height, and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec to be used to save the video. *'mp4v' is for .mp4 format
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Read and write each random frame to the new video file
for frame_index in random_frame_indices:
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

print(f"Done! {len(random_frame_indices)} random frames saved to {output_video_path}.")
