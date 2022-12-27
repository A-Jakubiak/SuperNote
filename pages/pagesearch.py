import gi

gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from pages.pageclass import *


class pagesearchbox(Gtk.Box):
    def __init__(self):
        super().__init__()
        self.clamp = Adw.Clamp()
        self.append(self.clamp)

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

        # Ajout de la barre de recherche dans la boite pricipal
        self.box.append(self.searchentry)

        # Ajout de la boite de résultat dans la boite pricipal
        self.box.append(self.scrolledwindow)

        # Ajout de résultat
        self.result = entryindividual("John", "Doe", "Classe Test")
        self.result2 = entryindividual("Jane", "Doe", "Classe Test")
        self.result3 = entryindividual("Nobody", "", "Classe Test")
        self.resultbox.append(self.result)
        self.resultbox.append(self.result2)
        self.resultbox.append(self.result3)