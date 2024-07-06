import os
import subprocess
import sys
from audio_extractor import convert_video_to_audio_moviepy
from argparse import ArgumentParser

def extract_prosodic_features(audio_file, output_file):
    """Extracts prosodic features using `openSMILE`"""
    cwd = os.getcwd()
    config_path = os.path.join(cwd, "config/prosody/prosodyShs.conf")
    command = ["SMILExtract", "-C", config_path, "-I", audio_file, "-O", output_file]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
def remove_audio_file(audio_file):
    """Removes the audio file"""
    os.remove(audio_file)

def get_features_for_file(input_file, output_file=None, output_ext="csv"):
    """Extracts prosodic features from a given video file"""
    filename, ext = os.path.splitext(input_file)
    audio_file = f"{filename}.wav"
    output_file = output_file if output_file else f"{filename}.csv"
    convert_video_to_audio_moviepy(input_file, output_ext="wav")
    extract_prosodic_features(audio_file, output_file)
    remove_audio_file(audio_file)

if __name__=="__main__":
    args = ArgumentParser()
    args.add_argument("-d", "--dir", type=str, required=True, dest="input_dir", help="Path to video directory")
    args.add_argument("-e", "--output-file-ext", type=str, dest="output_file_ext", default=None, help="Extension of output file")
    args = args.parse_args()
    input_dir = args.input_dir
    output_file_ext = args.output_file_ext
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4") and filename.__contains__("utterance"):
            input_file = os.path.join(input_dir, filename)
            get_features_for_file(input_file, output_ext=output_file_ext)
            print(f"Processed: {input_file}")
    print("Done")

    
    