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

from .keypress import Environment, Keypress
from .fabriek import Fabriek
from .parser import Parser
from .radio import Radio

import icyparser                ## Parses ICY messages in Icecast streams
import cursor                   ## Cursor tonen/verbergen
import time                     ## Polling voor opvangen keypress
import queue

def main(*afk):
    ## *afk: indien yamlradio wordt aangeroepen
    ## als module ipv als programma.
    
    cursor.hide()
    pa = Parser()                   
    naam, url, comm = pa.zendervinden(*afk)
    
    fa = Fabriek()
    co = fa.returnCommunicatorObject(comm)
    rd = Radio()
    q  = queue.Queue()
    rd.afspelen(url)
    co.processChannelName(naam)
    ## Loop: checks for keypresses and updated ICY info.
    
    kp = Keypress()
    ip = icyparser.IcyParser()
    ip.getIcyInformation(url)
    
    with Environment():    
        while True:
            kp.getKeypress(q)        
            if q.empty():
                co.processIcy(ip.icy_streamtitle)
                #print(rd.stream.stdout.readline())
                time.sleep(0.1)
            else:
                intent = q.get()
                if intent == "stop":
                    break
                elif intent == "volumeUp":
                    co.processVolumeUp()
                    rd.volumeUp()
                    
                elif intent == "volumeDown":
                    co.processVolumeDown()
                    rd.volumeDown()
                    
    ip.stop()
    rd.stoppen()
    co.restoreTerminalTitle()
    print("")
    cursor.show()