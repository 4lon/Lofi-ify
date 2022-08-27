from midi2audio import FluidSynth

# using the default sound font in 44100 Hz sample rate
FluidSynth('resources/SampleSynthesis.sf2')
fs = FluidSynth()
fs.midi_to_audio('input.mid', 'output.wav')


