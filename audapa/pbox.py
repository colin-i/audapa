
from gi.repository import Gtk

from . import sets
from . import seloff
from . import forms
from . import point

def open(o,h):
	global box,info
	box=Gtk.Box(halign=Gtk.Align.CENTER)
	box.append(sets.colorButton(seloff.char_delete,delete,None))
	info=sets.colorLabel(inf(o,h))
	box.append(info)
	forms.button.get_parent().append(box)

def close():
	forms.button.get_parent().remove(box)

def delete(b,d):
	p=point.lastselect
	p._remove_()
	point.points.remove(p)
	p.get_parent().remove(p)
	close()
	point.lastselect=None

def inf(o,h):
	return str(o)+'|'+str(h)