#! /usr/bin/python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("")
        self.set_size_request(250,200)
        self.set_position(gtk.WIN_POS_CENTER)

    
        self.connect("destroy", gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()
