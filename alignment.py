#! /usr/bin/python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Alignment")
        self.set_size_request(800,600)
        self.set_position(gtk.WIN_POS_CENTER)

        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 3)

        valign = gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(valign)

        ok = gtk.Button("OK")
        ok.set_size_request(150, 100)
        close = gtk.Button("Close")

        hbox.add(ok)
        hbox.add(close)

       halign = gtk.Alignment(1, 0, 0, 0)
       halign.add(hbox)

       vbox.pack_start(halign, False, False, 3)

       self.add(vbox)

       self.connect("destroy", gtk.main_quit)
       self.show_all()

PyApp()
gtk.main()
