#! /usr/bin/python
import gtk
class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

	self.set_title("Buttons_Tooltips")
        self.connect("destroy", gtk.main_quit)
        self.set_size_request(250,150)
        self.set_position(gtk.WIN_POS_CENTER)
	self.set_tooltip_text("Window widget")

	btn1 = gtk.Button("First")
	btn1.set_sensitive(False)
	btn2 = gtk.Button("Second")
	btn2.set_tooltip_text("Button widget")
	btn3 = gtk.Button(stock=gtk.STOCK_CLOSE)
	btn4 = gtk.Button("Fourth")
	btn4.set_size_request(80,40)

	fixed = gtk.Fixed()
	
	fixed.put(btn1, 20, 30)
	fixed.put(btn2, 100, 30)
	fixed.put(btn3, 20, 80)
	fixed.put(btn4, 100, 80)

	self.add(fixed)
        self.show_all()
PyApp()
gtk.main()
