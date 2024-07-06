import sys
import os 
from moviepy.editor import VideoFileClip
import time

def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}", logger=None, verbose=False)

    # Check if the duration of the generated audio file matches the duration of the original video file
    video_duration = clip.duration
    audio_duration = clip.audio.duration
    if round(video_duration, 2) != round(audio_duration, 2):
        print("Warning: The duration of the generated audio file does not match the duration of the video.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    s= time.time()
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):  # Process only mp4 files, adjust accordingly if needed
            video_file = os.path.join(directory, filename)
            print(f"Processing: {video_file}")
            convert_video_to_audio_moviepy(video_file)
    e = time.time()
    print(e-s)
