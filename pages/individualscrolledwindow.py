import sys

import gi

gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from gi.repository import Gtk, GLib
from widget.entryindividual import *
class individualScrolledWindow (Gtk.ScrolledWindow):
    def __init__(self, classmemberlist):
        super().__init__()
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_vexpand(True)
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.clamp = Adw.Clamp()
        self.clamp.set_child(self.box)
        self.set_child(self.clamp)
        widgetlist = []
        for individual in classmemberlist:
            widgetlist.append(entryindividual(individual[0], individual[1], individual[2], individual[3]))
            self.box.append(widgetlist[len(widgetlist)-1])
        self.backbutton=Gtk.Button(label="Retour")
        self.backbutton.set_margin_top(10)
        self.box.append(self.backbutton)