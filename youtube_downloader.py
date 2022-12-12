from pytube import YouTube
import sys

#######################################
# argv[1] - url to youtube video
#######################################

if __name__ == "__main__":
    yt = YouTube(sys.argv[1])
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()