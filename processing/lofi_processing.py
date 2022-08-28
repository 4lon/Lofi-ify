import os
from pedalboard.io import AudioFile
from pedalboard import Pedalboard, Chorus, Reverb, Bitcrush, Resample, Compressor, HighpassFilter, LowpassFilter, PitchShift
import processing.helpers as helpers
from midi2audio import FluidSynth


def lofify(dir, song):
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


    ### Find bpm - 1
    drums = helpers.pd_load_music(drums)
    bpm = 1.2 * helpers.determine_bpm(drums) / slow_factor
    ###


    ### Combine for accompinament and make midi - 1
    pb_combined = (pb_vocal + pb_bass + pb_piano + pb_other)

    with AudioFile(f"{dir}/without_drums.wav", 'w', samplerate, pb_combined.shape[0]) as f:
        f.write(pb_combined)

    os.system(f"basic-pitch {dir} \"{dir}/without_drums.wav\" --save-midi")
    ###


    ### Vocal editing - 1
    board = Pedalboard([Chorus(), Resample(16000), PitchShift(3), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
    effected = board(pb_vocal, samplerate)

    with AudioFile(f"{dir}/processed-output-voc.wav", 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

    vocals = helpers.pd_load_music(f"{dir}/processed-output-voc.wav")
    vocals = helpers.speed_change(vocals, slow_factor)
    ###


    ### Other editing - 1
    board = Pedalboard([Resample(6000), PitchShift(3), Reverb(room_size=0.75, wet_level=0.2, dry_level=0.2)])
    effected = board(pb_other, samplerate)

    with AudioFile(f"{dir}/processed-output-oth.wav", 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

    other = helpers.pd_load_music(f"{dir}/processed-output-oth.wav")
    other = helpers.speed_change(other, slow_factor)
    ###


    ### Create crackle track - 1
    crackle_track = "resources/crackle.wav"

    crackle = helpers.pd_load_music(crackle_track)
    crackle = helpers.repeat_for_length(crackle, vocals.duration_seconds)
    crackle += 20
    ###


    ### Load MIDI
    FluidSynth('resources/SampleSynthesis.sf2')
    fs = FluidSynth()
    fs.midi_to_audio('input.mid', 'output.wav')
    idk = helpers.pd_load_music("output.wav")
    idk = helpers.speed_change(idk, vocals.duration_seconds/idk.duration_seconds)
    idk += 20
    ###


    ### Create drum track - 2 (needs bpm)
    drum_track = "resources/Lo-fi Drum beat - 70 BPM.mp4"
    drum_bpm = 70
    target_bpm = bpm * slow_factor
    while target_bpm >= 2 * drum_bpm:
        target_bpm /= 2

    drums = helpers.pd_load_music(drum_track)
    drums = helpers.speed_change(drums, target_bpm/drum_bpm)
    drums = helpers.repeat_for_length(drums, vocals.duration_seconds)
    ###

    # drums.export("drums.wav", "wav")
    # crackle.export("crackle.wav", "wav")
    # vocals.export("vocals.wav", "wav")
    # other.export("vocals.wav", "wav")

    combined = vocals.overlay(crackle).overlay(drums).overlay(other).overlay(idk)
    combined.export(f"{dir}/combined.mp3", "mp3")
    return "combined.mp3"



if __name__ == "main":
    dir = "output/1" # custom directory for each call? maybe necessary to avoid multi user conflicts

    song = "Bruno Mars - Locked Out Of Heaven" # song name, should be replaced with youtube downloaded file title
    lofify(dir, song)
    