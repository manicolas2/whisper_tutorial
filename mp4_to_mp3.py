import sys
import ffmpeg

#######################################
# argv[1] - mp4 file path
# argv[1] - mp3 file path
#######################################

if __name__ == "__main__":
    stream = ffmpeg.input(sys.argv[1])
    stream = ffmpeg.output(stream, sys.argv[2])
    ffmpeg.run(stream)