
from gi.repository import Gtk

from . import sets
from . import bar
from . import draw

on='+'
off='-'
control=None

def init():
	global start,button
	b=Gtk.Box(homogeneous=True)
	start=sets.colorLabel("0")
	start.set_halign(Gtk.Align.START)
	b.append(start)
	t=sets.colorLabel("0")
	t.set_halign(Gtk.Align.END)
	b.append(t)
	return b

def press(g,n,x,y,d):
	start._set_text_(str(int(x)))

def open():
	global button
	button=sets.colorButton(on,toggle,draw.area)
	bar.box.append(button)
def close():
	if control:
		button.activate()
	bar.box.remove(button)

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
