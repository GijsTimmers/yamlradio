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
import sys
import subprocess

class Communicator(object):
    def __init__(self):
        self.oude_icy_streamtitle = ""
        self.BREEDTE_TERMINAL = 79
        
        if os.name == "posix":
            self.arrow_up_sign   = "↑"
            self.arrow_down_sign = "↓"
        
        if os.name == "nt":
            self.arrow_up_sign   = "\x18"
            self.arrow_down_sign = "\x19"
        
    def processChannelName(self, zender):
        print("Speelt nu af: [{zender}]".format(zender=zender))
        ## Huidige radiozender weergeven als terminaltitel.
        if os.name == "posix":
            sys.stdout.write("\x1b]2;{zender}\x07".format(zender=zender))
        elif os.name == "nt":
            import ctypes
            ctypes.windll.kernel32.SetConsoleTitleA(zender.encode())
            
    
    def checkIfIcyIsNew(self, regel):
        ## Het oudeInfo/nieuweInfo-mechanisme
        ## is een mechanisme om iedere keer alleen het nieuwste ICY-bericht
        ## in het leesvenster te plaatsen.
        self.nieuweInfo = regel
        if self.nieuweInfo == self.oudeInfo:
            return None
        else:
            self.oudeInfo = self.nieuweInfo
            return self.nieuweInfo
            
    def processIcy(self, icy_streamtitle):
        ## Ontvangen ICY-tekst doorgeven aan checkIfIcyIsNew() om te kijken of
        ## ze nieuw is. Indien ze hetzelfde is, gebeurt er niks.
        
        self.nieuwe_icy_streamtitle = icy_streamtitle
        
        if self.nieuwe_icy_streamtitle:
            if self.nieuwe_icy_streamtitle != self.oude_icy_streamtitle:
                sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
                sys.stdout.write("\r" + "Info:         [{info}]".format(info=self.nieuwe_icy_streamtitle[0:64]))
        else:
            sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
            sys.stdout.write("\r" + "Info:         [Geen informatie beschikbaar]".format(info=self.nieuwe_icy_streamtitle))
    
    def processVolumeUp(self):
        sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
        sys.stdout.write("\r" + "Info:         [Volume {arrow}]".format(arrow = self.arrow_up_sign))
    
    def processVolumeDown(self):
        sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
        sys.stdout.write("\r" + "Info:         [Volume {arrow}]".format(arrow = self.arrow_down_sign))
    
    def restoreTerminalTitle(self):
        ## Terminaltitel opnieuw instellen op "Terminal"
        if os.name == "posix":
            sys.stdout.write("\x1b]2;Terminal\x07")
