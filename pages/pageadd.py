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


class pageaddbox(Gtk.Box):
    def __init__(self):
        super().__init__()
        self.clamp = Adw.Clamp()
        self.append(self.clamp)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Scrollbar
        self.scrolledwindow = Gtk.ScrolledWindow.new()
        self.scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolledwindow.set_child(self.box)
        self.scrolledwindow.set_vexpand(True)

        self.clamp.set_child(self.scrolledwindow)

        self.avatarbutton = Gtk.Button()
        self.avatarbutton.set_halign(3)
        self.avatar = Adw.Avatar.new(128, "", True)
        self.avatarbutton.set_child(self.avatar)
        self.avatarbutton.set_margin_top(20)
        self.box.append(self.avatarbutton)

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

        """self.box_listbox_wrapper.append(
            self.listbox1
        )"""

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

        # Row 1
        self.row_listbox3_1 = Adw.ActionRow(
            title='Classe Test',
            subtitle="Ajoute l'individu a la classe Classe Test."
        )

        self.btn_listbox3_1_suffix = Gtk.Switch()
        self.btn_listbox3_1_suffix.set_margin_top(15)
        self.btn_listbox3_1_suffix.set_margin_bottom(15)
        self.row_listbox3_1.add_suffix(
            self.btn_listbox3_1_suffix
        )

        self.listbox3.append(
            self.row_listbox3_1
        )

        # Row 2
        self.row_listbox3_2 = Adw.ActionRow(
            title='Classe Test 2',
            subtitle="Ajoute l'individu a la classe Classe Test 2."
        )

        self.btn_listbox3_2_suffix = Gtk.Switch()
        self.btn_listbox3_2_suffix.set_margin_top(15)
        self.btn_listbox3_2_suffix.set_margin_bottom(15)
        self.row_listbox3_2.add_suffix(
            self.btn_listbox3_2_suffix
        )

        self.listbox3.append(
            self.row_listbox3_2
        )

        self.confirmbtn = Gtk.Button(label='Ajouter')
        self.confirmbtn.set_margin_top(10)
        self.box.append(self.confirmbtn)