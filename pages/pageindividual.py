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
from gi.repository import Gtk, Adw, GLib, Gio

from pages.pageindividual import *
from pages.pageindividualmodifier import *
class pageindividualbox (Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.prenom="John"
        self.nom = "Doe"

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
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.clamp = Adw.Clamp()
        self.clamp.set_child(self.box)
        self.scrolledwindow.set_child(self.clamp)

        self.avatar = Adw.Avatar.new(128, f"{self.nom}, {self.prenom}", True)
        self.avatar.set_margin_top(10)
        self.box.append(self.avatar)

        # ListBox
        self.listbox1 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.prfgr_listbox1 = Adw.PreferencesGroup(
            title='Informations'
        )
        self.prfgr_listbox1.set_margin_top(10)

        self.box.append(self.prfgr_listbox1)
        self.box.append(self.listbox1)

        self.listbox1.get_style_context().add_class('boxed-list')

        # Row 1
        self.row_listbox1_1 = Adw.ActionRow(
            title='Nom',
            subtitle="Nom de l'individu"
        )

        self.btn_listbox1_1_suffix = Gtk.Label(label=self.nom)
        self.row_listbox1_1.add_suffix(
            self.btn_listbox1_1_suffix
        )

        self.listbox1.append(
            self.row_listbox1_1
        )

        # Row 2
        self.row_listbox1_2 = Adw.ActionRow(
            title='Prénom',
            subtitle="Prénom de l'individu"
        )

        self.btn_listbox1_2_suffix = Gtk.Label(label=self.prenom)
        self.row_listbox1_2.add_suffix(
            self.btn_listbox1_2_suffix
        )

        self.listbox1.append(
            self.row_listbox1_2
        )

        # Status
        self.listbox2 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.listbox2.get_style_context().add_class('boxed-list')

        self.prfgr_listbox2 = Adw.PreferencesGroup(
            title='Status'
        )

        self.prfgr_listbox2.set_margin_top(10)

        self.box.append(self.prfgr_listbox2)
        self.box.append(self.listbox2)

        # Row 1
        self.row_listbox2_1 = Adw.ActionRow(
            title='Élève',
            subtitle="L'individu appartient au groupe élève."
        )

        self.listbox2.append(
            self.row_listbox2_1
        )

        # Classes
        self.listbox3 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.listbox3.get_style_context().add_class('boxed-list')

        self.prfgr_listbox3 = Adw.PreferencesGroup(
            title='Classes'
        )

        self.prfgr_listbox3.set_margin_top(10)

        self.box.append(self.prfgr_listbox3)
        self.box.append(self.listbox3)

        # Row 1
        self.row_listbox3_1 = Adw.ActionRow(
            title='Classe Test',
            subtitle="L'individu appartient à la classe classe test."
        )

        self.listbox3.append(
            self.row_listbox3_1
        )

        # absences

        self.prfgr_listbox4 = Adw.PreferencesGroup(
            title='Absences'
        )
        self.prfgr_listbox4.set_margin_top(10)

        self.listbox4 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.listbox4.get_style_context().add_class('boxed-list')

        # Row 1
        self.row_listbox4_1 = Adw.ActionRow(
            title='23/12/2022',
            subtitle="L'individu a été absent le 23/12/2022 pendant 1H"
        )

        self.btn_listbox4_1_suffix1 = Gtk.Label(label="1H")
        self.row_listbox4_1.add_suffix(
            self.btn_listbox4_1_suffix1
        )

        self.btn_listbox4_1_suffix2 = Gtk.Button.new_from_icon_name('edit-delete-symbolic')
        self.btn_listbox4_1_suffix2.get_style_context().add_class('circular')
        self.btn_listbox4_1_suffix2.get_style_context().add_class('destructive-action')
        self.btn_listbox4_1_suffix2.set_margin_top(13)
        self.btn_listbox4_1_suffix2.set_margin_bottom(13)
        self.row_listbox4_1.add_suffix(
            self.btn_listbox4_1_suffix2
        )

        self.listbox4.append(
            self.row_listbox4_1
        )

        self.box.append(self.prfgr_listbox4)
        self.box.append(self.listbox4)

        # Ajouter absences

        self.prfgr_listbox5 = Adw.PreferencesGroup(
            title='Ajouter une absence'
        )
        self.prfgr_listbox5.set_margin_top(10)

        self.box.append(self.prfgr_listbox5)

        self.calendar = Gtk.Calendar()
        self.box.append(self.calendar)

        self.listbox5 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.listbox5.set_margin_top(10)

        self.listbox5.get_style_context().add_class('boxed-list')

        # Row 1
        self.row_listbox5_1 = Adw.ActionRow(
            title='Heure',
            subtitle="Heure de l'absence."
        )

        self.btn_listbox5_1_suffix = Gtk.SpinButton.new(Gtk.Adjustment.new(8, 8, 18, 1, 1, 1), 1, 0)
        self.row_listbox5_1.add_suffix(
            self.btn_listbox5_1_suffix
        )

        self.btn_listbox5_1_suffix.set_margin_bottom(10)
        self.btn_listbox5_1_suffix.set_margin_top(10)

        self.listbox5.append(
            self.row_listbox5_1
        )

        # Row 2
        self.row_listbox5_2 = Adw.ActionRow(
            title='durée',
            subtitle="durée de l'absence en heures."
        )

        self.btn_listbox5_2_suffix = Gtk.SpinButton.new(Gtk.Adjustment.new(1, 1, 13, 1, 1, 1), 1, 0)
        self.row_listbox5_2.add_suffix(
            self.btn_listbox5_2_suffix
        )
        self.btn_listbox5_2_suffix.set_margin_bottom(10)
        self.btn_listbox5_2_suffix.set_margin_top(10)

        self.listbox5.append(
            self.row_listbox5_2
        )

        self.box.append(self.listbox5)

        self.addabsbutton=Gtk.Button(label="Ajouter")
        self.box.append(self.addabsbutton)
        self.addabsbutton.set_margin_top(5)

        self.editbutton = Gtk.Button(label="Modifer")
        self.editbutton.get_style_context ().add_class ('suggested-action')
        self.editbutton.set_margin_top(30)
        self.editbutton.connect('clicked', self.leaflet_next)
        self.box.append(self.editbutton)
        self.deletebutton = Gtk.Button(label="Supprimer")
        self.deletebutton.get_style_context ().add_class ('destructive-action')
        self.deletebutton.set_margin_top(10)
        self.box.append(self.deletebutton)
        self.backbutton = Gtk.Button(label="Retour")
        self.backbutton.set_margin_top(10)
        self.backbutton.connect('clicked', self.leaflet_go_back)
        self.box.append(self.backbutton)

        # page de modification
        self.modifierpage = pageindividualmodifierbox(self.nom, self.prenom)
        self.leaflet.append(self.modifierpage)

    def leaflet_go_back(self, widget):
        self.get_parent().set_visible_child(self.get_parent().get_parent().scrolledwindow)

    def leaflet_next(self, widget):
        self.leaflet.set_visible_child(self.modifierpage)