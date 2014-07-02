#!/usr/bin/env python

from distutils.core import setup

setup(name='LG-TV',
      version='0.1',
      description='Driver for LG TVs (via RS232)',
      author='Alexis Meneses',
      url='https://github.com/alexismeneses/py-lgtv',
      py_modules = ['lgtv'],
      package_dir = {'': 'lib'},
      scripts=['scripts/lgtv']
     )
