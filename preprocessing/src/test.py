import asyncio

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg

import os
CWD = os.getcwd()
raw_data_dir = os.path.join(CWD,'..','raw_data')


async def main():
    if not os.path.exists(os.path.join(raw_data_dir, "DSC_Utterance_1.mp3")):
        ffmpeg = (
            FFmpeg()
            .option("i", os.path.join(raw_data_dir,"DSC_Utterance_1.mp4"))
            # .input(os.path.join(raw_data_dir,"Dear_Father.mkv"))
            .option("vn")
            # .option("acodec", "copy")
            .output(
                os.path.join(raw_data_dir,"DSC_Utterance_1.mp3"),
                acodec="copy"
            )
        )

        @ffmpeg.on("progress")
        def on_progress(progress: Progress):
            print(progress)

        await ffmpeg.execute()


if __name__ == "__main__":
    asyncio.run(main())