#!/usr/bin/env python

# Donut Detector: setup.py
#
# Copyright (C) 2014 Brian Jing
# Author: Brian Jing
# For license information, see LICENSE


from setuptools import setup, find_packages

setup(name='donut_detector',
    version='0.1',
    description='Donut frees you from buying donuts again!',
    author='Brian Jing',
    author_email='supanovafreak@gmail.com',
    url='gaydonut.net',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['evdev'],
    data_files = [('/etc/init', ['src/donut-detector.conf']),
                  ('/usr/local/bin', ['src/donut_detector/donut_detector.py'])],
)
