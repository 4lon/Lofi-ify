import * as React from 'react';
import { useRef, useState } from 'react';
import { SpectrumVisualizer, SpectrumVisualizerTheme, AudioVisualizerEvents , } from 'react-audio-visualizers';
import record from '../assets/record.png'

const SONG = 'https://demo-react-audio-visualizers.vercel.app/tamsasbeats.mp3'
// const SONG = '../assets/fallen-kingdom.mp3'

export default function AudioVisualiser (props) {
    const [Play, setPlay] = useState(false);
    const ref = useRef(null);   
    const addclass = () => {
        const img = ref.current; // corresponding DOM node
        if (Play === false) {
            setPlay(true);
            img.className = "Playing";
        } else {
            setPlay(false);
            img.className = "Record";
        }
    };


  return (
    <div className='AudioVisualiser' onClick={addclass}>
        <img className="Record" ref={ref} src={record}/>
        <SpectrumVisualizer
            audio={props.songURL}  
            theme={SpectrumVisualizerTheme.radialSquaredBars}
            colors={['#5D2A7B', '#7948A2']}
            iconsColor="#BE8CE5"
            
            showMainActionIcon
            showLoaderIcon
            highFrequency={8000}
        />
    </div>
    );
}
