
from gi.repository import Gtk

from . import info
from . import sets

def open(b,d):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx=Gtk.Box()
	bx.append(sets.colorLabel("0-0"))
	bx.append(sets.colorEntry())
	bx.append(sets.colorButton("Go",cancel,"Proceed"))
	box.append(bx)
	box.append(sets.colorButton("First",cancel,"Start"))
	box.append(sets.colorButton("Last",cancel,"End"))
	box.append(sets.colorButton("Cancel",cancel,"Abort"))
	info.win.set_child(box)

def cancel(b,combo):
	info.win.set_child(info.box)
