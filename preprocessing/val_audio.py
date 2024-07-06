import os
import wave

from pydub import AudioSegment

def compare_audio_files(wav_file, mp3_file):
    """Compare the content of a WAV file and an MP3 file."""

    audio_wav = AudioSegment.from_wav(wav_file)
    audio_mp3 = AudioSegment.from_mp3(mp3_file)
    
    if audio_wav.raw_data == audio_mp3.raw_data:
        return True
    else:
        return False


def main():
    directory = "C:/Users/manis/OneDrive/Desktop/New folder (2)"
    moviepy=[]
    ffmpeg=[]
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            ffmpeg.append(filename)
        elif filename.endswith(".mp3"):
            moviepy.append(filename)
    moviepy.sort()
    ffmpeg.sort()
    # print(ffmpeg)

    for moviepy_file, ffmpeg_file in zip(moviepy, ffmpeg):
        ffmpeg_file= os.path.join(directory,ffmpeg_file)
        moviepy_file= os.path.join(directory,moviepy_file)
        # print( moviepy_file,ffmpeg_file)
        if os.path.exists(ffmpeg_file) and os.path.exists(moviepy_file):
            if compare_audio_files(ffmpeg_file, moviepy_file):
                print(f"Audio content of {ffmpeg_file} and {moviepy_file} is identical.")
            else:
                print(f"Audio content of {ffmpeg_file} and {moviepy_file} differs.")
        else:
            print(f"Corresponding files for {ffmpeg_file}' or {moviepy_file} not found.")
        
    


if __name__ == "__main__":
    main()
