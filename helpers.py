from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from pedalboard.io import AudioFile


def determine_bpm(seg):
    
    # seg = seg[int(len(seg)/4):int(len(seg)/2)]

    # reduce loudness of sounds over 120Hz (focus on bass drum, etc)
    seg = seg.low_pass_filter(120.0)

    # we'll call a beat: anything above average loudness
    beat_loudness = seg.dBFS 

    # the fastest tempo we'll allow is 240 bpm (60000ms / 240beats)
    minimum_silence = int(60000 / 240.0)

    nonsilent_times = detect_nonsilent(seg, minimum_silence, beat_loudness)

    spaces_between_beats = []
    last_t = nonsilent_times[0][0]

    for peak_start, _ in nonsilent_times[1:]:
        spaces_between_beats.append(peak_start - last_t)
        last_t = peak_start

    # We'll base our guess on the median space between beats
    spaces_between_beats = sorted(spaces_between_beats)
    space = spaces_between_beats[int(len(spaces_between_beats) / 2)]

    return round(60000 / space)


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


def pb_load_music(location):
    with AudioFile(location, 'r') as f:
        return f.read(f.frames), f.samplerate


def pd_load_music(location):
    return AudioSegment.from_file(location)


def repeat_for_length(song, desired_duration):
    lengthened = song[0]

    while (lengthened.duration_seconds + song.duration_seconds < desired_duration):
        lengthened += song

    lengthened = lengthened[1:]
    lengthened += song[: int(len(song) * (desired_duration - lengthened.duration_seconds) / song.duration_seconds)]
    return lengthened