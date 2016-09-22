#! /usr/bin/python

import gtk
import pango

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("System fonts")
        self.set_size_request(250,200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        context = self.create_pango_context()
        self.fam = context.list_families()

        store = self.create_model()

        treeView = gtk.TreeView(store)
        treeView.set_rules_hint(True)
        sw.add(treeView)

        self.create_column(treeView)
        self.add(sw)

        self.show_all()

    def create_column(self, treeView):
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("FontName", rendererText, text=0)
        column.set_sort_column_id(0)
        treeView.append_column(column)

    def create_model(self):
        store = gtk.ListStore(str)
        for ff in self.fam:
            store.append([ff.get_name()])
        return store

PyApp()
gtk.main()
