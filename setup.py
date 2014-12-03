#!/usr/bin/env python

# Donut Detector: setup.py
#
# Copyright (C) 2014 Brian Jing
# Author: Brian Jing
# For license information, see LICENSE.txt


from distutils.core import setup

setup(name='donut_detector',
    version='0.1',
    description='Donut detector that frees you from buying donuts again!',
    author='Brian Jing',
    author_email='brian.jing@au.experian.com',
    url='gaydonut.net',
    packages = ['donut_detector'],
    data_files = [('/etc/init.d', ['donut_detector.conf']),
                  ('/usr/local/bin', ['donut_detector/donut_detector.py'])],
    install_requires=['evdev'],
)