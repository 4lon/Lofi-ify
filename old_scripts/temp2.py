from midi2audio import FluidSynth

fs = FluidSynth("SampleSynthesis.sf2")
fs.play_midi("input.mid")