[![Build Status](https://travis-ci.org/GijsTimmers/radio.svg)](https://travis-ci.org/GijsTimmers/radio)

[![cc-logo](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)


# radio
A small Python script to play various radio stations from a terminal.

## Installation

Dependencies:

- `pip`
- `mplayer`
- `argparse`
- `pyYAML`
- `py-getch`


You can install pip and mplayer via your package manager:

On Ubuntu:
    
    sudo apt-get install python-pip mplayer

On Arch:
    
    sudo pacman -S python2-pip mplayer
    
You can install the other dependencies via `pip`:

    sudo pip install argparse pyYAML py-getch

## Usage

    ./radio <CHANNEL-ABBREVIATION>

e.g.

    ./radio r2nl
    ./radio stubru

Music will start playing automatically, press any of the following keys to exit:

- <kbd>Enter</kbd>
- <kbd>q</kbd>
- <kbd>Esc</kbd>
- <kbd>Ctrl</kbd> + <kbd>c</kbd>

## Adding other radio stations
There's a YAML file in this repository, called `zenders.yml`. You can edit
this file to add other radio stations.
