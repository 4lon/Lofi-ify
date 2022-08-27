import * as React from 'react';
import Stack from '@mui/material/Stack';
import CircularProgress from '@mui/material/CircularProgress';
import { createTheme, ThemeProvider } from '@mui/material/styles';

declare module '@mui/material/styles' {
    interface Theme {
      status: {
        danger: React.CSSProperties['color'];
      };
    }
  
    interface Palette {
      neutral: Palette['primary'];
    }
    interface PaletteOptions {
      neutral: PaletteOptions['primary'];
    }
  
    interface PaletteColor {
      darker?: string;
    }
    interface SimplePaletteColorOptions {
      darker?: string;
    }
    interface ThemeOptions {
      status: {
        danger: React.CSSProperties['color'];
      };
    }
  }
  

const theme = createTheme({
  status: {
    danger: '#ffffff',
  },
  palette: {
    primary: {
      main: '#ffffff',
      darker: '#053e85',
    },
    neutral: {
      main: '#64748B',
      contrastText: '#fff',
    },
  },
});

export default function ProgressBar() {
  return (
    <ThemeProvider theme={theme}>
        <Stack sx={{ color: 'grey.500' }} spacing={2} direction="row">
        {/* <CircularProgress color="primary" size="150px"/> */}
        </Stack>
    </ThemeProvider>
  );
}
