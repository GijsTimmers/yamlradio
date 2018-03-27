#!/usr/bin/env python3

import yamlradio
import http
import urllib
import sys
import yaml
import time
import os

def main():
    print("Testen of alle URL's nog online zijn.")
    print("200 = online.")

    loaded_yaml = os.path.join(os.path.dirname(__file__), "./yamlradio/zenders.yml")
    
    with open(loaded_yaml, "r") as f:
        zenderdict = yaml.load(f)
        urllijst = [combinatie["url"] \
        for combinatie in zenderdict]

        for url in urllijst:
            try:
                print("{}: {}".format(url,urllib.request.urlopen(url).getcode()))
            except urllib.error.HTTPError:
                print("{} offline!".format(url))
                sys.exit(1)
            except http.client.BadStatusLine:
                print("{} badstatusline!".format(url))
                sys.exit(1)
            except (TimeoutError, urllib.error.URLError):
                print("{} timeout!".format(url))
                sys.exit(1)

if __name__ == "__main__":
    main()

