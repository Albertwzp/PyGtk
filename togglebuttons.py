#! /usr/bin/python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.color = [0, 0, 0]
        self.set_title("ToggleButtons")
        self.set_size_request(350, 240)
        self.set_position(gtk.WIN_POS_CENTER)    
        self.connect("destroy", gtk.main_quit)

        red = gtk.ToggleButton("Red")
        red.set_size_request(80, 35)
        red.connect("clicked", self.onred)
        green = gtk.ToggleButton("Green")
        green.set_size_request(80, 35)
        green.connect("clicked", self.ongreen)
        blue = gtk.ToggleButton("Blue")
        blue.set_size_request(80, 35)
        blue.connect("clicked", self.onblue)

        self.darea = gtk.DrawingArea()
        self.darea.set_size_request(150, 150)
        self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))

        fixed = gtk.Fixed()
        fixed.put(red, 30, 30)
        fixed.put(green, 30, 80)
        fixed.put(blue, 30, 130)
        fixed.put(self.darea, 150, 30)
        self.add(fixed)
        self.show_all()

    def onred(self, widget):
        if widget.get_active():
            self.color[0] = 65535
        else:
            self.color[0] = 0
            self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(self.color[0], self.color[1], self.color[2]))

    def ongreen(self, widget):
        if widget.get_active():
            self.color[1] = 65535
        else:
            self.color[1] = 0
            self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(self.color[0], self.color[1], self.color[2]))

    def onblue(self, widget):
        if widget.get_active():
            self.color[2] = 65535
        else:
            self.color[2] = 0
            self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(self.color[0], self.color[1], self.color[2]))

PyApp()
gtk.main()
