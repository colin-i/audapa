
from gi.repository import Gtk

from . import sets
from . import draw
from . import point

#button
control=None
on=chr(0x25a1)

def init():
	b=Gtk.Box(homogeneous=True)#,hexpand=True nothing
	global button
	button=sets.colorButton(on,toggle,draw.cont)
	button.set_sensitive(False)
	button.set_halign(Gtk.Align.CENTER)
	b.append(button)
	return b

def open():
	button.set_sensitive(True)

def close():
	if control:
		button.emit(sets._click_)
	button.set_sensitive(False)
	clear()
	point.points.clear()

def clear():
	x=draw.cont.get_first_child()
	while x:
		y=x.get_next_sibling()
		draw.cont.remove(x)
		x=y
def redraw():
	clear()
	for i in range (0,points.length):
		if draw.offset<points[i]._offset_:
			continue
		for j in range(i,points.length):
			if draw.offset+draw.length<points[j]._offset_:
				break
			points[j]._put_()
		break

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
		b._set_text_(chr(0x25a0))

def press(g,n,x,y,d):
	point.struct(x,y)
