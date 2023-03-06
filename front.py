import gi
gi.require_version(
    "Gtk",
    "4.0"
)
gi.require_version(
    "Adw",
    "1"
)
import os
from pages.pageclasslist import *
from pages.pagesearch import *
from pages.pageadd import *
from back import *


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

        self.page1 = pageclasslistbox()

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
        self.page2 = pagesearchbox()

        self.stack.add_titled(
            self.page2,
            'page1',
            'Rechercher Individu'
        )
        self.stack.get_page(self.page2).set_icon_name(
            'edit-find-symbolic'
        )

        # Page 3
        self.page3 = pageaddbox()

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

    def hide_viewswitcher(self):
        self.viewswitcherbar.set_visible(False)
        self.viewswitcher_wide.set_visible(False)
        self.viewswitcher_narrow.set_visible(False)

    def show_viewswitcher(self):
        self.viewswitcherbar.set_visible(True)
        self.viewswitcher_wide.set_visible(True)
        self.viewswitcher_narrow.set_visible(True)
        self.page2.updateresultlist()


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


if configfile.bdd_path not in os.listdir():
    creer_bdd(configfile.bdd_path)

app = MyApp(
    application_id='fr.ajmf.supernote'
)
app.run(sys.argv)
