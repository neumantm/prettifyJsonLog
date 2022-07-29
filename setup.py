#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='prettifyJsonLog',
      version='1.0',
      description='A small python programm to make json log formats human readable',
      long_description="""
      A small python programm to make json log formats human readable

      It reads log lines from stdin.
      Each line must be one log entry formatted as a JSON object.
      """,
      url="https://github.com/neumantm/prettifyJsonLog",
      license="MIT",
      author='Tim Neumann',
      author_email='neuamntm@fius.informatik.uni-stuttgart.de',

      packages=find_packages(),
      entry_points = {
          'console_scripts': ['prettifyJsonLog=prettifyJsonLog.prettifyJsonLog:main'],
      }
     )
