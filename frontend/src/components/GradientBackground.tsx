import React from 'react';
import { useEffect } from 'react';
import { Gradient } from '../assets/Gradient.js'

function GradientBackground(){
    useEffect(() => {
        const canvasElement = document.getElementById("gradient-canvas");
        const gradient: any = new Gradient();
        if (canvasElement) {
            gradient.initGradient("#gradient-canvas");
        } else {
            gradient.pause();
        }
    }, []);

    return(
        <canvas id="gradient-canvas" data-transition-in />
    );
}

export default GradientBackground