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

import os
   
class UnixEnvironment(object):
    def __enter__(self):
        ## doing some 'scary' terminal stuff so that stdin is non-blocking
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        return self

    def __exit__(self, type, value, traceback):
        ## restoring the terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

class UnixKeypress(object):
    def __init__(self):
        ## defining keys we'll react on
        KEY_LOWER_Q  = "q"
        KEY_UPPER_Q  = "Q"
        KEY_ENTER    = "\n"
        KEY_SPACE    = " "
        KEY_ESC      = "\x1b"
        
        BYTE_LOWER_Q  = b"q"
        BYTE_UPPER_Q  = b"Q"
        BYTE_ENTER    = b"\n"
        BYTE_SPACE    = b" "
        BYTE_ESC      = b"\x1b"
             
        KEY_0        = "0"
        KEY_PLUS     = "+"
        KEY_EQUALS   = "="
        
        BYTE_0        = b"0"
        BYTE_PLUS     = b"+"
        BYTE_EQUALS   = b"="
        
        KEY_9        = "9"
        KEY_MINUS    = "-"
        
        BYTE_9        = b"9"
        BYTE_MINUS    = b"-"
        
        self.EXITKEYS = set([
                             KEY_LOWER_Q,
                             KEY_UPPER_Q,
                             KEY_ENTER, 
                             KEY_SPACE,
                             KEY_ESC,
                             BYTE_LOWER_Q,
                             BYTE_UPPER_Q,
                             BYTE_ENTER, 
                             BYTE_SPACE,
                             BYTE_ESC
                             ])
        
        self.VOLUMEUPKEYS = set([
                                 KEY_0,
                                 KEY_PLUS,
                                 KEY_EQUALS,
                                 BYTE_0,
                                 BYTE_PLUS,
                                 BYTE_EQUALS
                                 ])
        
        self.VOLUMEDOWNKEYS = set([
                                 KEY_9,
                                 KEY_MINUS,
                                 BYTE_9,
                                 BYTE_MINUS
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

class WindowsEnvironment(object):
    def __enter__(self):
        #print("enter...")
        pass
    def __exit__(self, type, value, traceback):
        #print("exit...")
        pass

class WindowsKeypress(UnixKeypress):
    def __init__(self):
        super().__init__()
        #print(self.EXITKEYS)
        #self.EXITKEYS = super().EXITKEYS
        
    def getKeypress(self, q):
        if msvcrt.kbhit():
            keypress = msvcrt.getch()
            #print(keypress)
            if keypress in self.EXITKEYS:
                q.put("stop")
            if keypress in self.VOLUMEUPKEYS:
                q.put("volumeUp")
            if keypress in self.VOLUMEDOWNKEYS:
                q.put("volumeDown")
            else:
                pass


if os.name == "posix":
    import tty                      ## Necessary stuff for logging keypresses
    import sys                      ## Necessary stuff for logging keypresses
    import select                   ## Necessary stuff for logging keypresses
    import termios                  ## Necessary stuff for logging keypresses
    Environment = UnixEnvironment
    Keypress = UnixKeypress

elif os.name == "nt":
    import os
    import msvcrt
    Environment = WindowsEnvironment
    Keypress = WindowsKeypress
