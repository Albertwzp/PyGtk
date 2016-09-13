#! /usr/bin/python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Calendar")
        self.set_size_request(300, 270)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(2)

        self.label = gtk.Label(". . .")

        calendar = gtk.Calendar()
        calendar.connect("day_selected", self.on_day_selected)

        fix = gtk.Fixed()
        fix.put(calendar, 20, 20)
        fix.put(self.label, 40, 230)
        self.add(fix)
    
        self.connect("destroy", gtk.main_quit)
        self.show_all()

    def on_day_selected(self, widget):
        (year, month, day) = widget.get_date()
        self.label.set_label(str(month) + "/" + str(day) + "/" + str(year))

PyApp()
gtk.main()
