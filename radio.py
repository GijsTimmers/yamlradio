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
import time
import threading
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
            self.stream = subprocess.Popen(["mplayer", url], \
            stdin=subprocess.PIPE, \
            stdout=subprocess.PIPE, \
            stderr=subprocess.STDOUT, \
            bufsize=1, \
            universal_newlines=True)
            
            ## We encoderen de zendernaam in UTF-8 om errors te voorkomen
            ## in de stringnaam: "België" zou anders een probleem geven.
            print "Speelt nu af: {zender}. " \
                  "Druk op Enter om te beëindigen." \
                  .format(zender=zender.encode("utf-8"))
            
            for regel in iter(self.stream.stdout.readline, ''):
                ## Per nieuwe entry in stdout.readline wordt door deze loop
                ## gegaan. Als bijvoorbeeld de ICY-info verandert, wordt er
                ## opnieuw geprint: ICY Info: ... Dat wordt opgepakt door de if,
                ## en geprint. Zo hebben we iedere keer de meest recente
                ## info te pakken.
                if re.match("^ICY", regel):
                    info = re.findall("(?<=ICY Info: StreamTitle=').*(?=';)", regel)[0]
                    print "Info: [{info}]".format(info=info)
                    pass
                if re.match("^Exiting...", regel):
                    break
            return()
            
        except OSError:
            print "Kon geen mplayer-executable vinden in $PATH."
        
    def stoppen(self):
        ## Stuur de toetsindruk Q naar de stream. mplayer reageert op q
        ## door te stoppen. Bij het stoppen print mplayer "Exiting...". In
        ## de thread t loopt een for-loop, welke deze string opvangt. Als 
        ## reactie stopt de for-loop ('break'), en komen we aan bij het
        ## return()-statenment. De thread is nu beëindigd.
        self.stream.communicate(input="q")
        


def main():
    rd = Radio()
    naam, url = rd.zendervinden()
    t = threading.Thread(target=rd.afspelen, args=(naam, url))
    t.start()
    
    ## Afspelen stoppen na drukken op ENTER mbv raw_input(): het script kan 
    ## pas verder na een invoer bij raw_input() en blijft daardoor afspelen.
    try:
        raw_input()
        rd.stoppen()
        t.join()
    except KeyboardInterrupt:
        print "\nAfsluiten kan ook met Enter."
        
    return 0

if __name__ == '__main__':
    main()