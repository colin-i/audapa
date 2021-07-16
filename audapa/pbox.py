
from gi.repository import Gtk

from . import sets
from . import seloff
from . import forms
from . import point
from . import points

def open(o,h):
	global box,info
	box=Gtk.Box()
	box.append(sets.colorButton(seloff.char_delete,delete,None))
	info=sets.colorLabel(inf(o,h))
	info.set_hexpand(True)
	info.set_halign(Gtk.Align.END)
	box.append(info)
	forms.button.get_parent().append(box)

def close():
	forms.button.get_parent().remove(box)

def delete(b,d):
	p=point.lastselect
	ix=and_inter(points.points.index(p))
	p._remove_(ix)
	p.get_parent().remove(p)
	close()
	point.lastselect=None
def and_inter(ix):
	pnts=points.points
	sz=len(pnts)
	gap=0
	if ix==0:
		if sz==1:
			return ix
		test=1
	elif ix==(sz-1):
		test=sz-2
		gap=1
	elif pnts[ix-1]._inter_:
		test=ix+1
	else:
		return ix
	p=pnts[test]
	if p._inter_==False:
		return ix
	p._remove_(test)
	if p.get_parent():
		p.get_parent().remove(p)
	return ix-gap

def inf(o,h):
	return str(o)+' '+str(h)