import dbus
import util

class Screen_Saver(object):
    _log_file = '/var/log/donut_detector.log'
    
    def __init__(self):
        self._logger = util.get_logger(__name__, log_file=self._log_file)
        
        bus = dbus.SessionBus()
        self._screensaver = bus.get_object('org.cinnamon.ScreenSaver', '/org/cinnamon/ScreenSaver')
        self._activated = bool(self._screensaver.GetActive())
        
    @property
    def activated(self):
        return self._activated
    
    @activated.setter
    def activated(self, active):
        self._logger.info("Setting screen saver activate to %s" % active)
        self._screensaver.SetActive(active)
        
