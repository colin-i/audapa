import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

from . import sets

def cl(b,data):
	data.quit()

sets.start()
win = Gtk.Window()
win.set_decorated(False)#such a heavy load here if True
win.maximize()
box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
bx=Gtk.Box()
b=Gtk.Button.new_with_label(chr(0x2699))
b.connect('clicked', sets.sets, [win,box])
bx.append(b)
mainloop = GLib.MainLoop()
b=Gtk.Button.new_with_label("X")
b.connect('clicked', cl, mainloop)
bx.append(b)
box.append(bx)
box.append(Gtk.DrawingArea())
win.set_child(box)
win.show()
mainloop.run()
