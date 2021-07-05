
from gi.repository import Gtk

from . import sets
from . import draw
from . import point
from . import drawscroll
from . import pbox
from . import points

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
	sz=len(points.points)
	for i in range(0,sz):
		p=points.points.pop()
		p._remove_()
	if point.lastselect:
		pbox.close()

def clear():
	x=draw.cont.get_first_child()
	while x:
		y=x.get_next_sibling()
		draw.cont.remove(x)
		x=y
def redraw(w,h):
	clear()
	sz=len(points.points)
	for i in range (0,sz):
		if points.points[i]._offset_<draw.offset:
			continue
		for j in range(i,sz):
			if draw.offset+(w if drawscroll.landscape
				else h)<points.points[j]._offset_:
				return
			points.points[j]._put_(w,h)
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
	if point.lastselect and point.lastselect._drag_==True:
		point.lastselect._dend_(x,y)
		return
	point.struct(x,y)
