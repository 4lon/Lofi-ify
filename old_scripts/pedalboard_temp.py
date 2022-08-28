from pydub import AudioSegment
from pydub.playback import play
from pedalboard import Pedalboard, Chorus, Reverb, Bitcrush, Resample, Compressor, HighpassFilter, LowpassFilter, PitchShift
from pedalboard.io import AudioFile
# import bpm

# song = "Taylor Swift - Blank Space"
song = "Bruno Mars - Locked Out Of Heaven"

vocal = '/home/alon/Documents/Lofi-ify/output/'+ song + '/vocals.wav'
bass = '/home/alon/Documents/Lofi-ify/output/'+ song + '/bass.wav'
piano = '/home/alon/Documents/Lofi-ify/output/'+ song + '/piano.wav'
other = '/home/alon/Documents/Lofi-ify/output/'+ song + '/other.wav'
drums = '/home/alon/Documents/Lofi-ify/output/'+ song + '/drums.wav'
drums = 'Vinyl Crackles (11).wav'

def load_music(location):
    with AudioFile(location, 'r') as f:
        return f.read(f.frames), f.samplerate

vocal, samplerate = load_music(vocal)
# bass, samplerate = load_music(bass)
# piano, samplerate = load_music(piano)
# other, samplerate = load_music(other)
drums, samplerate = load_music(drums)

# print(samplerate)


# board = Pedalboard([Resample(16000), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
# effected = board(vocal, samplerate)


# # play(effected)
# with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
#     f.write(effected)


# board = Pedalboard([Compressor(threshold_db=-30, ratio=10), LowpassFilter(), HighpassFilter(), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2), Resample(8000)])
# effected = board(drums, samplerate)

board = Pedalboard([PitchShift(2)])
effected = board(vocal, samplerate)

# play(effected)
with AudioFile('vocal.wav', 'w', samplerate, effected.shape[0]) as f:
    f.write(effected)



# def speed_change(sound, speed=1.0):
#     # Manually override the frame_rate. This tells the computer how many
#     # samples to play per second
#     sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
#          "frame_rate": int(sound.frame_rate * speed)
#       })
#      # convert the sound with altered frame rate to a standard frame rate
#      # so that regular playback programs will work right. They often only
#      # know how to play audio at standard frame rate (like 44.1k)
#     return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# vocal = AudioSegment.from_file('processed-output.wav')

# # play(vocal)

# board = Pedalboard([Resample(16000), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
# effected = board(vocal, samplerate)

# with AudioFile('processed-output.wav', 'w', samplerate, effected.shape[0]) as f:
#     f.write(effected)
