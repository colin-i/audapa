
from gi.repository import Gtk

from . import draw
from . import sets

def init():
	b=Gtk.Box()
	global atleft,atright
	atleft=sets.colorLabel("0")
	atright=sets.colorLabel("0")
	atright.set_halign(Gtk.Align.END)
	atright.set_hexpand(True)
	b.append(atleft)
	b.append(atright)
	return b

def cnged(a,visible):
	l=draw.offset+int(a.get_value())
	atleft._set_text_(str(l))
	r=max(draw.length-visible-l,0)
	atright._set_text_(str(r))
def cged(a):
	cnged(a,int(a.get_page_size()))
def cgd(a,d):
	cged(a)