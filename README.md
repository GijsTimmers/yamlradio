[![PyPI version](https://badge.fury.io/py/yamlradio.svg)]
(http://badge.fury.io/py/yamlradio)

[![Build Status](https://travis-ci.org/GijsTimmers/yamlradio.svg?branch=master)]
(https://travis-ci.org/GijsTimmers/yamlradio)

[![Code Health](https://landscape.io/github/GijsTimmers/yamlradio/master/landscape.svg?style=flat)]
(https://landscape.io/github/GijsTimmers/yamlradio/master)

# yamlradio
A small Python script to play various radio stations from a terminal.

## Installation
### Installing via `pip` (recommended)

On Ubuntu:

    $ sudo apt-get install python3-pip mplayer2

On Arch:

    $ sudo pacman -S python-pip mplayer

After installing `pip`, use it to install `yamlradio`:

    $ sudo pip3 install yamlradio

You don't need to mind the dependencies as they will be installed automatically.


## Usage

    $ yamlradio <CHANNEL-ABBREVIATION>

e.g.

    $ yamlradio r2nl
    $ yamlradio stubru

Music will start playing automatically, press any of the following keys to exit:

- <kbd>q</kbd>
- <kbd>Esc</kbd>
- <kbd>Enter</kbd>
- <kbd>Space</kbd>

## Requesting radio stations
You can request for a radio station to be added to `yamlradio`. Open an issue 
by [clicking this url](https://github.com/GijsTimmers/yamlradio/issues/new?title=Radio+Station+request+for+___RADIO_STATION___).
Please limit your requests to one station per issue.

## Adding other radio stations yourself

You can replace our fine choices with your own recommendations by creating
a file in your home directory, called `.yamlradio.yml`. Adhere to the syntax
defined in [`zenders.yml`](yamlradio/zenders.yml), otherwise you may run into 
some problems.

## Advanced usage

I try to provide tech-savvy users with the right tools to customise `yamlradio`
to their likings. Some things you can do:

- [Install with `git` instead of `pip`](https://github.com/GijsTimmers/yamlradio/wiki/Installing-via-git)
- [Change the way data is shown for radio stations](https://github.com/GijsTimmers/yamlradio/wiki/Adding-custom-communicators)
- [Autocomplete radio stations in `zsh`](https://github.com/GijsTimmers/yamlradio/wiki/Autocompleting-radio-stations-in-zsh)
