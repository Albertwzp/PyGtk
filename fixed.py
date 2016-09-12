#! /usr/bin/python

import gtk
import sys

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Fixed")
        self.set_size_request(1000, 500)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(1600, 1600, 5440))
        self.set_position(gtk.WIN_POS_CENTER)

        try:
            self.lt = gtk.gdk.pixbuf_new_from_file("/root/Downloads/lt.jpg")
            self.lye = gtk.gdk.pixbuf_new_from_file("/root/Downloads/lye.jpg")
            self.ly = gtk.gdk.pixbuf_new_from_file("/root/Downloads/ly.jpg")
        except Exception, e:
            print e.message
            sys.exit(1)

        image1 = gtk.Image()
        image2 = gtk.Image()
        image3 = gtk.Image()

        image1.set_from_pixbuf(self.lt)
        image2.set_from_pixbuf(self.lye)
        image3.set_from_pixbuf(self.ly)

        fix = gtk.Fixed()

        fix.put(image1, 20, 20)
        fix.put(image2, 300, 20)
        fix.put(image3, 500, 200)

        self.add(fix)

        self.connect("destroy", gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()
