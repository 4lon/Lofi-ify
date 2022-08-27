import React, { useState } from 'react';
import { useEffect } from 'react';
import './App.css';
import AudioVisualiser from './components/AudioVisualiser';

import GradientBackground from './components/GradientBackground'
import ProgressBar from './components/ProgressBar';
import Search from './components/Search';
import Play from './components/Play'


function App() {
  const [isSearch, setSearch] = useState(true);
  const [songURL, setSongURL] = useState('');

  const updateSearch = (e:boolean) => {
    setSearch(e)
  }
  const updateSongURL = (e:string) => {
    setSongURL(e)
  }

  return (
    <div className="App">
      <GradientBackground/>
      {isSearch ?  <Search updateSearch={updateSearch} updateSongURL={updateSongURL}/> : <Play updateSearch={updateSearch} songURL={songURL}/>}
    </div>
  );
}

export default App;
