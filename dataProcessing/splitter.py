from moviepy.editor import VideoFileClip


def split_video(video_path, output_path_1, output_path_2):
    """
    Split a video into two halves and save them.

    Parameters:
    - video_path (str): The path to the input video file.
    - output_path_1 (str): The path to save the first half.
    - output_path_2 (str): The path to save the second half.
    """
    # Load the video
    clip = VideoFileClip(video_path)

    # Get the duration of the video
    duration = clip.duration

    # Split the video into two halves
    clip1 = clip.subclip(0, duration / 2)
    clip2 = clip.subclip(duration / 2, duration)

    # Save the two halves
    clip1.write_videofile(output_path_1, codec="libx264", audio_codec="aac")
    clip2.write_videofile(output_path_2, codec="libx264", audio_codec="aac")

    # Close the clips
    clip1.close()
    clip2.close()
    clip.close()

# Example usage:
# split_video('path_to_your_video.mp4', 'first_half.mp4', 'second_half.mp4')

split_video("../annotations.mp4", "Matias_annotations.mp4", "Hans_Annotations.mp4")