#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='prettifyJsonLog',
      version='1.0',
      description='A small python programm to make json log formats human readable',
      url="https://github.com/neumantm/prettifyJsonLog",
      license="MIT",
      author='Tim Neumann',
      author_email='neuamntm@fius.informatik.uni-stuttgart.de',

      packages=find_packages(),
      entry_points = {
          'console_scripts': ['prettifyJsonLog=prettifyJsonLog.prettifyJsonLog:main'],
      }
     )
