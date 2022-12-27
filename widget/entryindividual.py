import gi

gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from gi.repository import Gtk, Adw


class entryindividual (Gtk.Button):
    def __init__(self, nom, prenom, classe, photo=None):
        super().__init__()
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.box)
        self.photo = photo
        self.nom = nom
        self.prenom = prenom
        self.classe = classe
        self.box.set_spacing(10)

        self.set_margin_top(15)

        self.avatar = Adw.Avatar.new(64, f"{self.nom}, {self.prenom}", True)
        self.box.append(self.avatar)

        self.label = Gtk.Label(label=f"{self.nom} {self.prenom}\n - {self.classe}")
        self.label.set_hexpand(True)
        self.label.set_halign(Gtk.Align(1))
        self.box.append(self.label)
