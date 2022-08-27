import React from 'react';
import { useEffect } from 'react';
import './App.css';

import GradientBackground from './components/GradientBackground'
import { SearchBar } from './components/SearchBar';


function App() {

  return (
    <div className="App">
      <GradientBackground/>
      <header className="App-header">
        <SearchBar/>
      </header>
    </div>
  );
}

export default App;
