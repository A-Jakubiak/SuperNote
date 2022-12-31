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
from pages.pageindividual import *
from widget.entryindividual import *
class pageclassbox (Gtk.Box):
    def __init__(self, classmemberlist):
        super().__init__()
        self.classmemberlist = classmemberlist
        self.leaflet = Adw.Leaflet(
            halign=Gtk.Align.FILL,
            valign=Gtk.Align.FILL
        )

        self.leaflet.set_can_unfold(False)
        self.append(self.leaflet)


        self.scrolledwindow = Gtk.ScrolledWindow()
        self.scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolledwindow.set_vexpand(True)
        self.leaflet.append(self.scrolledwindow)
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.clamp = Adw.Clamp()
        self.clamp.set_child(self.box)
        self.scrolledwindow.set_child(self.clamp)
        self.widgetlist = []
        for individual in self.classmemberlist:
            self.widgetlist.append(entryindividual(individual))
            self.box.append(self.widgetlist[len(self.widgetlist)-1])
        self.backbutton=Gtk.Button(label="Retour")
        self.backbutton.set_margin_top(10)
        self.backbutton.connect('clicked', self.leaflet_go_back)
        self.box.append(self.backbutton)

        # page individual

        for individual in self.widgetlist:
            individual.connect('clicked', self.btn_go_to_individual)
            self.leaflet.append(individual.pageindividual)
    def btn_go_to_individual(self, widget):
        self.leaflet.set_visible_child(widget.pageindividual)

    def leaflet_go_back(self, widget):
        self.get_parent().set_visible_child(self.get_parent().get_parent().scrolledwindow)
        self.get_root().show_viewswitcher()