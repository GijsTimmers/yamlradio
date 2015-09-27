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

import default                  ## Superklasse
import sys                      ## Basislib
import re                       ## Regex

class Communicator(default.Communicator):
    def processIcy(self, regel):
        ## Het oudeInfo/nieuweInfo-mechanisme
        ## is een mechanisme om iedere keer alleen het nieuwste ICY-bericht
        ## in het leesvenster te plaatsen.
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
        
        self.nieuweInfo = regel
        if self.nieuweInfo != self.oudeInfo:
            if " - " in self.nieuweInfo:
                ## Als er een liedje wordt afgespeeld (gekenmerkt door het
                ## streepje), wordt de string omgezet in kleine letters, be-
                ## ginnend met een hoofdletter.
                self.nieuweInfo = self.nieuweInfo.title()
            
            sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
            sys.stdout.write("\r" + "Info:         [{info}]".format(info=self.nieuweInfo))
            self.oudeInfo = self.nieuweInfo