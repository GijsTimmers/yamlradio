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

import os                       ## Basislib
import yaml                     ## Configuratie inlezen
import cursor                   ## Cursor tonen/verbergen
import threading                ## Voor multithreading
import subprocess               ## Om programma's uit te voeren vanuit Python
import argparse                 ## Parst argumenten
import getch                    ## Toetsaanslagen opvangen
import time                     ## Polling voor opvangen keypress
import sys                      ## Basislib
import re                       ## Regex

class Parser():
    def __init__(self):
        ## Zenderdictionary aanmaken
        DEFAULT_YAML = os.path.join(os.path.dirname(__file__), "zenders.yml")
        CUSTOM_YAML  = os.path.expanduser("~/.yamlradio.yml")
        
        if os.path.isfile(CUSTOM_YAML):
            ## Load a user-definded yaml file
            loaded_yaml = CUSTOM_YAML
        else:
            ## Load the included yaml file
            loaded_yaml = DEFAULT_YAML
        
        with open(loaded_yaml, "r") as f:
            self.zenderdict = yaml.load(f)
        
        ## Parser instantiëren en de te verwachten argumenten meegeven
        self.parser = argparse.ArgumentParser()
        
        ## Afkortingenlijst vullen met afkortingen
        afkortingenlijst = [combinatie["afk"] for combinatie \
        in self.zenderdict]
        self.parser.add_argument('zender', choices=afkortingenlijst)
        
        
    def zendervinden(self):
        ## De ingevoerde argumenten parsen
        argumenten = self.parser.parse_args()
        
        for combinatie in self.zenderdict:
            if combinatie["afk"] == argumenten.zender:
                naam = combinatie["naam"]
                url  = combinatie["url"]
        return (naam, url)

class Keypress():
    def __init__(self):
        KEY_ENTER  = "\r"
        KEY_Q      = "q"
        KEY_CTRL_C = "\x03"
        KEY_ESC    = "\x1b"
        
        self.EXITKEYS = set([KEY_ENTER, KEY_Q, KEY_CTRL_C, KEY_ESC])
        
    def getexitkeypress(self):
        keypress = getch.getch()
        if keypress in self.EXITKEYS:
            return True
        else:
            return False 

class Radio():
    def __init__(self):
        self.BREEDTE_TERMINAL = 80
        if os.name == "posix":
            self.cmd = "mplayer"
        else:
            self.cmd = "mplayer.exe"

    def afspelen(self, zender, url):
        try:        
            self.stream = subprocess.Popen([self.cmd, url], \
            stdin=subprocess.PIPE, \
            stdout=subprocess.PIPE, \
            stderr=subprocess.STDOUT, \
            bufsize=1, \
            universal_newlines=True)
            
        except OSError:
            print "Kon geen mplayer-executable vinden in $PATH."
            print "Installeer deze eerst:"
            print "Ubuntu:  sudo apt-get install mplayer"
            print "Arch:    sudo pacman -S mplayer"
            print "Windows: http://sourceforge.net/projects/mplayer-win32/"
            sys.exit() ## Moet nog aan gewerkt worden
            
        ## We encoderen de zendernaam in UTF-8 om errors te voorkomen
        ## in de stringnaam: "België" zou anders een probleem geven.
        print "Speelt nu af: [{zender}]"\
              .format(zender=zender.encode("utf-8"))
              
        ## Huidige radiozender weergeven als terminaltitel.
        sys.stdout.write("\x1b]2;{zender}\x07"\
                         .format(zender=zender.encode("utf-8")))
        
        
        for regel in iter(self.stream.stdout.readline, ''):
            ## Per nieuwe entry in stdout.readline wordt door deze loop
            ## gegaan. Als bijvoorbeeld de ICY-info verandert, wordt er
            ## opnieuw geprint: ICY Info: ... Dat wordt opgepakt door de if,
            ## en geprint. Zo hebben we iedere keer de meest recente
            ## info te pakken. Het oudeInfo/nieuweInfo-mechanisme is een
            ## mechanisme om iedere keer alleen het nieuwste ICY-bericht
            ## in het leesvenster te plaatsen.
            
            oudeInfo = ""
            if re.match("^ICY", regel):
                ## Wat uitleg over de regex:
                ## Alles tussen
                ## ICY Info: StreamTitle='
                ## en
                ## ';
                ## wordt opgeslagen als nieuweInfo. .* is non-greedy gemaakt
                ## met een vraagteken, zodat een eventueel volgende streamUrl
                ## niet wordt opgenomen in de nieuweInfo. Uiteindelijk nog een
                ## strip()-statement om losse spaties voorin en achterin de
                ## string weg te nemen.
                nieuweInfo = re.findall(
                "(?<=ICY Info: StreamTitle=').*?(?=';)", regel
                                        )[0].strip()[:64]
                if nieuweInfo != oudeInfo:
                    sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
                    sys.stdout.write("\r" + "Info:         [{info}]".format(info=nieuweInfo))
                    oudeInfo = nieuweInfo
            #else:
                #sys.stdout.write("\rInfo:         [Geen info beschikbaar]")
                #sys.stdout.flush()
                
                    
            if re.match("^Exiting...", regel):
                ## Op een nieuwe regel starten
                sys.stdout.write("\n")
                break
        return()
        
        
        
    def stoppen(self):
        ## Terminaltitel opnieuw instellen op "Terminal"
        sys.stdout.write("\x1b]2;Terminal\x07")
        
        ## Stuur de toetsindruk Q naar de stream. mplayer reageert op q
        ## door te stoppen. Bij het stoppen print mplayer "Exiting...". In
        ## de thread t loopt een for-loop, welke deze string opvangt. Als 
        ## reactie stopt de for-loop ('break'), en komen we aan bij het
        ## return()-statenment. De thread is nu beëindigd.
        try:
            self.stream.communicate(input="q")
        
        ## IOError ontstaat soms door een deadlock in subprocess. Ik weet niet
        ## precies hoe ik die moet oplossen, daarom vang ik hem gewoon op 
        ## zonder er iets mee te doen.
        except IOError:
            sys.stdout.write("\n")

def main():
    pa = Parser()
    naam, url = pa.zendervinden()
    
    cursor.hide()
    
    rd = Radio()
    t = threading.Thread(target=rd.afspelen, args=(naam, url))
    t.start()
    
    ## Afspelen stoppen na drukken op één van de EXITKEYS
    kp = Keypress()
    while kp.getexitkeypress() == False:
        time.sleep(0.2)
    
    cursor.show()
    rd.stoppen()
        
    return 0

if __name__ == '__main__':
    main()