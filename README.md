# Project Title

Whisper Test

## Description

Testing OpenAI's Whisper. It makes a transcription from a youtube video and output an srt file that can be used as the subtitle for the video.

### Executing program

This repository has 3 programs in it.

## 1. youtube_downloader.py

```
python3.9 youtube_downloader.py "<url of the youtube video>"
```

## 2. mp4_to_mp3.py

```
python3.9 mp4_to_mp3.py "<path to the mp4 file>" "<path to the mp3 file>"
```

## 3. whisper_test.py

model - tiny, base, small, medium, large

to translate - True / False (whether to translate the transcription to English)

```
python3.9 whisper_test.py <model> "<path to the mp3 file>" "<language>" "<to translate>" "<path to the srt file>"
```
