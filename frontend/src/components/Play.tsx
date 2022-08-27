import * as React from 'react';
import AudioVisualiser from './AudioVisualiser';

export interface IAppProps {
  updateSearch: Function;
  songURL: string;
}

export default function Play (props: IAppProps) {
  const backHandler = (e:any) =>{
    props.updateSearch(true );
  }

  return (
    <React.Fragment>
        <h1 className='App-Title'>lofi.io</h1>
        <h1 className='Back-Title' onClick={backHandler}>new remix</h1>
        <header className="Play-header"> 
          <AudioVisualiser songURL={props.songURL}/>
        </header>
        <footer className="Play-footer">
          {/* <h1 className='Song-Title-Start'>playing: wildest dreams</h1> */}
          <h1 className='Song-Title-End'>wildest dreams - taylor swift</h1>
        </footer>
    </React.Fragment>
  );
}
