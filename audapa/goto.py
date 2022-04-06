
from gi.repository import Gtk

from . import info
from . import sets

def open(b,d):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx=Gtk.Box()
	cur,max=get_vals()
	bx.append(sets.colorLabel(cur.__str__()+" 0-"))
	x=max.__str__()
	maxlab=sets.colorLabel(x)
	bx.append(maxlab)
	buf=Gtk.EntryBuffer()
	bx.append(sets.colorEntry(buf))
	bx.append(sets.colorButton("Go",cancel,"Proceed",[max,buf]))
	box.append(bx)
	box.append(sets.colorButton("First",cancel,"Start"))
	box.append(sets.colorButton("Previous",cancel,"0" if cur==0 else (cur-1).__str__()))
	box.append(sets.colorButton("Next",cancel,x if cur==max else (cur+1).__str__(),max))
	box.append(sets.colorButton("Last",cancel,"End",max))
	box.append(sets.colorButton("Cancel",cancel,"Abort"))
	info.win.set_child(box)

def cancel(b,combo):
	info.win.set_child(info.box)

def get_vals():
	return (0,0)
