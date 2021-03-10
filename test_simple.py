#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import time
from playsound import playsound
from threading import Thread


def play_sound():
    playsound(sys.argv[1])


T = Thread(target=play_sound)  # create thread
T.start()  # Launch created thread

SetLogLevel(0)

if not os.path.exists("model"):
    print(
        "download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

wf = wave.open(sys.argv[1], "rb")

print("The type is : ", type(wf))
time.sleep(3)
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    exit(1)

model = Model("model")
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(40000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        pass
        # print(rec.Result())

    else:
        pass
        # print(rec.PartialResult())


print(rec.FinalResult())
print("The type is : ", type(wf))