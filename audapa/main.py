import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from . import sets
from . import record
from . import loop

def cl(b,d):
	d.stop(False)

sets.start()
win = Gtk.Window()
win.set_decorated(False)#such a heavy load here if True
win.maximize()
ready=0x1F399
win.show()
while loop.n:
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx=Gtk.Box()
	bx.append(sets.colorButton(chr(ready), record.start, ready))
	bx.append(sets.colorButton(chr(0x2699), sets.sets, [win,box]))
	bx.append(sets.colorButton("X", cl, loop))
	box.append(bx)
	box.append(Gtk.DrawingArea())
	win.set_child(box)
	loop.main.run()
