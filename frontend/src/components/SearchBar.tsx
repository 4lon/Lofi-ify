import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, FilledInput } from '@mui/material';
import { useState } from 'react';
import { AnyNsRecord } from 'dns';

export interface IAppProps {
    updateSearch: Function;
    updateSongURL: Function;
}

export function SearchBar (props:IAppProps) {
  const [inputText, setInputText] = useState("");
  
  const inputHandler = (e:any) => {
    //convert input text to lower case
    // var lowerCase = e.target.value.toLowerCase();
    setInputText(e.target.value);
  }; 

  const submitHandler = (e:any) =>{
    props.updateSearch(false);
    props.updateSongURL(inputText);
    e.preventDefault();
  }


  return (
    <Box
        component="form"
        onSubmit={submitHandler}
        sx={{
            '& > :not(style)': { m: 1, width: '55ch' },
        }}
        noValidate
        autoComplete="off"
        >
        <TextField id="filled-basic" label="Enter Youtube URL" variant="filled" onChange={inputHandler} />

    </Box> 
  );
}
