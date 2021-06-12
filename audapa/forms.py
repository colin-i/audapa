
from gi.repository import Gtk

from . import sets

def init():
	b=Gtk.Box(homogeneous=True)#,hexpand=True nothing
	bu=sets.colorButton(chr(0x25a1),tog,None)#25a0
	bu.set_sensitive(False)
	bu.set_halign(Gtk.Align.CENTER)
	b.append(bu)
	return b

def tog(b,d):
	pass