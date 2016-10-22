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

class Radio(object):
    def __init__(self):
        if os.name == "posix":
            self.cmd = "mplayer"
        else:
            self.cmd = "mplayer.exe"

    def afspelen(self, url):
        dev_null = open(os.devnull, "w")
        
        try:        
            self.stream = subprocess.Popen([self.cmd, url], \
            stdin=subprocess.PIPE, \
            stdout=dev_null, \
            stderr=dev_null, \
            bufsize=1)
        except OSError:
            print("Kon geen mplayer-executable vinden in $PATH.")
            print("Installeer deze eerst:")
            print("Ubuntu:  sudo apt-get install mplayer2")
            print("Arch:    sudo pacman -S mplayer")
            print("Windows: http://sourceforge.net/projects/mplayer-win32/")

    def volumeUp(self):
        self.stream.stdin.write(b"0")
        self.stream.stdin.flush()
        
    def volumeDown(self):
        self.stream.stdin.write(b"9")
        self.stream.stdin.flush()
        
    def stoppen(self):
        ## Stuur de toetsindruk Q naar de stream. mplayer reageert op q
        ## door te stoppen.
        self.stream.stdin.write(b"q")
        self.stream.stdin.flush()
        
        
