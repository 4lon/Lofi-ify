from pydub import AudioSegment
from pydub.playback import play
import helpers

song = "Cymatics - Eternity Drum Loop 9 - 87 BPM.wav"
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

drums = AudioSegment.from_file(song)
sound = speed_change(drums, 144/87)
sound = sound * 40

vocal = AudioSegment.from_file("processed-output.wav")
sound = sound.overlay(vocal)

sound.export("test_combo.wav", format="wav")