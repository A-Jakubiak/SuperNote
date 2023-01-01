import gi

gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
from gi.repository import Gtk, Gdk
import sqlite3
from back import *
from pages.pageclass import *


class pageaddbox(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.clamp = Adw.Clamp()


        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Scrollbar
        self.scrolledwindow = Gtk.ScrolledWindow.new()
        self.scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolledwindow.set_child(self.clamp)
        self.scrolledwindow.set_vexpand(True)
        self.append(self.scrolledwindow)
        self.clamp.set_child(self.box)

        self.avatarbutton = Gtk.Button()
        self.avatarbutton.connect("clicked", self.show_file_chooser)
        self.avatarbutton.set_halign(3)
        self.avatar = Adw.Avatar.new(128, "", True)
        self.avatar.file = None
        self.avatarbutton.set_child(self.avatar)
        self.avatarbutton.set_margin_top(20)
        self.box.append(self.avatarbutton)
        self.filechooserdialog = Gtk.FileChooserNative.new(title="Sélectionner une photo.",
                                  parent=self.get_root(), action=Gtk.FileChooserAction.OPEN)
        self.filechooserdialog.set_transient_for(self.get_root())
        self.filter = Gtk.FileFilter()
        self.filter.set_name("Photo")
        self.filter.add_pattern("*.png")
        self.filter.add_pattern("*.jpg")
        self.filter.add_pattern("*.jpeg")
        self.filechooserdialog.add_filter(self.filter)
        self.filechooserdialog.connect("response", self.filechooserresponse)

        # ListBox
        self.listbox1 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.prfgr_listbox1 = Adw.PreferencesGroup(
            title='Informations',
            margin_top=10
        )

        self.box.append(self.prfgr_listbox1)
        self.box.append(self.listbox1)

        self.listbox1.get_style_context().add_class('boxed-list')


        # Row 1
        self.row_listbox1_1 = Adw.ActionRow(
            title='Nom',
            subtitle="Nom de l'individu"
        )

        self.btn_listbox1_1_suffix = Gtk.Entry()
        self.btn_listbox1_1_suffix.set_margin_top(10)
        self.btn_listbox1_1_suffix.set_margin_bottom(10)
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

        self.btn_listbox1_2_suffix = Gtk.Entry()
        self.btn_listbox1_2_suffix.set_margin_top(10)
        self.btn_listbox1_2_suffix.set_margin_bottom(10)
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
            title='Status',
            margin_top=10
        )

        self.box.append(self.prfgr_listbox2)
        self.box.append(self.listbox2)

        # Row 1
        self.row_listbox2_1 = Adw.ActionRow(
            title='Élève',
            subtitle="Ajoute l'individu au groupe élève."
        )

        self.btn_listbox2_1_suffix = Gtk.Switch()
        self.btn_listbox2_1_suffix.set_margin_top(15)
        self.btn_listbox2_1_suffix.set_margin_bottom(15)
        self.row_listbox2_1.add_suffix(
            self.btn_listbox2_1_suffix
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
            title='Classes',
            margin_top=10
        )

        self.box.append(self.prfgr_listbox3)
        self.box.append(self.listbox3)

        self.rows_listbox3 = []
        self.update_class_list()

        self.confirmbtn = Gtk.Button(label='Ajouter')
        self.confirmbtn.set_margin_top(10)
        self.box.append(self.confirmbtn)

    def update_class_list(self):
        """
        Génère la liste de switch pour les classes.
        """
        for row in self.rows_listbox3:
            self.listbox3.remove(row)

        # HACK: L'application crash au bout de 2 ajout de classe si on ne redéfinit pas la liste.
        self.rows_listbox3 = []

        connection_bdd = None
        try:
            connection_bdd = sqlite3.connect("supernote.db")
        except Exception as e:
            infobar = Gtk.InfoBar()
            infobar.add_child(Gtk.Label(label=f"Une erreur est survenue. \n\n {e}"))
            infobar.add_button("OK", 1)
            infobar.connect('response', self.removeinfobar)
            self.prepend(infobar)
            return None
        for classe in liste_classe(connection_bdd):

            self.rows_listbox3.append(Adw.ActionRow(
                title=f"{classe[0]}, {classe[1]}",
                subtitle=f"Ajoute l'individu à la classe {classe[0]}."
            ))

            self.rows_listbox3[len(self.rows_listbox3)-1].suffix = Gtk.Switch()
            self.rows_listbox3[len(self.rows_listbox3)-1].suffix.set_margin_top(15)
            self.rows_listbox3[len(self.rows_listbox3)-1].suffix.set_margin_bottom(15)
            self.rows_listbox3[len(self.rows_listbox3)-1].add_suffix(
                self.rows_listbox3[len(self.rows_listbox3)-1].suffix
            )

            self.listbox3.append(
                self.rows_listbox3[len(self.rows_listbox3)-1]
            )
        connection_bdd.close()

    def show_file_chooser(self, widget):
        self.filechooserdialog.show()

    def filechooserresponse(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            filename = file.get_path()
            self.avatar.file = file
            self.avatar.set_custom_image(Gdk.Texture.new_from_file(file))
