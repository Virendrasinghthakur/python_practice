# Write a Python Program to play a wav file in python using pydub library

from pydub import AudioSegment
from pydub.playback import play

sound=AudioSegment.from_wav("")

play(sound)