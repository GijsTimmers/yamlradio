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
import sys
import os


class Fabriek():
    def returnCommunicatorObject(self, comm):
        """
        try:
            ## Als er geen bestanden zijn in de configuratiemap, is os.listdir
            ## False en wordt er een AssertionError gegooid. Als de map zelfs 
            ## niet bestaat, wordt er een OSError gegooid omdat os.listdir dan
            ## niet uitgevoerd kan worden.
            assert os.listdir(os.path.join(os.path.expanduser("~"), ".yamlradio", "communicators"))
        except OSError:
            print "Map bestaat niet"
        except AssertionError:
            print "Map is leeg"
        
        #sys.path.append(os.path.join(os.path.expanduser("~"), ".yamlradio", "communicators"))
        sys.path.append(os.path.join(os.path.expanduser("~"), ".yamlradio"))
        co = importlib.import_module("communicators.default2")
        print co
        exit()
        """
        try:
            co = importlib.import_module(".communicators.%s" % comm, \
            package="yamlradio").Communicator()
        except ImportError:
            co = importlib.import_module(".communicators.default", \
            package="yamlradio").Communicator()
        return co
        
        
