from setuptools import setup, find_packages
setup(
  name = "yamlradio",
  packages = ["yamlradio"],
  version = "1.0",
  description = "A small Python package to play radio stations as defined in a YAML file.",
  author = "Gijs Timmers",
  author_email = "gijs.timmers@student.kuleuven.be",
  url = "https://github.com/GijsTimmers/radio",
  keywords = ["radio", "terminal", "yaml"],
  install_requires = ["argparse", "pyYAML", "py-getch", "cursor"],
  classifiers = [],
  entry_points = {
        'console_scripts': ['rd=yamlradio.yamlradio:main']},
  include_package_data = True
)
