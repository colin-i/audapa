
from gi.repository import Gtk

from . import sets
from . import draw
from . import point
from . import drawscroll
from . import pbox

#button
control=None
on=chr(0x25a1)

def init():
	b=Gtk.Box(homogeneous=True)#,hexpand=True nothing
	global button
	button=sets.colorButton(on,toggle,None)
	button.set_sensitive(False)
	button.set_halign(Gtk.Align.CENTER)
	b.append(button)
	return b

def open():
	button.set_sensitive(True)
	point.lastselect=None

def close():
	if control:
		button.emit(sets._click_)
	button.set_sensitive(False)
	sz=len(point.points)
	for i in range(0,sz):
		p=point.points.pop()
		p._remove_()
	pbox.close()

def clear():
	x=draw.cont.get_first_child()
	while x:
		y=x.get_next_sibling()
		draw.cont.remove(x)
		x=y
def redraw(w,h):
	clear()
	sz=len(point.points)
	for i in range (0,sz):
		if point.points[i]._offset_<draw.offset:
			continue
		for j in range(i,sz):
			if draw.offset+(w if drawscroll.landscape
				else h)<point.points[j]._offset_:
				return
			point.points[j]._put_(w,h)
		return

def toggle(b,a):
	a=draw.cont
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
