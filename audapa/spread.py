
from gi.repository import Gtk

from . import sets
from . import points

spread=Gtk.EntryBuffer()
compress=Gtk.CheckButton()

def open(b,combo):
	bx=Gtk.Grid(hexpand=True)
	bx.attach(sets.colorLabel("Spread/Compress N samples"),0,0,1,1)
	bx.attach(sets.colorEntry(spread),1,0,1,1)
	bx.attach(sets.colorLabel("Compress"),0,1,1,1) #Enlarge
	bx.attach(compress,1,1,1,1)
	bx.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,2,2,1)
	bx.attach(sets.colorButton("Done",done,"Apply",combo),0,3,2,1)
	combo[0].set_child(bx)

def cancel(b,combo):
	combo[0].set_child(combo[1])

def done(b,combo):
	combo[0].set_child(combo[1])
	ps=points.points
	s=len(ps)
	if s>=2:
		a=spread.get_text()
		if a.isdigit():
			b=int(a)
			n=p[s-1]._offset_-p[0]._offset_
			if compress.get_active():
				b=b if b<n else n
