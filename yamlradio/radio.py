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
import subprocess               ## Om programma's uit te voeren vanuit Python


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
