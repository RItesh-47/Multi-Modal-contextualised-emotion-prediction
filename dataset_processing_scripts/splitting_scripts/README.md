# Scripts

This folder consists to the two scripts used to convert the files with audio and video with synced `English` subtitles to the their context and utterance.

## Directory

- `script.py`
- `mp_split_final.py`

## Run Instructions

`python3 script.py <srt_path> `

`python3 mp_split_final.py myOutFile.txt <av_path> 1 1&`

## Libraries Used

1. `moviepy.editor` - for video editing tasks such as cutting, concatenations, title insertions.
2. `csv` - to read and write CSV files.
3. `sys` - to use command line arguments.
4. `os` - to interact with the operating system, for tasks like changing the working directory or creating directories.
