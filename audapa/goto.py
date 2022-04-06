
from gi.repository import Gtk

from . import info
from . import sets

def open(b,d):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx=Gtk.Box()
	bx.append(sets.colorLabel("0-"))
	x=get_max()
	max=sets.colorLabel(x.__str__())
	bx.append(max)
	buf=Gtk.EntryBuffer()
	bx.append(sets.colorEntry(buf))
	bx.append(sets.colorButton("Go",cancel,"Proceed",[max,buf]))
	box.append(bx)
	box.append(sets.colorButton("First",cancel,"Start"))
	box.append(sets.colorButton("Last",cancel,"End",max))
	box.append(sets.colorButton("Cancel",cancel,"Abort"))
	info.win.set_child(box)

def cancel(b,combo):
	info.win.set_child(info.box)

def get_max():
	return 0
