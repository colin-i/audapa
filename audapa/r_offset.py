
from gi.repository import Gtk

from . import draw
from . import sets

def init():
	b=Gtk.Box()
	global text,total
	text=sets.colorLabel("0")
	total=sets.colorLabel("0")
	total.set_halign(Gtk.Align.END)
	total.set_hexpand(True)
	b.append(text)
	b.append(total)
	return b 

def cgd(a,d):
	text._set_text_(str(draw.offset+int(a.get_value())))
