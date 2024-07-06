from ffmpeg import FFmpeg, Progress
import os

CWD = os.getcwd()
raw_data_dir = os.path.join(CWD,'..','raw_data')

def main():
    ffmpeg = (
        FFmpeg()
        .option("i", os.path.join(raw_data_dir,"DSC_Utterance_1.mp4"))
        # .input("input.mov")
        .option("vn")
        .output(
            os.path.join(raw_data_dir,"DSC_Utterance_1.mp3"),
            acodec="copy"
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    ffmpeg.execute()


if __name__ == "__main__":
    main()