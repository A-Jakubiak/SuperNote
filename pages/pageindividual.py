import sys

import gi
import datetime
gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from gi.repository import Gtk, Adw, GLib, Gio
import back
import configfile
import sqlite3
from pages.pageindividualmodifier import *


class pageindividualbox (Gtk.Box):
    def __init__(self, individual):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.individual = individual

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

        self.avatar = Adw.Avatar.new(128, f"{self.individual[1]}, {self.individual[2]}", True)
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

        self.btn_listbox1_1_suffix = Gtk.Label(label=self.individual[1])
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

        self.btn_listbox1_2_suffix = Gtk.Label(label=self.individual[2])
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

        self.list_row_classe = []

        # absences

        self.prfgr_listbox4 = Adw.PreferencesGroup(
            title='Absences'
        )
        self.prfgr_listbox4.set_margin_top(10)

        self.listbox4 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.listbox4.get_style_context().add_class('boxed-list')

        self.list_row_abs = []

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
        self.addabsbutton.connect('clicked', self.btn_ajouter_absence)
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
        self.modifierpage = pageindividualmodifierbox(self.individual)
        self.leaflet.append(self.modifierpage)

        self.generate()

    def generate(self):
        if self.individual[4]:
            self.listbox2.append(
                self.row_listbox2_1
            )
        else:
            try:
                self.listbox2.remove(self.listbox2.get_row_at_index(0))
            except:
                pass

        for row in self.list_row_classe:
            self.listbox3.remove(row)

        self.list_row_classe = []
        connection_bdd = sqlite3.connect(configfile.bdd_path)
        for classe in self.individual[3]:
            self.list_row_classe.append(Adw.ActionRow(
                title=', '.join(map(str,recuperer_nom_date_depuis_id(connection_bdd, classe))),
                subtitle=f"L'individu appartient à la classe {', '.join(map(str, recuperer_nom_date_depuis_id(connection_bdd, classe)))}."
            ))


            self.listbox3.append(
                self.list_row_classe[-1]
            )

        for row in self.list_row_abs:
            self.listbox4.remove(row)

        self.list_row_abs = []

        for absence in liste_absences(connection_bdd, self.individual[0]):
            self.list_row_abs.append( Adw.ActionRow(
                title=datetime.datetime.utcfromtimestamp(absence).strftime("%d/%m/%y"),
                subtitle=f"L'individu a été absent le 23/12/2022 à {datetime.datetime.utcfromtimestamp(absence).strftime('%H')}H"
            ))

            self.list_row_abs[-1].suffix1 = Gtk.Label(label=f"{datetime.datetime.utcfromtimestamp(absence).strftime('%H')}H")
            self.list_row_abs[-1].add_suffix(
                self.list_row_abs[-1].suffix1
            )

            self.list_row_abs[-1].suffix2 = Gtk.Button.new_from_icon_name('edit-delete-symbolic')
            self.list_row_abs[-1].suffix2.get_style_context().add_class('circular')
            self.list_row_abs[-1].suffix2.get_style_context().add_class('destructive-action')
            self.list_row_abs[-1].suffix2.set_margin_top(13)
            self.list_row_abs[-1].suffix2.set_margin_bottom(13)
            self.list_row_abs[-1].add_suffix(
                self.list_row_abs[-1].suffix2
            )

            self.listbox4.append(
                self.list_row_abs[-1]
            )


        connection_bdd.close()
    def btn_ajouter_absence(self, widget):
        date = self.calendar.get_date().get_utc_offset()
        heure= self.btn_listbox5_1_suffix.get_value()
        nb_absences = self.btn_listbox5_2_suffix.get_value()
        timestamp = date + heure*60*60 + 60*2

        connection_bdd = sqlite3.connect(configfile.bdd_path)
        for h in range(nb_absences):
            ajouter_absence(connection_bdd, self.individual[0], timestamp + h*60*60)

        connection_bdd.commit()
        connection_bdd.close()


    def leaflet_go_back(self, widget):
        self.get_parent().set_visible_child(self.get_parent().get_pages()[0].get_child())
        if str(type((self.get_parent().get_parent()))) == "<class 'pages.pagesearch.pagesearchbox'>":
            self.get_root().show_viewswitcher()

    def leaflet_next(self, widget):
        self.leaflet.set_visible_child(self.modifierpage)