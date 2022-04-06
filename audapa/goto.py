
from gi.repository import Gtk

from . import info
from . import sets

def open(b,d):
	bx=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx.append(sets.colorButton("Cancel",cancel,"Abort"))
	info.win.set_child(bx)

def cancel(b,combo):
	info.win.set_child(info.box)
