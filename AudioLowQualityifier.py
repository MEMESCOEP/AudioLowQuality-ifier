# Imports
from pydub import AudioSegment

# Variables
inf = input("Input file >> ")
otf = input("Output file >> ")
bitrate = "4k"
framerate = 8000
channels = 1

# DO STUFF AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
sound = AudioSegment.from_file(inf)
sound = sound + 10
new_sound = sound.set_frame_rate(framerate).set_channels(channels)
new_sound.export(otf, format="mp3", bitrate=bitrate)
