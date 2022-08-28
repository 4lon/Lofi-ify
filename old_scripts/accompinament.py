from pydub import AudioSegment
from pydub.playback import play
from pedalboard import Pedalboard, Chorus, Reverb, Bitcrush, Resample
from pedalboard.io import AudioFile
# import bpm

# song = "Taylor Swift - Blank Space"
song = "Bruno Mars - Locked Out Of Heaven"

vocal = '/home/alon/Documents/Lofi-ify/output/'+ song + '/vocals.wav'
bass = '/home/alon/Documents/Lofi-ify/output/'+ song + '/bass.wav'
piano = '/home/alon/Documents/Lofi-ify/output/'+ song + '/piano.wav'
other = '/home/alon/Documents/Lofi-ify/output/'+ song + '/other.wav'
drums = '/home/alon/Documents/Lofi-ify/output/'+ song + '/drums.wav'

def load_music(location):
    with AudioFile(location, 'r') as f:
        return f.read(f.frames), f.samplerate

vocal, samplerate = load_music(vocal)
bass, samplerate = load_music(bass)
piano, samplerate = load_music(piano)
other, samplerate = load_music(other)

combined = (vocal + bass + piano + other)

with AudioFile('processed-output_comb.wav', 'w', samplerate, combined.shape[0]) as f:
    f.write(combined)


# song = "Taylor Swift - Blank Space"

# vocal = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/vocals.wav')
# bass = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/bass.wav')
# piano = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/piano.wav')
# other = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/other.wav')
# combined = vocal.overlay(bass).overlay(other).overlay(piano)

# combined.export("test2.wav", format="wav")

# predict_and_save(["test2.wav"], output_directory=".", sonify_midi=False, save_model_outputs=False, save_notes=False, save_midi=True)
