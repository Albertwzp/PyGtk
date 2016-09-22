#! /usr/bin/python

import gtk
import pango

quote = "<span foreground='red' size='12000'>The only victory over love is flight</span>"

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Markup")
        self.set_border_width(5)
        self.set_position(gtk.WIN_POS_CENTER)

        label = gtk.Label()
        label.set_markup(quote)

        vbox = gtk.VBox(False, 0)
        vbox.add(label)
        self.add(vbox)
    
        self.connect("destroy", gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()
