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
    
    $ sudo apt-get install python-pip mplayer

On Arch:
    
    $ sudo pacman -S python2-pip mplayer
    
The other dependencies will be installed automatically when using `pip`:

    $ sudo pip install yamlradio

## Usage

    $ rd <CHANNEL-ABBREVIATION>

e.g.

    $ rd r2nl
    $ rd stubru

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

## Autocompleting radio stations in `zsh`
`yamlradio` is made so that channels can be autocompleted in `zsh`. This feature
may come in handy:

    $ rd st      ## Now press the TAB key
    $ rd stubru  ## Result
    
For this to work, execute the following commands:

    $ activate-global-python-argcomplete --user
    
Now, add the following lines at the end of your `~/.zshrc`:

    ## Setting up argcomplete
    ## Remember to execute
    ## activate-global-python-argcomplete --user
    ## first!

    autoload bashcompinit
    bashcompinit
    source ~/.bash_completion.d/python-argcomplete.sh

    ## now name the to be completed scripts
    eval "$(register-python-argcomplete /usr/local/bin/rd)"

If the command `activate-global-python-argcomplete --user` fails, make sure that
you have `argcomplete` installed. If you install `yamlradio` with `pip`, 
`argcomplete` gets installed automatically.