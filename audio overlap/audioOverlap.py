from pydub import AudioSegment
from pydub.playback import play

sound1 = AudioSegment.from_file("test1.wav")


sound2 = AudioSegment.from_file("test2.wav")



combined = sound1.overlay(sound2)


combined.export("combined.wav", format='wav')