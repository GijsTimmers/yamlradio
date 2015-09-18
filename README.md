[![Build Status](https://travis-ci.org/GijsTimmers/radio.svg)](https://travis-ci.org/GijsTimmers/radio)

[![cc-logo](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)


# yamlradio
A small Python script to play various radio stations from a terminal.

## Installation
Dependencies:

- `pip`
- `mplayer`
- `argparse`
- `pyYAML`
- `py-getch`
- `cursor`


You can install pip and mplayer via your package manager:

On Ubuntu:
    
    sudo apt-get install python-pip mplayer

On Arch:
    
    sudo pacman -S python2-pip mplayer
    
The other dependencies will be installed automatically when using `pip`:

    sudo pip install yamlradio

## Usage

    rd <CHANNEL-ABBREVIATION>

e.g.

    rd r2nl
    rd stubru

Music will start playing automatically, press any of the following keys to exit:

- <kbd>Enter</kbd>
- <kbd>q</kbd>
- <kbd>Esc</kbd>
- <kbd>Ctrl</kbd> + <kbd>c</kbd>

## Adding other radio stations
You can replace our fine choices with your own recommendations by creating
a file in your home directory, called `.yamlradio.yml`. Adhere to the syntax
defined in [`zenders.yml`](yamlradio/zenders.yml), otherwise you may run into 
some problems.