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

import re                       ## Regex
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
        "zenders.yml"), "r") as f:
            self.zenderdict = yaml.load(f)
        
        ## Parser instantiëren
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('zender', choices=self.zenderdict.keys())
        
                
        ## Argumenten automatisch aanvullen met TAB.
        argcomplete.autocomplete(self.parser)
        
    def zendervinden(self):
        ## De ingevoerde argumenten parsen
        argumenten = self.parser.parse_args()
        
        naam = self.zenderdict[argumenten.zender]["naam"]
        url  = self.zenderdict[argumenten.zender]["url"]
        return (naam, url)

    def afspelen(self, zender, url):
        try:
            ## dev_null als schrijfbestand definiëren om output te verbergen.
            with open(os.devnull, "w") as dev_null:
                self.stream = subprocess.Popen(["mplayer", url], \
                stdout = dev_null, stderr = dev_null)
                
                ## We encoderen de zendernaam in UTF-8 om errors te voorkomen
                ## in de stringnaam: "België" zou anders een probleem geven.
                print "Speelt nu af: {zender}. " \
                      "Druk op Enter om te beëindigen." \
                      .format(zender=zender.encode("utf-8"))
                      
        except IOError:
            print "Kon /dev/null niet bereiken."
        except OSError:
            print "Kon geen mplayer-executable vinden in $PATH."
    
    def stoppen(self):
        self.stream.kill()


def main():
    rd = Radio()
    naam, url = rd.zendervinden()
    rd.afspelen(naam, url)
    ## Afspelen stoppen na drukken op ENTER mbv raw_input(): het script kan 
    ## pas verder na een invoer bij raw_input() en blijft daardoor afspelen.
    raw_input()
    rd.stoppen()
    return 0

if __name__ == '__main__':
    main()