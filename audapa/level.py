
from gi.repository import Gtk

from . import sets
from . import draw

dif=Gtk.EntryBuffer()

def open(b,combo):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	#+/- button or not   entry   maxim
	b2=Gtk.Box()
	if draw.baseline!=0:
		s=sets.colorButton("+",sign,"Sign")
		b2.append(s)
	en=sets.colorEntry(dif)
	b2.append(en)
	box.append(b2)
	#atstart   middle   - or calculated
	#Calculate
	#Cancel
	bt=sets.colorButton("Done",click,"Return",combo)
	box.append(bt)
	combo[0].set_child(box)

def click(b,combo):
	combo[0].set_child(combo[1])

def sign(b,d):
	pass