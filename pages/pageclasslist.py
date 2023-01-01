import sys
from back import *
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
from pages.pageclass import *


class pageclasslistbox(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        # Page 1

        self.leaflet = Adw.Leaflet(
            halign=Gtk.Align.FILL,
            valign=Gtk.Align.FILL
        )

        self.leaflet.set_can_unfold(False)

        self.append(self.leaflet)

        self.boxClamp = Adw.Clamp()
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.boxClamp.set_child(self.box)
        # Scrollbar
        self.scrolledwindow = Gtk.ScrolledWindow.new()
        self.scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolledwindow.set_child(self.boxClamp)
        self.scrolledwindow.set_vexpand(True)

        self.leaflet.append(self.scrolledwindow)

        # ListBox
        self.listbox1 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.listbox1.get_style_context().add_class('boxed-list')

        self.prfgr_listbox1 = Adw.PreferencesGroup(
            title='Classes',
            margin_top=10
        )

        self.box.append(self.prfgr_listbox1)
        self.box.append(
            self.listbox1
        )

        self.rows_listbox = []
        self.generate_class_list()

        # ListBox
        self.listbox2 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.listbox2.get_style_context().add_class('boxed-list')

        self.prfgr_listbox2 = Adw.PreferencesGroup(
            title='Ajouter classe',
            margin_top=10
        )

        self.box.append(self.prfgr_listbox2)
        self.box.append(
            self.listbox2
        )

        # Row 1
        self.row_listbox2_1 = Adw.ActionRow(
            title='Nom',
            subtitle='Nom de la classe a ajouter.'
        )

        self.btn_listbox2_1_suffix = Gtk.Entry()
        self.btn_listbox2_1_suffix.set_margin_bottom(10)
        self.btn_listbox2_1_suffix.set_margin_top(10)
        self.row_listbox2_1.add_suffix(
            self.btn_listbox2_1_suffix
        )

        self.listbox2.append(
            self.row_listbox2_1
        )

        # Row 2
        self.row_listbox2_2 = Adw.ActionRow(
            title='Année',
            subtitle='Année de la classe a ajouter.'
        )

        self.btn_listbox2_2_suffix = Gtk.SpinButton.new(Gtk.Adjustment.new(2022, 1900, 2147483647, 1, 1, 1), 1, 0)
        self.btn_listbox2_2_suffix.set_margin_bottom(10)
        self.btn_listbox2_2_suffix.set_margin_top(10)
        self.row_listbox2_2.add_suffix(
            self.btn_listbox2_2_suffix
        )

        self.listbox2.append(
            self.row_listbox2_2
        )

        self.addbtn = Gtk.Button(label='Ajouter')
        self.addbtn.connect('clicked', self.btn_ajouter_classe)
        self.listbox2.append(self.addbtn)

        # ClassIndividual Page
        self.indiduallistpage = pageclassbox(
            (("Doe", "Jhon", ("Classe Test",), True, None), ("User", "Name", ("Classe Test",), True, None)))
        self.leaflet.append(self.indiduallistpage)

    def on_btn_show_individuallistpage(self, widget):
        self.leaflet.set_visible_child(self.indiduallistpage)
        self.get_root().hide_viewswitcher()

    def generate_class_list(self):
        """
        Génère la liste des classe.
        """
        for row in self.rows_listbox:
            self.listbox1.remove(row)

        # HACK: L'application crash au bout de 2 ajout de classe si on ne redéfinit pas la liste.
        self.rows_listbox = []

        lclasse = ()
        try:
            connection_bdd = sqlite3.connect("supernote.db")
            lclasse = liste_classe(connection_bdd)
            connection_bdd.close()
        except Exception as e:
            print(e)
            infobar = Gtk.InfoBar()
            infobar.add_child(Gtk.Label(label=f"Une erreur est survenue. \n\n {e}"))
            infobar.add_button("OK", 1)
            infobar.connect('response', self.removeinfobar)
            self.prepend(infobar)
            return None
        for classe in lclasse:
            # Row 1
            self.rows_listbox.append(Adw.ActionRow(
                title=f'{classe[0]} | {classe[1]}'
            ))

            self.rows_listbox[len(self.rows_listbox)-1].suffix1 = Gtk.Button(
                label='Accéder',
                halign=Gtk.Align.CENTER,
                valign=Gtk.Align.CENTER,
            )

            self.rows_listbox[len(self.rows_listbox)-1].suffix1.connect(
                'clicked',
                self.on_btn_show_individuallistpage
            )

            self.rows_listbox[len(self.rows_listbox)-1].add_suffix(
                self.rows_listbox[len(self.rows_listbox)-1].suffix1
            )
            self.rows_listbox[len(self.rows_listbox)-1].suffix2 = Gtk.Button.new_from_icon_name('edit-delete-symbolic')
            self.rows_listbox[len(self.rows_listbox)-1].suffix2.get_style_context().add_class('circular')
            self.rows_listbox[len(self.rows_listbox)-1].suffix2.get_style_context().add_class('destructive-action')
            self.rows_listbox[len(self.rows_listbox)-1].suffix2.set_margin_top(13)
            self.rows_listbox[len(self.rows_listbox)-1].suffix2.set_margin_bottom(13)
            self.rows_listbox[len(self.rows_listbox)-1].add_suffix(
                self.rows_listbox[len(self.rows_listbox)-1].suffix2
            )

            self.listbox1.append(
                self.rows_listbox[len(self.rows_listbox)-1]
            )



    def btn_ajouter_classe(self, widget):
        """
        Fonction pour ajouter une classe depuis un clic sur un bouton
        :param widget: widget sur le quel on clique
        :type widget:
        """
        nom_classe = self.btn_listbox2_1_suffix.get_buffer().get_text()
        annee_classe = self.btn_listbox2_2_suffix.get_adjustment().get_value()
        if nom_classe == "":
            infobar = Gtk.InfoBar()
            infobar.add_child(Gtk.Label(label="Impossible de créer une classe avec un nom vide."))
            infobar.add_button("OK", 1)
            infobar.connect('response', self.removeinfobar)
            self.prepend(infobar)
            return None
        connection_bdd = sqlite3.connect("supernote.db")
        try:
            for classe in liste_classe(connection_bdd):
                if nom_classe == classe[0] and annee_classe == classe[1]:
                    raise Exception("La classe existe déja.")
            ajouter_classe(connection_bdd, nom_classe, annee_classe)
            connection_bdd.commit()
            infobar = Gtk.InfoBar()
            infobar.add_child(Gtk.Label(label="Classe créée avec succès."))
            infobar.add_button("OK", 1)
            infobar.connect('response', self.removeinfobar)
            self.prepend(infobar)
            self.btn_listbox2_1_suffix.get_buffer().delete_text(0, self.btn_listbox2_1_suffix.get_buffer().get_length())
            self.generate_class_list()
            self.get_root().page3.update_class_list()
            for individual in self.indiduallistpage.widgetlist:
                individual.pageindividual.modifierpage.update_class_list()
        except Exception as e:
            print(e)
            infobar = Gtk.InfoBar()
            infobar.add_child(Gtk.Label(label=f"Une erreur est survenue. \n\n {e}"))
            infobar.add_button("OK", 1)
            infobar.connect('response', self.removeinfobar)
            self.prepend(infobar)
        finally:
            connection_bdd.close()


    def removeinfobar(self, widget, response):
        return widget.get_parent().remove(widget)
