#!/usr/bin/env python2
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

import getch                    ## Toetsaanslagen opvangen

class Keypress():
    def __init__(self):
        KEY_ENTER  = "\r"
        KEY_Q      = "q"
        KEY_CTRL_C = "\x03"
        KEY_ESC    = "\x1b"
        
        self.EXITKEYS = set([KEY_ENTER, KEY_Q, KEY_CTRL_C, KEY_ESC])
        
    def getexitkeypress(self):
        keypress = getch.getch()
        if keypress in self.EXITKEYS:
            return True
        else:
            return False 
