#! /usr/bin/python

import gtk
import pango

quotes = """Excess of joy is harder to bear than any amount of sorrow.
The more one judges, the less one loves.
There is no such thing as a great talent without great will power.
"""

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Quotes")
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        label = gtk.Label(quotes)
        gtk.gdk.beep()

        fontdesc = pango.FontDescription("Purisa 10")
	label.modify_font(fontdesc)
        fix = gtk.Fixed()
        fix.put(label, 5, 5)
        self.add(fix)
        self.show_all()

PyApp()
gtk.main()
