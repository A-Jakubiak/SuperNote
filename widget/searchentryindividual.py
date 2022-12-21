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


class searchentryindividual (Gtk.Box):
    def __init__(self, nom, classe, photo=None):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL)
        self.photo = photo
        self.nom = nom
        self.classe = classe
        self.set_spacing(10)

        self.set_margin_top(15)

        self.avatar = Adw.Avatar.new(64, nom, True)
        self.append(self.avatar)

        self.label = Gtk.Label(label=f"{self.nom}\n - {self.classe}")
        self.label.set_hexpand(True)
        self.label.set_halign(Gtk.Align(1))
        self.append(self.label)

        self.button = Gtk.Button(label="Accéder")
        self.button.set_margin_top(20)
        self.button.set_margin_bottom(20)
        self.append(self.button)
