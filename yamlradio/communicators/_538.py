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

from . import default           ## Superklasse
import sys                      ## Basislib

class Communicator(default.Communicator):
    def processIcy(self, icy_streamtitle):
        ## Ontvangen ICY-tekst doorgeven aan checkIfIcyIsNew() om te kijken of
        ## ze nieuw is. Indien ze hetzelfde is, gebeurt er niks.
    
        self.nieuwe_icy_streamtitle = icy_streamtitle
        
        if self.nieuwe_icy_streamtitle:
            if " - " in self.nieuwe_icy_streamtitle:
                self.nieuwe_icy_streamtitle = self.nieuwe_icy_streamtitle.title()
            if self.nieuwe_icy_streamtitle != self.oude_icy_streamtitle:
                sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
                sys.stdout.write("\r" + "Info:         [{info}]".format(info=self.nieuwe_icy_streamtitle[0:64]))
        else:
            sys.stdout.write("\r" + " " * self.BREEDTE_TERMINAL)
            sys.stdout.write("\r" + "Info:         [Geen informatie beschikbaar]".format(info=self.nieuwe_icy_streamtitle))
    