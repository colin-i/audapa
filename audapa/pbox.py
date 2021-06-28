
from gi.repository import Gtk

from . import sets
from . import seloff
from . import forms
from . import point

box=None

def open():
	global box
	box=Gtk.Box(halign=Gtk.Align.CENTER)
	box.append(sets.colorButton(seloff.char_delete,delete,None))
	box.append(sets.colorButton('&lt;',left,None))
	box.append(sets.colorButton('&gt;',right,None))
	forms.button.get_parent().append(box)

def close():
	global box
	if box:
		forms.button.get_parent().remove(box)
		box=None
		point.lastselect=None

def delete(b,d):
	p=point.lastselect
	p._remove_()
	point.points.remove(p)
	p.get_parent().remove(p)
	close()

def left(b,d):
	n=point.points.index(point.lastselect)
	if n==0:
		return
	inter(n-1,n)
def right(b,d):
	n=point.points.index(point.lastselect)
	if n+1==len(point.points):
		return
	inter(n+1,n+1)
def inter(n,m):
	a=point.points[n]
	s=point.lastselect
	p=point.struct()
	p._offset_=(s._offset_+a._offset_)/2
	p._height_=(s._height_+a._height_)/2
	p._put_fix_()
	point.points.insert(m,p)