
from gi.repository import Gtk

from . import sets
from . import seloff
from . import forms

box=None

def open():
	global box
	box=Gtk.Box(halign=Gtk.Align.CENTER)
	box.append(sets.colorButton(seloff.char_delete,toggle,None))
	forms.button.get_parent().append(box)

def close():
	if box:
		forms.button.get_parent().remove(box)

def toggle(b,d):
	pass