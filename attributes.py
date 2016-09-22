#! /usr/bin/python

import gtk
import pango

text = "Valour fate kinship drakness"

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Attributes")
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        label = gtk.Label(text)
        attr = pango.AttrList()

        fg_color = pango.AttrForeground(65535, 0, 0, 0, 6)
        underline = pango.AttrUnderline(pango.UNDERLINE_DOUBLE, 7, 11)
        bg_color = pango.AttrBackground(40000, 40000, 4000, 12, 19)
        strike = pango.AttrStrikethrough(True, 20, 29)
        size = pango.AttrSize(30000, 0, -1)

        attr.insert(fg_color)
        attr.insert(underline)
        attr.insert(bg_color)
        attr.insert(size)
        attr.insert(strike)

        label.set_attributes(attr)

        fix = gtk.Fixed()
        fix.put(label, 5, 5)
        self.add(fix)

        self.show_all()

PyApp()
gtk.main()
