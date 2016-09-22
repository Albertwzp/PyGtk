#! /usr/bin/python

import gtk
import glib
import pango
import math

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("ZetCode")
        self.set_size_request(250,200)
        self.set_position(gtk.WIN_POS_CENTER)

        glib.timeout_add(160, self.on_timer)
        self.count = 1
        self.set_border_width(10)
        self.label = gtk.Label("ZetCode")
        fontdesc = pango.FontDescription("Serif Bold 30")
        self.label.modify_font(fontdesc)

        vbox = gtk.VBox(False, 0)
        vbox.add(self.label)
        self.add(vbox)
    
        self.connect("destroy", gtk.main_quit)
        self.show_all()

    def on_timer(self):
        attr = pango.AttrList()
        self.count = self.count + 1
        for i in range(7):
            r =pango.AttrRise(int(math.sin(self.count +i)*20)*pango.SCALE, i, i+1)
            attr.insert(r)
        self.label.set_attributes(attr)
        return True

PyApp()
gtk.main()
