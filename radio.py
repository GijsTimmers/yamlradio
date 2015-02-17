#!/usr/bin/env python2
# -*- coding: utf-8 -*-

## Dependencies:    argparse, mplayer
## Author:          Gijs Timmers: https://github.com/GijsTimmers

## Licence:         CC-BY-SA-4.0
##                  http://creativecommons.org/licenses/by-sa/4.0/

## This work is licensed under the Creative Commons
## Attribution-ShareAlike 4.0 International License. To  view a copy of
## this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or
## send a letter to Creative Commons, PO Box 1866, Mountain View,
## CA 94042, USA.

import sys                      ## Basislib
import argparse                 ## Parst argumenten
import subprocess               ## Om programma's uit te voeren vanuit Python

class Radio():
    def __init__(self):
        ## Parser instantiëren
        self.parser = argparse.ArgumentParser()
        
        ## Zorgen dat geen twee zenders tegelijk kunnen worden ingevoerd
        self.zenderparser = self.parser.add_mutually_exclusive_group()
        
        ## Mogelijke zenders opgeven
        self.zenderparser.add_argument("--stubru",
        help="Studio Brussel",\
        action="store_const", dest="zender", const="stubru")
        
        self.zenderparser.add_argument("--538",
        help="Radio 538",\
        action="store_const", dest="zender", const="538")
        
        self.zenderparser.add_argument("--3fm",
        help="3FM",\
        action="store_const", dest="zender", const="3fm")
        
        self.zenderparser.add_argument("--risefm",
        help="RiseFM",\
        action="store_const", dest="zender", const="risefm")
        
        self.zenderparser.add_argument("--r2nl",
        help="Radio 2 (Nederland)",\
        action="store_const", dest="zender", const="r2nl")
        
        
        
    def zendervinden(self):
        ## De ingevoerde argumenten parsen
        argumenten = self.parser.parse_args()
        
        ## Zenderlijst definiëren; voeg hier extra zenders toe als
        ## een zender:url-dictionary
        
        zenderlijst = {
        "stubru": "http://mp3.streampower.be/stubru-high.mp3",
        "538"   : "http://82.201.100.9:8000/radio538",
        "3fm"   : "http://icecast.omroep.nl/3fm-bb-mp3",
        "risefm": "http://mastersound.hu/clubfmplay_hq",
        "r2nl"  : "http://icecast.omroep.nl/radio2-bb-mp3"
        }
        
        
        ## Indien er geen opties zijn meegegeven, krijgen we een KeyError.
        ## In dat geval printen we de --help-output.
        try:
            url = zenderlijst[argumenten.zender]
            return (argumenten.zender, url)
        except KeyError:
            self.parser.parse_args("--help".split())
        
        
        
    def afspelen(self, zender, url):
        print "Speelt nu af: " + zender + ". " + \
        "Druk op Q om te beëindigen."
        
        ## dev_null als schrijfbestand definiëren om output te verbergen.
        try:
            dev_null = open("/dev/null", "w")
        except IOError:
            print "Kon /dev/null niet bereiken."
            
        ## mplayer starten
        try:
            subprocess.call(["mplayer", url], \
            stdout = dev_null, stderr = dev_null)
        except OSError:
            print "Kon geen mplayer-executable vinden in $PATH."
            
def main():
    rd = Radio()
    (zender, url) = rd.zendervinden()
    rd.afspelen(zender, url)
    return 0

if __name__ == '__main__':
    main()

