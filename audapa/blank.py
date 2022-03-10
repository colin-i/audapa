
from gi.repository import Gtk

from . import sets

start=Gtk.EntryBuffer()
stop=Gtk.EntryBuffer()

def open(b,combo):
	bx=Gtk.Grid(hexpand=True)
	bx.attach(sets.colorLabel("Blank samples at start"),0,0,1,1)
	bx.attach(sets.colorEntry(start),1,0,1,1)
	bx.attach(sets.colorLabel("Blank samples at end"),0,1,1,1)
	bx.attach(sets.colorEntry(stop),1,1,1,1)
	bx.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,2,2,1)
	bx.attach(sets.colorButton("Done",done,"Apply",combo),0,3,2,1)
	combo[0].set_child(bx)

def cancel(b,combo):
	combo[0].set_child(combo[1])

def done(b,combo):
	combo[0].set_child(combo[1])
