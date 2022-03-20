
from gi.repository import Gtk

from . import sets
from . import draw
from . import save
from . import delete
from . import level

def saved():
	draw.length=len(draw.samples)
	delete.changed() #this is not required in all cases but when adding without modifying draw(draw is big enough), will be required

start=Gtk.EntryBuffer(text="0")
stop=Gtk.EntryBuffer(text="0")

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
	a=start.get_text()
	b=stop.get_text()
	abool=a.isdigit()
	bbool=b.isdigit()
	if abool or bbool:
		if abool:
			c=int(a)
			draw.samples=([0]*c)+draw.samples
		if bbool:
			c=int(b)
			draw.samples+=[0]*c
		combo[0].set_child(combo[1])
		saved()
		save.saved()
		return
	if not abool:
		level.not_a_digit(start)
	if not bbool:
		level.not_a_digit(stop)
