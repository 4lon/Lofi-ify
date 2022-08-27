from pydub import AudioSegment
from pydub.playback import play

def pd_load_music(location):
    return AudioSegment.from_file(location)

track = "Lo-fi Drum beat - 70 BPM.mp4"

drum = pd_load_music(track)
bpm = 70

play(drum)