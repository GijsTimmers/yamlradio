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

import argcomplete              ## Argumenten aanvullen 
import argparse                 ## Parst argumenten
import yaml                     ## Configuratie inlezen
import os                       ## Basislib
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
        
        ## Afkortingenlijsten vullen met afkortingen en evt. namen
        self.afkortingenlijst = [combinatie["afk"] \
        for combinatie in self.zenderdict]
        self.afkortingenennamenlijst = [(combinatie["afk"], combinatie ["naam"]) \
        for combinatie in self.zenderdict]
        
        ## Parser instantiëren en de te verwachten argumenten meegeven
        self.parser = argparse.ArgumentParser(usage=self.helpoutput(), add_help=False)
        self.parser.add_argument('zender', choices=self.afkortingenlijst, help="hulp hier")
        
    def zendervinden(self):
        ## De ingevoerde argumenten parsen
        argcomplete.autocomplete(self.parser)
        argumenten = self.parser.parse_args()
        for combinatie in self.zenderdict:
            if combinatie["afk"] == argumenten.zender:
                naam = combinatie["naam"]
                url  = combinatie["url"]
                
                if re.match("\d", combinatie["afk"][0]):
                    comm = "_" + combinatie["afk"]
                else:
                    comm = combinatie["afk"]
                    
        return (naam, url, comm)    
    
    def helpoutput(self, name=None):
        ## We schrijven een eigen helpoutput, omdat die van argparse hier niet
        ## volstaat. De reden:
        ## We willen dat gebruikers "rd 3fm" kunnen schrijven ipv bvb
        ## "rd --3fm";
        ## De afwezigheid van streepjes impliceert een positioneel argument,
        ## ipv een optioneel argument;
        ## Daarom moeten we werken met één argument, genaamd "zender", welke
        ## meerdere keuzes heeft (de lijst van zenders);
        ## Dat leidt tot een kleine helpoutput, iets als "rd zender {}" met
        ## tussen de accolades alle mogelijke zenderafkortingen.
        SPACING = 2
        
        text = "rd [channel_abbreviation]\n" + \
        "available channels:\n"
        abbreviation_column_width = max([len(afk) for afk in self.afkortingenlijst]) + SPACING
        
        for c in self.afkortingenennamenlijst:
            text += ("  " + \
            c[0] + \
            ((abbreviation_column_width - len(c[0])) * " " ) + \
            c[1] + \
            "\n")
        return text