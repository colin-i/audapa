
from gi.repository import Gtk

from . import draw
from . import sets
from . import seloff

def init():
	b=Gtk.Box(homogeneous=True)
	global atleft,atright
	atleft=sets.colorLabel("0")
	atleft.set_halign(Gtk.Align.START)
	atright=sets.colorLabel("0")
	atright.set_halign(Gtk.Align.END)
	b.append(atleft)
	b.append(seloff.init())
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