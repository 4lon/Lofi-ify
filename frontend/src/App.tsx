import React, { useState } from 'react';
import { useEffect } from 'react';
import './App.css';
import AudioVisualiser from './components/AudioVisualiser';
import axios from 'axios'

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
    const url = e.split('?')[1]
    console.log(url)
    axios.get("http://127.0.0.1:5000/api/to_lofi/"+url)
    .then(response => console.log('sent'));

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
