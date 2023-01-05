import gi

from pages.pageindividual import *

gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from gi.repository import Gtk, Adw
from back import *
import sqlite3


class entryindividual (Gtk.Button):
    def __init__(self, individual):
        super().__init__()
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.box)
        self.photo = individual[len(individual)-1]
        self.nom = individual[0]
        self.prenom = individual[1]
        self.classe = individual[2]
        self.eleve = individual[3]
        self.box.set_spacing(10)

        self.set_margin_top(15)

        self.avatar = Adw.Avatar.new(64, f"{individual[0]}, {individual[1]}", True)
        self.box.append(self.avatar)

        self.label = Gtk.Label(label=f'{individual[0]} {individual[1]}\n - {"; ".join((map(self.id_vers_classe,individual[2])))}')
        self.label.set_hexpand(True)
        self.label.set_halign(Gtk.Align(1))
        self.box.append(self.label)

        self.pageindividual = pageindividualbox(individual)

    def id_vers_classe(self, id):
        connection_bdd = sqlite3.connect("supernote.db")
        to_return = ', '.join(map(str,recuperer_nom_date_depuis_id(connection_bdd, id)))
        connection_bdd.close()
        return to_return
