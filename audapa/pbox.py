
from gi.repository import Gtk

from . import sets
from . import seloff
from . import forms
from . import point
from . import points
from . import draw
from . import graph

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
	ix=points.points.index(p)
	w=draw.wstore
	h=draw.hstore
	dels,puts=p._take_(ix,w,h)
	ix=and_inter(ix,dels,puts,w,h)
	graph.lines(dels,puts)
	p._remove_(ix)
	if p.get_parent():
		p.get_parent().remove(p)
	close()
	point.lastselect=None
	graph.area.queue_draw()
def and_inter(ix,dels,puts,w,h):
	pnts=points.points
	sz=len(pnts)
	if ix==0:
		if sz==1:
			return ix
		if and_inter_test(1):
			dels.append([dels[0][1],pnts[1]._coord_(w,h)])
	elif ix==(sz-1):
		if and_inter_test(sz-2):
			dels.append([pnts[sz-3]._coord_(w,h),dels[0][0]])
			ix-=1
	elif pnts[ix-1]._inter_:
		if and_inter_test(ix+1):
			aux=pnts[ix+1]._coord_(w,h)
			dels.append([dels[1][1],aux])
			puts[0][1]=aux
	return ix
def and_inter_test(test):
	p=points.points[test]
	b=p._inter_
	if b:
		p._remove_(test)
		if p.get_parent():
			p.get_parent().remove(p)
	return b

def inf(o,h):
	return str(o)+' '+str(h)