
from gi.repository import Gtk

from . import sets
from . import bar
from . import draw

on='+'
off='-'
control=None

def init():
	global start,end
	b=Gtk.Box(homogeneous=True)
	start=sets.colorLabel("0")
	start.set_halign(Gtk.Align.START)
	b.append(start)
	end=sets.colorLabel("0")
	end.set_halign(Gtk.Align.END)
	b.append(end)
	return b

def press(g,n,x,y,d):
	start._set_text_(str(int(x)))

def open():
	button=sets.colorButton(on,toggle,draw.area)
	bar.box.append(button)
	stop=sets.colorButton("x",close,button)
	bar.box.append(stop)
def close(s,b):
	if control:
		b.activate()
	bar.box.remove(b)
	bar.box.remove(s)
	start._set_text_("0")
	end._set_text_("0")
	draw.close()

def toggle(b,a):
	global control
	if control:
		a.remove_controller(control)
		control=None
		b._set_text_(on)
	else:
		control = Gtk.GestureClick()
		control.connect("pressed",press,None)
		a.add_controller(control)
		b._set_text_(off)
