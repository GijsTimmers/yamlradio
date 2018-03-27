#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

## Dependencies:    mplayer, argparse, argcomplete, pyYAML
## Author:          Gijs Timmers: https://github.com/GijsTimmers

## Licence:         CC-BY-SA-4.0
##                  http://creativecommons.org/licenses/by-sa/4.0/

## This work is licensed under the Creative Commons
## Attribution-ShareAlike 4.0 International License. To  view a copy of
## this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or
## send a letter to Creative Commons, PO Box 1866, Mountain View,
## CA 94042, USA.

## This class controls music playback and nothing else.

import subprocess               ## Om programma's uit te voeren vanuit Python
import os                       ## Basislib
import tempfile                 ## Voor tijdelijke mappen / bestanden

class Radio(object):
    def __init__(self):
        self.cmd = ["mpv", "--no-terminal", "--no-ytdl"]

    def afspelen(self, url):
        dev_null = open(os.devnull, "w")

        self.tempdirpath = tempfile.mkdtemp(prefix="yamlradio_", dir="/tmp")
        self.fifopath = os.path.join(self.tempdirpath, "fifo")
        os.mkfifo(self.fifopath)

        self.cmd.append("--input-file={}".format(self.fifopath))
        self.cmd.append(url)
        
        try:        
            self.stream = subprocess.Popen(self.cmd)

        except OSError:
            print("Kon geen mpv-executable vinden in $PATH.")
            print("Installeer deze eerst:")
            print("Ubuntu:  sudo apt-get install mpv")
            print("Arch:    sudo pacman -S mpv")

    def stoppen(self):
        self.fifo = open(self.fifopath, "w")
        self.fifo.write("quit\n")
        self.fifo.close()
        os.remove(self.fifopath)
        os.rmdir(self.tempdirpath)
