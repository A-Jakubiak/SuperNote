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
        for individual in classmemberlist:
            self.widgetlist.append(entryindividual(individual[0], individual[1], individual[2], individual[3]))
            self.box.append(self.widgetlist[len(self.widgetlist)-1])
        self.backbutton=Gtk.Button(label="Retour")
        self.backbutton.set_margin_top(10)
        self.box.append(self.backbutton)

        self.widgetlist[0].connect('clicked', self.btn_go_to_individual)

        # page individual

        self.individualpage = pageindividualbox()
        self.leaflet.append(self.individualpage)
        self.individualpage.backbutton.connect('clicked', self.on_btn_show_list)
    def btn_go_to_individual(self, widget):
        self.leaflet.set_visible_child(self.individualpage)

    def on_btn_show_list(self, widget):
        self.leaflet.set_visible_child(self.scrolledwindow)