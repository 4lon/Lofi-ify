import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { createTheme, FilledInput } from '@mui/material';

export interface IAppProps {
}

export function SearchBar (props: IAppProps) {
  return (
    <Box
        component="form"
        sx={{
            '& > :not(style)': { m: 1, width: '55ch' },
        }}
        noValidate
        autoComplete="off"
        >
        <TextField id="filled-basic" label="Enter Youtube URL" variant="filled" />

    </Box> 
  );
}
