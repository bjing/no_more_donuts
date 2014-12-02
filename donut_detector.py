import sys
import logging
from subprocess import Popen
from evdev import InputDevice, categorize, ecodes

from find_input import find_keyboard_devs

logging.basicConfig(level=logging.INFO)

"""
Categorized key event class methods
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
'__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__slots__', '__str__', '__subclasshook__', 'event', 'key_down', 'key_hold', 'key_up', 'keycode', 'keystate', 'scancode']
"""

class Donut_Detector(object):
    """ This an attempt to avoid being donuted at work, which would suck so bad
    """
    _cache = '' # This is used to record keystrokes
    _devices = None # Input devices
    _locked = False

    def __init__(self):
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
          
        if 'UNDONUT' in self._cache:
            # Only unlock when typed "undonut"
            self._locked = False
            self._cache = ''  
        elif 'DONUT' in self._cache or 'DOGHNUT' in self._cache:
            # TODO enable screen saver or something else...
            logging.info("Donut detected!")
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
                logging.info(dev.fn, dev.name, dev.phys)
                for event in dev.read_loop():
                    if event.type == ecodes.EV_KEY:
                        cat_event = categorize(event)
                        if cat_event.keystate == 1:
                            print "Detected key press: %s" % cat_event.keycode
                            self.detect_donut(cat_event.keycode.lstrip('KEY_'))
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":

    dd = Donut_Detector()
    dd.run()

