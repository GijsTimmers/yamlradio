[![Build Status](https://travis-ci.org/GijsTimmers/yamlradio.svg?branch=master)]
(https://travis-ci.org/GijsTimmers/yamlradio)

[![cc-logo](https://licensebuttons.net/l/by-sa/4.0/88x31.png)]
(https://creativecommons.org/licenses/by-sa/4.0/)


# yamlradio
A small Python script to play various radio stations from a terminal.

## Installation
### Installing via `pip` (recommended)

On Ubuntu:
    
    $ sudo apt-get install python-pip mplayer

On Arch:
    
    $ sudo pacman -S python2-pip mplayer
    
After installing `pip`, use it to install `yamlradio`:

    $ sudo pip install yamlradio

You don't need to mind the dependencies as they will be installed automatically.

### Installing via `git clone`

First, install the dependencies:

- `git`
- `pip`
- `mplayer`
- `argparse`
- `argcomplete`
- `pyYAML`
- `py-getch`
- `cursor`

Afterwards, clone `yamlradio`:

    git clone https://github.com/GijsTimmers/yamlradio.git

Now run `yamlradio.py`:

    cd yamlradio/yamlradio
    ./yamlradio.py [channel_abbreviation]

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
    
For this to work, execute the following commands

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
    eval "$(register-python-argcomplete `which rd`)"

Then, source the configuration to apply it:

    source ~/.zshrc

If the command `activate-global-python-argcomplete --user` fails, make sure that
you have `argcomplete` installed. If you install `yamlradio` with `pip`, 
`argcomplete` gets installed automatically.

## Adding custom communicators

If you think the display of ICY information can be improved, you can write
custom communicators for your channel in the directory `communicators/`. 
Make sure the file name is the same as the channel's abbreviation, ending with
`.py`. If the channel's abbreviation starts with a digit, start the filename
with an underscore (`_`). For example:

- the communicator for `stubru` is `stubru.py`
- the communicator for `538` is `_538.py`

There are two methods at your disposal:

- `processChannelName(self, zender)`, which gets called just before playing
the radio station, with `zender` being the channel name. Edit this method to 
change the way the channel name is displayed.
- `processIcy(self, regel)`, which gets called every time the radio station
sends new information via a ICY string, with `regel` being the sent string. Edit
this method to change the way the ICY information is displayed.