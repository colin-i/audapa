
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
	pass
def right(b,d):
	pass