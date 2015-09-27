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

from .keypress import Keypress
from .fabriek import Fabriek
from .parser import Parser
from .radio import Radio

import threading                ## Voor multithreading
import cursor                   ## Cursor tonen/verbergen
import time                     ## Polling voor opvangen keypress
import re                       ## Regex

def main():
    pa = Parser()
    naam, url, comm = pa.zendervinden()
    #print naam, url, comm
    cursor.hide()
    
    fa = Fabriek()
    co = fa.returnCommunicatorObject(comm)
        
    rd = Radio()
    t = threading.Thread(target=rd.afspelen, args=(naam, url, co))
    t.start()
    
    ## Afspelen stoppen na drukken op één van de EXITKEYS
    kp = Keypress()
    while kp.getexitkeypress() == False:
        time.sleep(0.2)
    
    cursor.show()
    rd.stoppen()
    
    return 0