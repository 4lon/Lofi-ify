from pydub import AudioSegment
from pydub.playback import play
import helpers

song = "Taylor Swift - Blank Space"
# song = "Viva La Vida"

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

vocal = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/vocals.wav')
bass = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/bass.wav')
piano = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/piano.wav')
other = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/other.wav')
combined = vocal.overlay(bass).overlay(other).overlay(piano)
# drums = AudioSegment.from_file("Cymatics - Eternity Drum Loop 9 - 87 BPM.wav")


combined.export("test2.mp3", format="mp3")

# drums = AudioSegment.from_file('/home/alon/Documents/Lofi-ify/output/'+ song + '/drums.wav')


# bpm = bpm.determine_bpm(drums)

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

# def set_loudness(sound, target_dBFS):
#     loudness_difference = target_dBFS - sound.dBFS
#     return sound.apply_gain(loudness_difference)


# def adjust_channel(sound, noise_factor, target_dBFS, slw_factor):
#     # add noise
#     sound = speed_change(sound, noise_factor)
#     sound = speed_change(sound, 1/noise_factor)

#     # normalize
#     sound = set_loudness(sound, target_dBFS)

#     # slow 
#     sound = `speed_change(sound, slw_factor)`

#     return sound

# overall_spd = 1

# # piano = adjust_channel(piano, 1.0, 1, overall_spd)
# # bass = adjust_channel(bass, 1.0, 1, overall_spd)
# # piano = noise_it(piano, 3.0, overall_spd) - 4
# # other = adjust_channel(other, 2.0, -5, overall_spd)

# # combined = piano.overlay(bass).overlay(other)
# play(other)

# # slow_sound = speed_change(sound, 0.75)

# # combined.export("test.wav", format="wav")