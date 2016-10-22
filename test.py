#!/usr/bin/env python3

import yamlradio
import subprocess
import sys
import yaml
import time
import os

print("Testing is turned off for now.")

"""
def main():
    loaded_yaml = os.path.join(os.path.dirname(__file__), "./yamlradio/zenders.yml")
    
    with open(loaded_yaml, "r") as f:
        zenderdict = yaml.load(f)
        afkortingenlijst = [combinatie["afk"] \
        for combinatie in zenderdict]

        for afk in afkortingenlijst:
            p = subprocess.Popen(["yamlradio", afk])
            time.sleep(2)
            p.terminate()



        


if __name__ == "__main__":
    main()
"""

