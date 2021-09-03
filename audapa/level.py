
from gi.repository import Gtk

from . import sets

def open(b,combo):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	en=sets.colorEntry()
	bt=sets.colorButton("Done",click,combo)
	box.append(en)
	box.append(bt)
	combo[0].set_child(box)

def click(b,combo):
	combo[0].set_child(combo[1])
