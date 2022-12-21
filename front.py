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
from gi.repository import Gtk, GLib
from widget.searchentryindividual import *


class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs
        )
        GLib.set_prgname(
            'SuperNote'
        )
        GLib.set_application_name(
            'SuperNote'
        )
        GLib.set_prgname(
            'SuperNote'
        )

        self.set_name(
            'SuperNote'
        )
        self.set_default_size(780, 300)
        self.set_title("SuperNote")

        self.box_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            halign=Gtk.Align.FILL,
            valign=Gtk.Align.FILL,
            hexpand=True,
            vexpand=True
        )
        self.set_content(
            self.box_main
        )

        self.hb = Adw.HeaderBar(
            centering_policy=Adw.CenteringPolicy.STRICT
        )
        self.box_main.append(self.hb)

        self.stack = Adw.ViewStack()
        self.box_main.append(
            self.stack
        )

        # Squeezer
        self.sq_viewswitcher = Adw.Squeezer(
            halign=Gtk.Align.FILL,
        )
        self.sq_viewswitcher.set_switch_threshold_policy(
            Adw.FoldThresholdPolicy.NATURAL
        )
        self.sq_viewswitcher.set_transition_type(
            Adw.SqueezerTransitionType.CROSSFADE
        )
        self.sq_viewswitcher.set_xalign(1)
        self.sq_viewswitcher.set_homogeneous(True)
        self.hb.set_title_widget(
            self.sq_viewswitcher
        )

        # ViewSwitcher (wide)
        self.viewswitcher_wide = Adw.ViewSwitcher(
            halign=Gtk.Align.CENTER,
            margin_start=50,
            margin_end=50
        )
        self.viewswitcher_wide.set_policy(
            Adw.ViewSwitcherPolicy.WIDE
        )
        self.viewswitcher_wide.set_stack(
            self.stack
        )
        self.sq_viewswitcher.add(
            self.viewswitcher_wide
        )

        # ViewSwitcher (narrow)
        self.viewswitcher_narrow = Adw.ViewSwitcher(
            halign=Gtk.Align.CENTER,
        )
        self.viewswitcher_narrow.set_policy(
            Adw.ViewSwitcherPolicy.NARROW
        )
        self.viewswitcher_narrow.set_stack(
            self.stack
        )
        self.sq_viewswitcher.add(
            self.viewswitcher_narrow
        )

        # ViewSwitcherBar (bottom viewswitcher)
        self.viewswitcherbar = Adw.ViewSwitcherBar(
            vexpand=True,
            valign=Gtk.Align.END
        )
        self.viewswitcherbar.set_vexpand(False)
        self.viewswitcherbar.set_stack(
            self.stack
        )
        self.viewswitcherbar.set_reveal(False)
        self.box_main.append(
            self.viewswitcherbar
        )

        # Window Title
        self.wintitle = Adw.WindowTitle(
            title='SuperNote'
        )
        self.sq_viewswitcher.add(self.wintitle)

        # Connect signals
        self.sq_viewswitcher.connect(
            'notify::visible-child',
            self.on_sq_get_visible_child
        )

        # Page 1
        self.page1 = Adw.Clamp()

        self.classbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Scrollbar
        self.classscrolledwindow = Gtk.ScrolledWindow.new()
        self.classscrolledwindow.set_policy (Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.classscrolledwindow.set_child(self.classbox)
        self.classscrolledwindow.set_vexpand(True)

        self.page1.set_child(self.classscrolledwindow)

        # ListBox
        self.classlistbox1 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.classlistbox1.get_style_context().add_class('boxed-list')


        self.prfgr_classlistbox1 = Adw.PreferencesGroup(
            title='Classes',
            margin_top=10
        )

        self.classbox.append(self.prfgr_classlistbox1)
        self.classbox.append(
            self.classlistbox1
        )

        # Row 1
        self.row_classlistbox1_1 = Adw.ActionRow(
            title='Classe Test'
        )

        self.btn_classlistbox1_1_suffix = Gtk.Button(
            label='Accéder',
            halign=Gtk.Align.CENTER,
            valign=Gtk.Align.CENTER,
        )
        self.row_classlistbox1_1.add_suffix(
            self.btn_classlistbox1_1_suffix
        )

        self.classlistbox1.append(
            self.row_classlistbox1_1
        )

        # Row 2
        self.row_classlistbox1_2 = Adw.ActionRow(
            title='Classe Test 2'
        )

        self.btn_classlistbox1_2_suffix = Gtk.Button(
            label='Accéder',
            halign=Gtk.Align.CENTER,
            valign=Gtk.Align.CENTER,
        )
        self.row_classlistbox1_2.add_suffix(
            self.btn_classlistbox1_2_suffix
        )

        self.classlistbox1.append(
            self.row_classlistbox1_2
        )

        # ListBox
        self.classlistbox2 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )
        self.classlistbox2.get_style_context().add_class('boxed-list')

        self.prfgr_classlistbox2 = Adw.PreferencesGroup(
            title='Ajouter classe',
            margin_top=10
        )

        self.classbox.append(self.prfgr_classlistbox2)
        self.classbox.append(
            self.classlistbox2
        )

        # Row 1
        self.row_classlistbox2_1 = Adw.ActionRow(
            title='Nom',
            subtitle='Nom de la classe a ajouter.'
        )

        self.btn_classlistbox2_1_suffix = Gtk.Entry()
        self.btn_classlistbox2_1_suffix.set_margin_bottom(10)
        self.btn_classlistbox2_1_suffix.set_margin_top(10)
        self.row_classlistbox2_1.add_suffix(
            self.btn_classlistbox2_1_suffix
        )

        self.classlistbox2.append(
            self.row_classlistbox2_1
        )

        # Row 2
        self.row_classlistbox2_2 = Adw.ActionRow(
            title='Année',
            subtitle='Année de la classe a ajouter.'
        )

        self.btn_classlistbox2_2_suffix = Gtk.SpinButton.new(Gtk.Adjustment.new(2022, 1900, 2147483647, 1, 1, 1), 1, 0)
        self.btn_classlistbox2_1_suffix.set_margin_bottom(10)
        self.btn_classlistbox2_1_suffix.set_margin_top(10)
        self.row_classlistbox2_2.add_suffix(
            self.btn_classlistbox2_2_suffix
        )

        self.classlistbox2.append(
            self.row_classlistbox2_2
        )

        self.classaddbtn = Gtk.Button(label='Ajouter')
        self.classlistbox2.append(self.classaddbtn)

        self.stack.add_titled(
            self.page1,
            'page0',
            'Classes'
        )
        self.stack.get_page(self.page1).set_icon_name(
            'system-users-symbolic'
        )

        # Page 2

        # Permet de pas prendre touter la largeur de la fenetre
        self.page2 = Adw.Clamp()

        # Boite principal
        self.searchbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Ajout de la boite principale
        self.page2.set_child(self.searchbox)

        # Boite de résultat
        self.searchresultbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Scrollbar
        self.searchscrolledwindow = Gtk.ScrolledWindow.new()
        self.searchscrolledwindow.set_child(self.searchresultbox)
        self.searchscrolledwindow.set_vexpand(True)

        # Barre de recherche
        self.searchsearchentry = Gtk.SearchEntry()
        self.searchsearchentry.set_margin_top(15)

        # Ajout de la barre de recherche dans la boite pricipal
        self.searchbox.append(self.searchsearchentry)

        # Ajout de la boite de résultat dans la boite pricipal
        self.searchbox.append(self.searchscrolledwindow)

        # Ajout de résultat
        self.searchresult = searchentryindividual("John Doe", "Classe Test")
        self.searchresult2 = searchentryindividual("Jane Doe", "Classe Test")
        self.searchresult3 = searchentryindividual("Nobody", "Classe Test")
        self.searchresultbox.append(self.searchresult)
        self.searchresultbox.append(self.searchresult2)
        self.searchresultbox.append(self.searchresult3)

        self.stack.add_titled(
            self.page2,
            'page1',
            'Rechercher Individu'
        )
        self.stack.get_page(self.page2).set_icon_name(
            'edit-find-symbolic'
        )

        # Page 3
        self.page3 = Adw.Clamp()

        self.userbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # self.userbox.set_spacing(10)

        # Scrollbar
        self.userscrolledwindow = Gtk.ScrolledWindow.new()
        self.userscrolledwindow.set_policy (Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.userscrolledwindow.set_child(self.userbox)
        self.userscrolledwindow.set_vexpand(True)

        self.page3.set_child(self.userscrolledwindow)

        self.useravatar=Adw.Avatar.new(128, "", True)
        self.useravatar.set_margin_top(20)
        self.userbox.append(self.useravatar)

        # ListBox
        self.userlistbox1 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.prfgr_userlistbox1 = Adw.PreferencesGroup(
            title='Informations',
            margin_top=10
        )

        self.userbox.append(self.prfgr_userlistbox1)
        self.userbox.append(self.userlistbox1)

        self.userlistbox1.get_style_context().add_class('boxed-list')

        """self.box_listbox_wrapper.append(
            self.listbox1
        )"""

        # Row 1
        self.row_userlistbox1_1 = Adw.ActionRow(
            title='Nom',
            subtitle="Nom de l'individu"
        )

        self.btn_userlistbox1_1_suffix = Gtk.Entry()
        self.btn_userlistbox1_1_suffix.set_margin_top(10)
        self.btn_userlistbox1_1_suffix.set_margin_bottom(10)
        self.row_userlistbox1_1.add_suffix(
            self.btn_userlistbox1_1_suffix
        )

        self.userlistbox1.append(
            self.row_userlistbox1_1
        )

        # Row 2
        self.row_userlistbox1_2 = Adw.ActionRow(
            title='Prénom',
            subtitle="Prénom de l'individu"
        )

        self.btn_userlistbox1_2_suffix = Gtk.Entry()
        self.btn_userlistbox1_2_suffix.set_margin_top(10)
        self.btn_userlistbox1_2_suffix.set_margin_bottom(10)
        self.row_userlistbox1_2.add_suffix(
            self.btn_userlistbox1_2_suffix
        )

        self.userlistbox1.append(
            self.row_userlistbox1_2
        )

        # Status
        self.userlistbox2 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.prfgr_userlistbox2 = Adw.PreferencesGroup(
            title='Status',
            margin_top=10
        )

        self.userbox.append(self.prfgr_userlistbox2)
        self.userbox.append(self.userlistbox2)

        # Row 1
        self.row_userlistbox2_1 = Adw.ActionRow(
            title='Élève',
            subtitle="Ajoute l'individu au groupe élève."
        )

        self.btn_userlistbox2_1_suffix = Gtk.Switch()
        self.btn_userlistbox2_1_suffix.set_margin_top(15)
        self.btn_userlistbox2_1_suffix.set_margin_bottom(15)
        self.row_userlistbox2_1.add_suffix(
            self.btn_userlistbox2_1_suffix
        )

        self.userlistbox2.append(
            self.row_userlistbox2_1
        )

        # Classes
        self.userlistbox3 = Gtk.ListBox(
            selection_mode=Gtk.SelectionMode.NONE
        )

        self.prfgr_userlistbox3 = Adw.PreferencesGroup(
            title='Classes',
            margin_top=10
        )

        self.userbox.append(self.prfgr_userlistbox3)
        self.userbox.append(self.userlistbox3)

        # Row 1
        self.row_userlistbox3_1 = Adw.ActionRow(
            title='Classe Test',
            subtitle="Ajoute l'individu a la classe Classe Test."
        )

        self.btn_userlistbox3_1_suffix = Gtk.Switch()
        self.btn_userlistbox3_1_suffix.set_margin_top(15)
        self.btn_userlistbox3_1_suffix.set_margin_bottom(15)
        self.row_userlistbox3_1.add_suffix(
            self.btn_userlistbox3_1_suffix
        )

        self.userlistbox3.append(
            self.row_userlistbox3_1
        )

        # Row 2
        self.row_userlistbox3_2 = Adw.ActionRow(
            title='Classe Test 2',
            subtitle="Ajoute l'individu a la classe Classe Test 2."
        )

        self.btn_userlistbox3_2_suffix = Gtk.Switch()
        self.btn_userlistbox3_2_suffix.set_margin_top(15)
        self.btn_userlistbox3_2_suffix.set_margin_bottom(15)
        self.row_userlistbox3_2.add_suffix(
            self.btn_userlistbox3_2_suffix
        )

        self.userlistbox3.append(
            self.row_userlistbox3_2
        )

        self.userconfirmbtn= Gtk.Button(label='Ajouter')
        self.userconfirmbtn.set_margin_top(10)
        self.userbox.append(self.userconfirmbtn)



        self.stack.add_titled(
            self.page3,
            'page2',
            'Ajouter Individu'
        )
        self.stack.get_page(self.page3).set_icon_name(
            'contact-new-symbolic'
        )

    def on_sq_get_visible_child(self, widget, event):
        if self.sq_viewswitcher.get_visible_child() == self.wintitle:
            self.viewswitcherbar.set_reveal(True)
        else:
            self.viewswitcherbar.set_reveal(False)


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect(
            'activate',
            self.on_activate
        )

    def on_activate(self, appl):
        self.win = MainWindow(
            application=appl
        )
        self.win.present()


app = MyApp(
    application_id='fr.ajmf.supernote'
)
app.run(sys.argv)
