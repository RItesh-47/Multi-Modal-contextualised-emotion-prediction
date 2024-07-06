import sys
import os 
import subprocess
import time

def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    """Converts video to audio using ffmpeg"""
    filename, ext = os.path.splitext(video_file)
    output_file = f"{filename}.{output_ext}"
    print("filename ",filename)
    print("EXT",ext)
    print("OUTPUT",output_file)
    # cmd = f"ffmpeg -i {video_file} -vn -acodec copy {output_file}"
    # # subprocess.run(cmd, shell=True)
    ffmpeg_command = ["ffmpeg", "-i", video_file, "-vn", "-acodec", "copy", output_file]


    completed_process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ffmpeg_output = completed_process.stderr.decode("utf-8")

    # Print the ffmpeg output
    # print(ffmpeg_output)

    # Check if the duration of the generated audio file matches the duration of the original video file
    # video_duration = get_duration(video_file)
    # audio_duration = get_duration(output_file)
    # if video_duration is not None and audio_duration is not None:
    #     if round(video_duration, 2) != round(audio_duration, 2):
    #         print("Warning: The duration of the generated audio file does not match the duration of the video.")
    # else:
    #     print(f"Skipping: Unable to determine duration for {video_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    # print(directory)
    s = time.time()
    for filename in os.listdir(directory):
       
        if filename.endswith(".mp4"):  # Process only mp4 files, adjust accordingly if needed
            video_file = os.path.join(directory, filename)
            print(video_file)
            # print(f"Processing: {video_file}")
            convert_video_to_audio_ffmpeg(video_file)
            # break
    e = time.time()
    print(e - s)
