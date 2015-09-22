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

import importlib

class Fabriek():
    def returnCommunicatorObject(self, comm):
        ## Ontvangt als argument de gewenste communicator als string, en geeft
        ## daarvoor een geïmporteerd communicatorobject terug.
        try:
            co = importlib.import_module(".communicators.%s" % comm, \
            package="yamlradio").Communicator()
        except ImportError:
            co = importlib.import_module(".communicators.default", \
            package="yamlradio").Communicator()
        return co
        
        
