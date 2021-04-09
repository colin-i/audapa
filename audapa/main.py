import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

from . import sets
from . import record

def cl(b,data):
	data.quit()

sets.start()
win = Gtk.Window()
win.set_decorated(False)#such a heavy load here if True
win.maximize()
box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
bx=Gtk.Box()
ready=0x1F399
b=Gtk.Button.new_with_label(chr(ready))
b.connect('clicked', record.start, ready)
bx.append(b)
b=Gtk.Button.new_with_label(chr(0x2699))
b.connect('clicked', sets.sets, [win,box])
bx.append(b)
b=Gtk.Button.new_with_label("X")
mainloop = GLib.MainLoop()
b.connect('clicked', cl, mainloop)
bx.append(b)
box.append(bx)
box.append(Gtk.DrawingArea())
win.set_child(box)
win.show()
mainloop.run()
