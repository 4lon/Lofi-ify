import * as React from 'react';
import { SearchBar } from './SearchBar';

export interface IAppProps {
    updateSearch: Function;
    updateSongURL: Function;
}

export default function Search (props: IAppProps) {
  return (
    <header className="App-header">
        <h1 className='Heading-1'>lofi.io</h1>
        <SearchBar updateSearch={props.updateSearch} updateSongURL={props.updateSongURL}/>
    </header>
  );
}
