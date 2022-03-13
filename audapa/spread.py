
from gi.repository import Gtk

from . import sets
from . import points
from . import level

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
	a=spread.get_text()
	if a.isdigit():
		ps=points.points
		s=len(ps)
		if s>=2:
			b=int(a)
			n=ps[s-1]._offset_-ps[0]._offset_
			if compress.get_active():
				if b>n:
					spread.set_text(n.__str__(),-1)
					return
				#b=-b
			#apply()
			#save.apply()
			#move.saved(combo)
			#blank.saved()
			#return
		combo[0].set_child(combo[1])
		return
	level.not_a_digit(spread)

#def apply():
	#samples enlarge
	#sz=[i]-[i-1]
	#*b/total
	#[i]._offset_
	#rest.append()
	#rest_pos.append()
	#rest sort
	#rest sum/total
	#for i in range(0,)
	#[j]._offset_+=sign
	#samples compress
