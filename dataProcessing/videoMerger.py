from moviepy.editor import VideoFileClip, concatenate_videoclips

# List of video files to merge
video_files = ['2.mp4', "new.mp4", "2minutes.mp4"]  # Add or replace with your video file names

# Create a list of VideoFileClip objects
clips = [VideoFileClip(video) for video in video_files]

# Concatenate the video clips into one video clip
final_clip = concatenate_videoclips(clips, method="compose")

# Write the result to a file
final_clip.write_videofile("step1.mp4", codec='libx264')

# Print done message
print("Videos merged successfully!")





