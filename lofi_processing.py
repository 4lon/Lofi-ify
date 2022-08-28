import os
from pedalboard.io import AudioFile
from pedalboard import Pedalboard, Chorus, Reverb, Bitcrush, Resample, Compressor, HighpassFilter, LowpassFilter, PitchShift
import helpers
from midi2audio import FluidSynth


# def lofify(dir, song):
#     # dir = "output/1" # custom directory for each call? maybe necessary to avoid multi user conflicts

#     # song = "Viva La Vida" # song name, should be replaced with youtube downloaded file title
#     slow_factor = 0.9

#     ### Seperate channels and load location strings
#     os.system(f"spleeter separate -p spleeter:5stems -o {dir}/spleeter_output \"copyright/{song}.mp3\"")

#     vocal = f"{dir}/spleeter_output/{song}/vocals.wav"
#     bass = f"{dir}/spleeter_output/{song}/bass.wav"
#     piano = f"{dir}/spleeter_output/{song}/piano.wav"
#     other = f"{dir}/spleeter_output/{song}/other.wav"
#     drums = f"{dir}/spleeter_output/{song}/drums.wav"

#     pb_vocal, samplerate = helpers.pb_load_music(vocal)
#     pb_bass, samplerate = helpers.pb_load_music(bass)
#     pb_piano, samplerate = helpers.pb_load_music(piano)
#     pb_other, samplerate = helpers.pb_load_music(other)
#     # pb_drums, samplerate = helpers.pb_load_music(drums)
#     ###


#     ### Find bpm - 1
#     drums = helpers.pd_load_music(drums)
#     bpm = 1.2 * helpers.determine_bpm(drums) / slow_factor
#     ###


#     ### Combine for accompinament and make midi - 1
#     # pb_combined = (pb_vocal + pb_bass + pb_piano + pb_other)

#     # with AudioFile(f"{dir}/without_drums.wav", 'w', samplerate, pb_combined.shape[0]) as f:
#     #     f.write(pb_combined)

#     os.system(f"rm \"{dir}/{song}_basic_pitch.mid\"")
#     os.system(f"basic-pitch {dir} \"copyright/{song}.mp3\" --save-midi")
#     os.system(f"conda run -n g2g10 python -m groove2groove.models.roll2seq_style_transfer --logdir resources/v01_drums run-midi --softmax-temperature 0.5 --sample \"{dir}/{song}_basic_pitch.mid\" resources/Lofi_Piece_in_Eb_major_1.mid {dir}/output.mid")
#     ###


#     ### Vocal editing - 1
#     board = Pedalboard([Chorus(), Resample(16000), PitchShift(3), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
#     effected = board(pb_vocal, samplerate)

#     with AudioFile(f"{dir}/processed-output-voc.wav", 'w', samplerate, effected.shape[0]) as f:
#         f.write(effected)

#     vocals = helpers.pd_load_music(f"{dir}/processed-output-voc.wav")
#     vocals = helpers.speed_change(vocals, slow_factor)
#     vocals -= 10
#     ###


#     # ### Other editing - 1
#     # board = Pedalboard([Resample(6000), PitchShift(3), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
#     # effected = board(pb_other, samplerate)

#     # with AudioFile(f"{dir}/processed-output-oth.wav", 'w', samplerate, effected.shape[0]) as f:
#     #     f.write(effected)

#     # other = helpers.pd_load_music(f"{dir}/processed-output-oth.wav")
#     # other = helpers.speed_change(other, slow_factor)
#     # ###

#     ### bass editing - 1
#     board = Pedalboard([LowpassFilter(), HighpassFilter(), Compressor(-10, 5), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
#     effected = board(pb_bass, samplerate)

#     with AudioFile(f"{dir}/processed-output-oth.wav", 'w', samplerate, effected.shape[0]) as f:
#         f.write(effected)

#     bass = helpers.pd_load_music(f"{dir}/processed-output-oth.wav")
#     bass = helpers.speed_change(bass, slow_factor)
#     ###


#     ### Create crackle track - 1
#     crackle_track = "resources/crackle.wav"

#     crackle = helpers.pd_load_music(crackle_track)
#     crackle = helpers.repeat_for_length(crackle, vocals.duration_seconds)
#     crackle += 5
#     ###


#     ### Load MIDI
#     fs = FluidSynth()
#     fs.midi_to_audio(f'{dir}/output.mid', f'{dir}/output.wav')
#     idk = helpers.pd_load_music(f"{dir}/output.wav")
#     idk = helpers.speed_change(idk, vocals.duration_seconds/idk.duration_seconds)
#     idk += 10
#     ###


#     ### Create drum track - 2 (needs bpm)
#     drum_track = "resources/Lo-fi Drum beat - 70 BPM.mp4"
#     drum_bpm = 70
#     target_bpm = bpm * slow_factor
#     while target_bpm >= 2 * drum_bpm:
#         target_bpm /= 2

#     drums = helpers.pd_load_music(drum_track)
#     drums = helpers.speed_change(drums, target_bpm/drum_bpm)
#     drums = helpers.repeat_for_length(drums, vocals.duration_seconds)
#     ###

#     drums.export("drums.wav", "wav")
#     # crackle.export("crackle.wav", "wav")
#     vocals.export("vocals.wav", "wav")
#     # other.export("vocals.wav", "wav")

#     combined = vocals.overlay(crackle).overlay(drums).overlay(idk).overlay(bass)
#     combined.export(f"{dir}/combined.wav", "wav")


def proc_drums(drums, slow_factor):
    ### Find bpm - 1
    drums = helpers.pd_load_music(drums)
    bpm = 1.5 * helpers.determine_bpm(drums) / slow_factor
    return bpm
    ###

def make_midi(dir, song):
    os.system(f"rm \"{dir}/{song}_basic_pitch.mid\"")
    os.system(f"basic-pitch {dir} \"copyright/{song}.mp3\" --save-midi")

def make_accomp(dir, song):
    os.system(f"conda run -n g2g10 python -m groove2groove.models.roll2seq_style_transfer --logdir resources/v01_drums run-midi --softmax-temperature 0.5 --sample \"{dir}/{song}_basic_pitch.mid\" resources/Lofi_Piece_in_Eb_major_1.mid {dir}/output.mid")
    
def proc_voc(pb_vocal, samplerate, slow_factor):
    ### Vocal editing - 1
    board = Pedalboard([Chorus(), Resample(16000), PitchShift(3), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
    effected = board(pb_vocal, samplerate)

    with AudioFile(f"{dir}/processed-output-voc.wav", 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

    vocals = helpers.pd_load_music(f"{dir}/processed-output-voc.wav")
    vocals = helpers.speed_change(vocals, slow_factor)
    vocals -= 10

    return vocals
    ###

def make_crackle(duration_seconds):
    ### Create crackle track - 1
    crackle_track = "resources/crackle.wav"

    crackle = helpers.pd_load_music(crackle_track)
    crackle = helpers.repeat_for_length(crackle, duration_seconds)
    crackle += 15

    return crackle
    ###

def gen_midi_audio(dir, duration_seconds):
    ### Load MIDI
    fs = FluidSynth()
    fs.midi_to_audio(f'{dir}/output.mid', f'{dir}/output.wav')
    idk = helpers.pd_load_music(f"{dir}/output.wav")
    idk = helpers.speed_change(idk, duration_seconds/idk.duration_seconds)
    fade_time = int(len(idk) * 0.05)
    idk = idk.fade_in(fade_time).fade_out(fade_time)
    idk += 7

    return idk
    ###

def gen_drums(bpm, slow_factor, duration_seconds):    
    ### Create drum track - 2 (needs bpm)
    drum_track = "resources/Lo-fi Drum beat - 70 BPM.mp4"
    drum_bpm = 70
    target_bpm = bpm * slow_factor
    while target_bpm >= 2 * drum_bpm:
        target_bpm /= 2

    drums = helpers.pd_load_music(drum_track)
    drums = helpers.speed_change(drums, target_bpm/drum_bpm)
    drums = helpers.repeat_for_length(drums, duration_seconds)

    return drums
    ###

def lofify_temp(dir, song):
    # dir = "output/1" # custom directory for each call? maybe necessary to avoid multi user conflicts

    # song = "Viva La Vida" # song name, should be replaced with youtube downloaded file title
    slow_factor = 0.9

    ### Seperate channels and load location strings
    os.system(f"spleeter separate -p spleeter:5stems -o {dir}/spleeter_output \"copyright/{song}.mp3\"")

    vocal = f"{dir}/spleeter_output/{song}/vocals.wav"
    bass = f"{dir}/spleeter_output/{song}/bass.wav"
    piano = f"{dir}/spleeter_output/{song}/piano.wav"
    other = f"{dir}/spleeter_output/{song}/other.wav"
    drums = f"{dir}/spleeter_output/{song}/drums.wav"

    pb_vocal, samplerate = helpers.pb_load_music(vocal)
    pb_bass, samplerate = helpers.pb_load_music(bass)
    pb_piano, samplerate = helpers.pb_load_music(piano)
    pb_other, samplerate = helpers.pb_load_music(other)
    # pb_drums, samplerate = helpers.pb_load_music(drums)
    ###

    bpm = proc_drums(drums, slow_factor)
    make_midi(dir, song)
    make_accomp(dir, song)
    vocals = proc_voc(pb_vocal, samplerate, slow_factor)
    crackle = make_crackle(vocals.duration_seconds)
    idk = gen_midi_audio(dir, vocals.duration_seconds)
    drums = gen_drums(bpm, slow_factor, vocals.duration_seconds)

    combined = vocals.overlay(crackle).overlay(drums).overlay(idk)
    fade_time = int(len(combined) * 0.1)
    combined = combined.fade_in(fade_time).fade_out(fade_time)
    combined.export(f"{dir}/combined.wav", "wav")


    # drums.export("drums.wav", "wav")
    # vocals.export("vocals.wav", "wav")
    # idk.export("idk.wav", "wav")



if __name__ == "__main__":
    dir = "output/15" # custom directory for each call? maybe necessary to avoid multi user conflicts

    song = "Chet Faker - Gold (Official Music Video)" # song name, should be replaced with youtube downloaded file title
    lofify_temp(dir, song)
    