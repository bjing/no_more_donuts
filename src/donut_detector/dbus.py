import dbus

def screensaver_active():
    bus = dbus.SessionBus()
    screensaver = bus.get_object('org.gnome.ScreenSaver', '/org/gnome/ScreenSaver')
    return bool(screensaver.GetActive())

print screensaver_active()