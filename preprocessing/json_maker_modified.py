import os
import sys
import csv
import json
import bisect
from datetime import timedelta


# I have assumed that the data is organised as 
# utterance audio in "utterance_audio" folde
# context video in "context" folder
# times.csv file in the main directory
# srt file in the main directory

def convert_seconds_to_hhmmss(seconds):
    return str(timedelta(seconds=float(seconds)))

def extract_subtitle(srt_file, target_time):
    subtitle_lines = ""
    with open(srt_file, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.isdigit():
                start_time = str(lines[i+1].split(' --> ')[0][:-4])
                if start_time == str(target_time.zfill(8)):
                    subtitle_lines += lines[i+2].strip()
                    subtitle_lines +=" "
                    subtitle_lines += lines[i+3].strip()
                    break
    return subtitle_lines

def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3",output_path = ""):
    input_file = ffmpeg.input(f"{video_file}.mp4")
    input_file.output(f'{output_path}.{output_ext}', acodec='mp3',  loglevel="quiet").run()
    print(f"{video_file} has been converted to audio.")



def main():
    if len(sys.argv) < 5:
        print("Usage: python json-maker.py <directory> <short movie name> <srt file> <language> <index_start>")
        return
    directory = sys.argv[1]
    MOVIE_NAME = sys.argv[2]
    srt_file = sys.argv[3]
    language = sys.argv[4]
    index = int(sys.argv[5])  # Initialize index variable



        
    data = {}
    audio_files=[]
    context_files=[]
    csv_file_path = os.path.join(directory, "times.csv")
    srt_file_path = os.path.join(directory, srt_file)
    audio_files_directory = os.path.join(directory, "utterance_audio")
    context_files_directory = os.path.join(directory, "context")

    for filename in os.listdir(audio_files_directory):
        if filename.endswith(".mp3"):
            audio_files.append(filename)
    for filename in os.listdir(context_files_directory):
        if filename.endswith(".mp4"):
            context_files.append(filename)
    context_files.sort()
    audio_files.sort()



    i = 0

    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            i = i + 1
            utterance_start_time = convert_seconds_to_hhmmss(row["utterance_start_time"])
            utterance_end_time = convert_seconds_to_hhmmss(row["utterance_end_time"])
            context_name = str(row["context_name"])+".mp4"
            utterance_name = row["utterance_name"]
            audio_name = f"{utterance_name}.mp3"

            srt_for_utterance = extract_subtitle(srt_file_path, convert_seconds_to_hhmmss(float(row["utterance_start_time"]) + 0.5))
            #search for audio file

            index_A = bisect.bisect_left(audio_files, audio_name)
            if index_A == len(audio_files) or audio_files[index_A] != audio_name:
                print(f"{audio_name} not found!!")
                continue
            #search for context
            index_C = bisect.bisect_left(context_files, context_name)
            if index_C == len(context_files)  or context_files[index_C] != context_name:
                print(f"{context_name} not found!!")
                continue
            
            data[str(index)] = {  # Use index as key
                    "movieShortname": MOVIE_NAME,
                    "language" : language,
                    "startTime": utterance_start_time,
                    "endTime": utterance_end_time,
                    "contextId": context_name,
                    "subtitle": srt_for_utterance,
                    "asrText": "",  
                    "audioFileID": audio_name,
                    "videoFileID": audio_name[:-3] + "mp4",
                    "textFeaturesFileID": "",
                    "audioFeaturesFileID": "",
                    "videoFeaturesFileID": ""
                }

            print(context_name)
            index += 1  # Increment index for the next entry

    with open(f"{MOVIE_NAME}.json", "w") as json_file:
        json.dump(data, json_file, indent=3)

    print(f"Data has been saved to {MOVIE_NAME}.json")

if __name__ == "__main__":
    main()