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

import subprocess
import yaml
import os
import time

def main():
    loaded_yaml = os.path.join(os.path.dirname(__file__), "./yamlradio/zenders.yml")
    
    with open(loaded_yaml, "r") as f:
        zenderdict = yaml.load(f)
        afkortingenlijst = [combinatie["afk"] \
        for combinatie in zenderdict]

        for afk in afkortingenlijst:
            cmd = ["rd", afk]
            print("$ " + " ".join(cmd))
            p = subprocess.Popen(cmd)
            time.sleep(3)
            p.kill()
            print("\n")


if __name__ == "__main__":
    main()