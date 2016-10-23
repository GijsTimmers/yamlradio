#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys
import os


def check_requirements():
    assert sys.version_info >= (3, 4), "Please use Python 3.4 or higher."
    if os.name == "posix":
        assert os.geteuid() == 0, "Please run with root privileges."

try:
    check_requirements()
    setup(
    name = "yamlradio",
    packages = ["yamlradio"],
    version = "2.2.1",
    description = "A small Python3 package to play radio stations as defined in a YAML file.",
    author = "Gijs Timmers",
    author_email = "gijs.timmers@student.kuleuven.be",
    url = "https://github.com/GijsTimmers/yamlradio",
    keywords = ["radio", "terminal", "yaml"],
    install_requires = ["argparse", "argcomplete", "pyYAML", "cursor", "icyparser"],
    classifiers = [],
    entry_points = {
          "console_scripts": ["yamlradio=yamlradio:yamlradio"]},
    include_package_data = True
    )
except AssertionError as e:
    print(e)
