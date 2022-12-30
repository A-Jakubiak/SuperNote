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
from pages.pageclass import *


class pageclasslistbox(Gtk.Box):
    def __init__(self):
        super().__init__()
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

        # Row 1
        self.row_listbox1_1 = Adw.ActionRow(
            title='Classe Test'
        )

        self.btn_listbox1_1_suffix1 = Gtk.Button(
            label='Accéder',
            halign=Gtk.Align.CENTER,
            valign=Gtk.Align.CENTER,
        )

        self.btn_listbox1_1_suffix1.connect(
            'clicked',
            self.on_btn_show_individuallistpage
        )

        self.row_listbox1_1.add_suffix(
            self.btn_listbox1_1_suffix1
        )
        self.btn_listbox1_1_suffix2 = Gtk.Button.new_from_icon_name('edit-delete-symbolic')
        self.btn_listbox1_1_suffix2.get_style_context().add_class('circular')
        self.btn_listbox1_1_suffix2.get_style_context().add_class('destructive-action')
        self.btn_listbox1_1_suffix2.set_margin_top(13)
        self.btn_listbox1_1_suffix2.set_margin_bottom(13)
        self.row_listbox1_1.add_suffix(
            self.btn_listbox1_1_suffix2
        )

        self.listbox1.append(
            self.row_listbox1_1
        )

        # Row 2
        self.row_listbox1_2 = Adw.ActionRow(
            title='Classe Test 2'
        )

        self.btn_listbox1_2_suffix1 = Gtk.Button(
            label='Accéder',
            halign=Gtk.Align.CENTER,
            valign=Gtk.Align.CENTER,
        )
        self.row_listbox1_2.add_suffix(
            self.btn_listbox1_2_suffix1
        )
        self.btn_listbox1_2_suffix2 = Gtk.Button.new_from_icon_name('edit-delete-symbolic')
        self.btn_listbox1_2_suffix2.get_style_context().add_class('circular')
        self.btn_listbox1_2_suffix2.get_style_context().add_class('destructive-action')
        self.btn_listbox1_2_suffix2.set_margin_top(13)
        self.btn_listbox1_2_suffix2.set_margin_bottom(13)
        self.row_listbox1_2.add_suffix(
            self.btn_listbox1_2_suffix2
        )
        self.listbox1.append(
            self.row_listbox1_2
        )

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
        self.listbox2.append(self.addbtn)

        # ClassIndividual Page
        self.indiduallistpage = pageclassbox(
            (("Doe", "Jhon", ("Classe Test", ), True, None), ("User", "Name", ("Classe Test", ), True, None)))
        self.leaflet.append(self.indiduallistpage)
    def on_btn_show_individuallistpage(self, widget):
        self.leaflet.set_visible_child(self.indiduallistpage)
        self.get_root().hide_viewswitcher()