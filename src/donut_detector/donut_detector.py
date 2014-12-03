#!/usr/bin/env python

# Donut Detector: main script
#
# Copyright (C) 2014 Brian Jing
# Author: Brian Jing
# For license information, see LICENSE


from subprocess import Popen
from evdev import InputDevice, categorize, ecodes

from find_input import find_keyboard_devs
import util

class Donut_Detector(object):
    """ This an attempt to avoid being donuted at work, which would suck so bad
    """
    _cache = '' # This is used to record keystrokes
    _devices = None # Input devices
    _locked = False
    _log_file = '/var/log/donut_detector.log'

    def __init__(self):
        self._logger = util.get_logger(__name__, log_file=self._log_file)
        self._init_devices()

    def _init_devices(self):
        # Initialise keyboard devices
        keyboards = find_keyboard_devs()

        self._devices = [InputDevice(fn.dev_path()) for fn in keyboards]

    def detect_donut(self, key):
        if key == 'BACKSPACE':
            self._cache = self._cache[:-1]
        else:
            self._cache += key
          
        if 'LEFTSHIFTU' in self._cache:
            # Only unlock when typed "undonut"
            self._locked = False
            self._cache = ''  
        elif 'DONUT' in self._cache or 'DOUGHNUT' in self._cache:
            # TODO enable screen saver or something else...
            self._logger.info("Donut detected!")
            self.busted()
            # Reset cache back to empty after a detection
            self._cache = ''
        
        if self._locked and not 'UNDONUT' in self._cache:
            self.busted()

    def busted(self):
        self._locked = True
        cmd = 'gnome-screensaver-command -l'
        p = Popen(cmd, shell=True)
        p.communicate()

    def run(self):
        try:
            for dev in self._devices:
                self._logger.info(dev.fn, dev.name, dev.phys)
                for event in dev.read_loop():
                    if event.type == ecodes.EV_KEY:
                        cat_event = categorize(event)
                        if cat_event.keystate == 1:
                            print "Detected key press: %s" % cat_event.keycode
                            self.detect_donut(cat_event.keycode.lstrip('KEY_'))
        except Exception as e:
            self._logger.error(e)

if __name__ == "__main__":
    dd = Donut_Detector()
    dd.run()

