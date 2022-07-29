#!/usr/bin/env python

import os
from setuptools import setup, find_packages


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(name='prettifyJsonLog',
      version='1.0',
      description='A small python programm to make json log formats human readable',
      long_description=README,
      url="https://github.com/neumantm/prettifyJsonLog",
      license="MIT",
      author='Tim Neumann',
      author_email='neuamntm@fius.informatik.uni-stuttgart.de',

      include_package_data=True,
      packages=find_packages(),
      entry_points = {
          'console_scripts': ['prettifyJsonLog=prettifyJsonLog.prettifyJsonLog:main'],
      }
     )
