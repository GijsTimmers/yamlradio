#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

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
import yaml
import argparse                 ## Parst argumenten
import argcomplete              ## Argumenten aanvullen met Tab
import subprocess               ## Om programma's uit te voeren vanuit Python

class Radio():
    def __init__(self):
        
        ## Zenderdictionary aanmaken
        with open("zenders.yaml", "r") as f:
            self.zenderdict = yaml.load(f)
        
        ## Parser instantiëren
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('zender', choices=self.zenderdict.keys())
        
        
        """
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
        """
        
        ## Argumenten automatisch aanvullen met TAB.
        argcomplete.autocomplete(self.parser)
        
    def zendervinden(self):
        ## De ingevoerde argumenten parsen
        argumenten = self.parser.parse_args()
        #print argumenten.zender
        #print self.zenderdict[argumenten.zender]
        
        ## Indien er geen opties zijn meegegeven, krijgen we een KeyError.
        ## In dat geval printen we de --help-output.
        try:
            url = self.zenderdict[argumenten.zender]
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

