# Write a Python Program to cut a wav file audio in python.

from pydub import AudioSegement
audio=AudioSegement.from_wav("sound.wav")

cut_audio=audio[:1000]
cut_audio.export("cut_sound.wav",format="wav")