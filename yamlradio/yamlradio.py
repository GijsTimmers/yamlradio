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

import threading                ## Voor multithreading
import cursor                   ## Cursor tonen/verbergen
import time                     ## Polling voor opvangen keypress

import queue

def main():
    pa = Parser()
    naam, url, comm = pa.zendervinden()
    
    cursor.hide()
    
    fa = Fabriek()
    co = fa.returnCommunicatorObject(comm)
    
    rd = Radio()
    q  = queue.Queue()
    t1 = threading.Thread(target=rd.afspelen, args=(naam, url, co, q))
    t1.start()
    
    with Environment():
        kp = Keypress()
        while t1.isAlive():
            kp.getKeypress(q)
            
            if q.empty():
                time.sleep(0.1)
            else:
                intent = q.get()
                if intent == "stop":
                    q.task_done()
                    cursor.show()
                    rd.stoppen()
                elif intent == "volumeUp":
                    rd.volumeUp()
                elif intent == "volumeDown":
                    rd.volumeDown()
    return 0