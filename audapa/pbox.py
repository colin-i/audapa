
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
	p._remove_()
	points.points.remove(p)
	p.get_parent().remove(p)
	close()
	point.lastselect=None

def inf(o,h):
	return str(o)+' '+str(h)