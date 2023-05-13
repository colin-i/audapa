
from gi.repository import Gtk

from . import sets
from . import level
from . import play
from . import draw

default_toler="1"
toler=Gtk.EntryBuffer(text=default_toler)
default_mdist="1"
mdist=Gtk.EntryBuffer(text=default_mdist)

def open(b,combo):
	box=Gtk.Grid(hexpand=True)
	box.attach(sets.colorLabel("Tolerance"),0,0,1,1)
	box.attach(sets.colorEntry(toler),1,0,1,1)
	box.attach(sets.colorLabel("‰"),2,0,1,1)
	box.attach(sets.colorLabel("Min distance"),0,1,1,1)
	box.attach(sets.colorEntry(mdist),1,1,2,1)
	box.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,2,3,1)
	box.attach(sets.colorButton("Done",done,"Apply",combo),0,3,3,1)
	combo[0].set_child(box)

def cancel(b,combo):
	combo[0].set_child(combo[1])

def done(b,combo):
	a=toler.get_text()
	abool=a.isdigit()
	b=mdist.get_text()
	bbool=b.isdigit()
	if abool and bbool:
		a=int(a)
		b=int(b)
		if a>1000:
			toler.set_text("1000",-1)
		elif b==0:
			mdist.set_text("1",-1)
		else:
			a=pow(2,8*play.wavefile.getsampwidth())*a/1000;
			calculate(draw.samples,draw.length,int(a),b)
			combo[0].set_child(combo[1])
	else:
		if not abool:
			toler.set_text(default_toler,-1)
		if not bbool:
			mdist.set_text(default_mdist,-1)

def calculate(samples,length,tolerance,min_dist):
	pass
