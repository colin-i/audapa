
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
	mx=sets.colorLabel("0")
	b2.append(mx)
	box.append(b2)
	#atstart   middle[-1,1]   - or calculated
	st=sets.colorLabel("0")
	md=sets.colorLabel("0")
	cal=sets.colorLabel("0")
	b3=Gtk.Box()
	b3.append(st)
	b3.append(md)
	b3.append(cal)
	box.append(b3)
	#Calculate
	calc=sets.colorButton("Calculate",calcs,"Test")
	box.append(calc)
	#Cancel
	exit=sets.colorButton("Cancel",abort,"Abort")
	box.append(exit)
	bt=sets.colorButton("Done",click,"Apply",combo)
	box.append(bt)
	combo[0].set_child(box)

def click(b,combo):
	combo[0].set_child(combo[1])

def sign(b,d):
	pass

def calcs(b,d):
	pass

def abort(b,d):
	pass
