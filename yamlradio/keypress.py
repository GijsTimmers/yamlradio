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

import tty                      ## Necessary stuff for logging keypresses
import sys                      ## Necessary stuff for logging keypresses
import select                   ## Necessary stuff for logging keypresses
import termios                  ## Necessary stuff for logging keypresses

class Keypress(object):
    def __enter__(self):
        ## doing some 'scary' terminal stuff so that stdin is non-blocking
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        return self

    def __exit__(self, type, value, traceback):
        ## restoring the terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
        
    def __init__(self):
        ## defining keys we'll react on
        KEY_LOWER_Q  = "q"
        KEY_UPPER_Q  = "Q"
        KEY_ENTER    = "\n"
        KEY_SPACE    = " "
        KEY_ESC      = "\x1b"
        
        KEY_0        = "0"
        KEY_PLUS     = "+"
        KEY_EQUALS   = "="
        
        KEY_9        = "9"
        KEY_MINUS    = "-"
        
        self.EXITKEYS = set([
                             KEY_LOWER_Q,
                             KEY_UPPER_Q,
                             KEY_ENTER, 
                             KEY_SPACE,
                             KEY_ESC
                             ])
        
        self.VOLUMEUPKEYS = set([
                                 KEY_0,
                                 KEY_PLUS,
                                 KEY_EQUALS
                                 ])
        
        self.VOLUMEDOWNKEYS = set([
                                 KEY_9,
                                 KEY_MINUS
                                 ])


    def getKeypress(self, q):
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            keypress = sys.stdin.read(1)
            if keypress in self.EXITKEYS:
                q.put("stop")
            if keypress in self.VOLUMEUPKEYS:
                q.put("volumeUp")
            if keypress in self.VOLUMEDOWNKEYS:
                q.put("volumeDown")
            else:
                pass
        return False