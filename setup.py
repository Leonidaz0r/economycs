#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="economycs",
    version="0.1",
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        economycs=economycs.main:main
    '''
)
