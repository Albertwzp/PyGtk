#! /usr/bin/python

import gtk, sys
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Icon Simple menu")
        self.set_size_request(500,300)
#        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        try:
            self.set_icon_from_file("/root/Downloads/lt.jpg")
        except Exception, e:
            print e.message
            sys.exit(1)


        mb = gtk.MenuBar()
            
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
	filemenu.append(exit)

        mb.append(filem)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        self.add(vbox)
        self.connect("destroy", gtk.main_quit)
        self.show_all()
PyApp()
gtk.main()
