
from gi.repository import Gtk

from . import sets

spread=Gtk.EntryBuffer()

def open(b,combo):
	bx=Gtk.Grid(hexpand=True)
	bx.attach(sets.colorLabel("Spread by samples"),0,0,1,1)
	bx.attach(sets.colorEntry(spread),1,0,1,1)
	bx.attach(sets.colorLabel("Compress"),0,1,1,1) #Enlarge
	bx.attach(Gtk.CheckButton(),1,1,1,1)
	bx.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,2,2,1)
	bx.attach(sets.colorButton("Done",done,"Apply",combo),0,3,2,1)
	combo[0].set_child(bx)

def cancel(b,combo):
	combo[0].set_child(combo[1])

def done(b,combo):
	combo[0].set_child(combo[1])
