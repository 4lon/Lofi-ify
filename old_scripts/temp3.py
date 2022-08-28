from midi2audio import FluidSynth
import os

dir = "output/2"
song = "Bruno Mars - Locked Out Of Heaven" 

os.system(f"basic-pitch {dir} \"copyright/{song}.mp3\" --save-midi")
os.system(f"conda run -n g2g10 python -m groove2groove.models.roll2seq_style_transfer --logdir resources/v01_drums run-midi --softmax-temperature 0.5 --sample {dir}/\"Bruno Mars - Locked Out Of Heaven_basic_pitch.mid\" resources/Lofi_Piece_in_Eb_major_1.mid {dir}/output.mid")
    
# fs = FluidSynth()
# fs.midi_to_audio(f'{dir}/output.mid', f'output.wav')