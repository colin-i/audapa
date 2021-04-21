
from gi.repository import Gtk

from . import sets

def init():
	b=Gtk.Box(homogeneous=True)
	t=sets.colorLabel("0")
	t.set_halign(Gtk.Align.START)
	b.append(t)
	t=sets.colorLabel("0")
	t.set_halign(Gtk.Align.END)
	b.append(t)
	return b
