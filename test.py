#!/usr/bin/env python3

import yaml
import os
import queue
import time
import threading

import yamlradio.fabriek
import yamlradio.yamlradio
import yamlradio.keypress
import yamlradio.parser
import yamlradio.radio

def main():
    pa = yamlradio.parser.Parser()
    rd = yamlradio.radio.Radio()
    fa = yamlradio.fabriek.Fabriek()

    loaded_yaml = os.path.join(os.path.dirname(__file__), "./yamlradio/zenders.yml")
    
    with open(loaded_yaml, "r") as f:
        zenderdict = yaml.load(f)
        afkortingenlijst = [combinatie["afk"] \
        for combinatie in zenderdict]

        for afk in afkortingenlijst:
            naam, url, comm = pa.zendervinden(afk)
            #print(naam, url, comm)
            co = fa.returnCommunicatorObject(comm)
            q = queue.Queue()
            t1 = threading.Thread(target=rd.afspelen, args=(naam, url, co, q))
            t1.start()
            time.sleep(3)
            rd.stoppen()
            print("\n")

        


if __name__ == "__main__":
    main()


