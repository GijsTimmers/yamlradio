#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  radio.py
#  
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys
import argparse                         ## Parst argumenten
import subprocess

class Radio():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.zenderparser = self.parser.add_mutually_exclusive_group()
        
        self.zenderparser.add_argument("--stubru",
        help="Studio Brussel",\
        action="store_const", dest="zender", const="stubru")
        
        self.zenderparser.add_argument("--538",
        help="Radio 538",\
        action="store_const", dest="zender", const="538")
        
        self.zenderparser.add_argument("--3fm",
        help="3FM",\
        action="store_const", dest="zender", const="3fm")
        
        self.zenderparser.add_argument("--risefm",
        help="RiseFM",\
        action="store_const", dest="zender", const="risefm")
        
    def afspelen(self):
        argumenten = self.parser.parse_args()
        
        zenderlijst = {
        "stubru": "http://mp3.streampower.be/stubru-high.mp3",
        "538"   : "http://82.201.100.9:8000/radio538",
        "3fm"   : "http://icecast.omroep.nl/3fm-bb-mp3",
        "risefm": "http://mastersound.hu/clubfmplay_hq"
        }
        
        url = zenderlijst[argumenten.zender]
        print "Speelt nu af: " + argumenten.zender + ". " + \
        "Druk op Q om te beëindigen."
        
        
        dev_null = open("/dev/null", "w")
        subprocess.call(["mplayer", url], stdout = dev_null, stderr = dev_null)
            
def main():
    rd = Radio()
    rd.afspelen()
    return 0

if __name__ == '__main__':
    main()

