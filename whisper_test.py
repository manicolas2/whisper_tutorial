import whisper
import datetime
import sys

#######################################
# argv[1] - model (tiny, base, small, medium, large)
# argv[2] - path to file to the mp3 file
# argv[3] - language
# argv[4] - to translate? (True or False)
# argv[5] - srt file name
#######################################



if __name__ == "__main__":

    model = whisper.load_model(sys.argv[1])
    translate = str(sys.argv[4]).lower()
    result = model.transcribe(sys.argv[2], fp16=False, language=sys.argv[3], task="translate") if translate == "true" else model.transcribe(sys.argv[2], fp16=False, language=sys.argv[3])
    segments = result["segments"]

    for segment in segments:
        startTime = f"{str(0)}{str(datetime.timedelta(seconds=int(segment['start'])))},000"
        endTime = f"{str(0)}{str(datetime.timedelta(seconds=int(segment['end'])))},000"
        text = segment['text']
        segmentId = segment['id'] + 1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        with open(sys.argv[5], "a", encoding="utf-8") as srt:
            srt.write(segment)
