import sqlite3

import gi

gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from gi.repository import Gtk, Adw, GLib, Gio
from pages.pageclass import *
from widget.entryindividual import *


class pagesearchbox(Gtk.Box):
    def __init__(self):
        self.resultlist=[]
        self.resultwidgets=[]
        super().__init__()
        self.leaflet = Adw.Leaflet(
            halign=Gtk.Align.FILL,
            valign=Gtk.Align.FILL
        )

        self.leaflet.set_can_unfold(False)

        self.append(self.leaflet)

        self.clamp = Adw.Clamp()
        self.leaflet.append(self.clamp)

        # Boite principal
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Ajout de la boite principale
        self.clamp.set_child(self.box)

        # Boite de résultat
        self.resultbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Scrollbar
        self.scrolledwindow = Gtk.ScrolledWindow.new()
        self.scrolledwindow.set_child(self.resultbox)
        self.scrolledwindow.set_vexpand(True)

        # Barre de recherche
        self.searchentry = Gtk.SearchEntry()
        self.searchentry.set_margin_top(15)
        self.searchentry.set_hexpand(True)
        self.searchentry.connect('search-changed', self.search)

        # Ajout de la barre de recherche dans la boite pricipal
        self.box.append(self.searchentry)

        # Ajout de la boite de résultat dans la boite pricipal
        self.box.append(self.scrolledwindow)

        connection_bdd = sqlite3.connect(configfile.bdd_path)
        self.updateresultlist(recherche_individu(connection_bdd, ''))
        connection_bdd.close()

    def updateresultlist(self, rl):
        self.resultlist = rl
        for widget in self.resultwidgets:
            self.resultbox.remove(widget)
            self.leaflet.remove(widget.pageindividual)

        self.resultwidgets = []

        for individual in self.resultlist:
            self.resultwidgets.append(entryindividual(individual))

        for widget in self.resultwidgets:
            self.resultbox.append(widget)
            self.leaflet.append(widget.pageindividual)
            widget.connect('clicked', self.btn_go_to_individual)


    def search(self, widget):
        connection_bdd = sqlite3.connect(configfile.bdd_path)
        self.updateresultlist(recherche_individu(connection_bdd, widget.get_text()))
        connection_bdd.close()
    def btn_go_to_individual(self, widget):
        self.leaflet.set_visible_child(widget.pageindividual)
        self.get_root().hide_viewswitcher()