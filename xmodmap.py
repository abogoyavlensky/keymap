#!/usr/bin/env python

import os
from subprocess import check_output

import dbus
import gobject
from dbus.mainloop.glib import DBusGMainLoop

DEFAULT_XMODMAP_PATH = '~/xmodmap/.Xmodmap'
ALT_XMODMAP_PATH = '~/xmodmap/.Xmodmap_ru'
ALT_LOCALE = 'ru,us'


def is_alt_locale():
    return ALT_LOCALE in check_output(['setxkbmap', '-query'])

def xmodmap():
    file_path = ALT_XMODMAP_PATH if is_alt_locale() else DEFAULT_XMODMAP_PATH
    os.system('xmodmap ' + file_path)

def event_handler(args):
    if args == 'com.canonical.indicator.keyboard':
        xmodmap()

# Run xmodmap by default for current locale
xmodmap()

# Run xmodmap by changing layout
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_signal_receiver(event_handler,
                        dbus_interface='com.canonical.Unity.Panel.Service',
                        signal_name='ReSync')

loop = gobject.MainLoop()
loop.run()
