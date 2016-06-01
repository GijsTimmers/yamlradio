#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys

try:
    assert sys.version_info >= (3, 4)
    setup(
    name = "yamlradio",
    packages = ["yamlradio"],
    version = "2.1.2",
    description = "A small Python3 package to play radio stations as defined in a YAML file.",
    author = "Gijs Timmers",
    author_email = "gijs.timmers@student.kuleuven.be",
    url = "https://github.com/GijsTimmers/yamlradio",
    keywords = ["radio", "terminal", "yaml"],
    install_requires = ["argparse", "argcomplete", "pyYAML", "cursor"],
    classifiers = [],
    entry_points = {
          'console_scripts': ['rd=yamlradio:rd']},
    include_package_data = True
    )
except AssertionError:
    print("Please use Python 3.4 or higher.")
