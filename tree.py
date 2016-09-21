#! /usr/bin/python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_size_request(400, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        self.set_title("Tree")

        tree = gtk.TreeView()
        languages = gtk.TreeViewColumn()
        languages.set_title("Programming languages")

        cell = gtk.CellRendererText()
        languages.pack_start(cell, True)
        languages.add_attribute(cell, "text", 0)

        treestore = gtk.TreeStore(str)

        it = treestore.append(None, ["Scripting languages"])
        treestore.append(it, ["Python"])
        treestore.append(it, ["PHP"])
        treestore.append(it, ["Perl"])
        treestore.append(it, ["Ruby"])

        it=treestore.append(None, ["Compiling languages"])
        treestore.append(it, ["C"])
        treestore.append(it, ["C++"])
        treestore.append(it, ["C#"])
        treestore.append(it, ["Java"])

        tree.append_column(languages)
        tree.set_model(treestore)

        self.add(tree)
        self.show_all()

PyApp()
gtk.main()
