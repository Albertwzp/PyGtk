#! /usr/bin/python

import gtk
import pango

class PyApp(gtk.Window):
    def __init__(self):
	super(PyApp, self).__init__()

        self.set_title("Color Selection Dialog")
        self.set_size_request(300, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        self.label = gtk.Label("The only victory over love is flight.")
        button = gtk.Button("Select color")
        button.connect("clicked", self.on_clicked)

        fix = gtk.Fixed()
        fix .put(button, 100, 30)
        fix.put(self.label, 30, 90)
	self.add(fix)
        self.show_all()

    def on_clicked(self, widget):
        cdia = gtk.ColorSelectionDialog("Select color")
        response = cdia.run()

        if response == gtk.RESPONSE_OK:
		colorsel = cdia.colorsel
		color = colorsel.get_current_color()
                self.label.modify_fg(gtk.STATE_NORMAL, color)
        cdia.destroy()

PyApp()
gtk.main()
