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

import os                       ## Basislib
import sys                      ## Basislib
import yaml                     ## Configuratie inlezen
import argparse                 ## Parst argumenten
import argcomplete              ## Argumenten aanvullen met Tab
import subprocess               ## Om programma's uit te voeren vanuit Python

class Radio():
    def __init__(self):
        ## Zenderdictionary aanmaken
        with open(os.path.join(os.path.dirname(__file__), 
        "zenders.yaml"), "r") as f:
            self.zenderdict = yaml.load(f)
        
        ## Parser instantiëren
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('zender', choices=self.zenderdict.keys())
        
                
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
            naam = self.zenderdict[argumenten.zender]["naam"]
            url  = self.zenderdict[argumenten.zender]["url"]
            return (naam, url)
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
    (naam, url) = rd.zendervinden()
    rd.afspelen(naam, url)
    return 0

if __name__ == '__main__':
    main()

