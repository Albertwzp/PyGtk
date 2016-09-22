#! /usr/bin/python

import gtk
import pango

lyrics = """Free means what, anyone get it ?
if soul can be free, does it move out body.
no one knows it, mybe one day you die it out.
liberty is easy sometime, but aways difficult for someone.

everyone bron with freedom, but we sell it to demon.
god take pity on us, but we betray.
now it time to judge, no one can escape.
"""

class Area(gtk.DrawingArea):
    def __init__(self):
        super(Area, self).__init__()
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 65535, 0))
        self.connect("expose_event", self.expose)

    def expose(self, widget, event):
        gc = self.get_style().fg_gc[gtk.STATE_NORMAL]
        font_desc = pango.FontDescription('Sans 10')

        layout = self.create_pango_layout(lyrics)
        width, height = self.get_size_request()

        attr = pango.AttrList()

        fg_color = pango.AttrForeground(60535, 60535, 60535, 0, -1)
        attr.insert(fg_color)

        layout.set_width(pango.SCALE * self.allocation.width)
        layout.set_spacing(pango.SCALE * 3)
        layout.set_alignment(pango.ALIGN_CENTER)
        layout.set_font_description(font_desc)
        layout.set_attributes(attr)

        self.window.draw_layout(gc, 0, 5, layout)

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("doomsday")
        self.set_size_request(300, 300)
        self.set_position(gtk.WIN_POS_CENTER)

        self.add(Area())
        self.connect("destroy", gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()
