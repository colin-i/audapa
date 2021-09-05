
from gi.repository import Gtk

from . import sets
from . import draw
from . import point
from . import drawscroll
from . import pbox
from . import points
from . import graph
from . import level
from . import save

#button
control=None
on=chr(0x25a1)

def init(combo):
	b=Gtk.Box(homogeneous=True)#,hexpand=True nothing
	global button,box
	box=Gtk.Box(halign=Gtk.Align.CENTER)
	button=sets.colorButton(on,toggle)#halign CENTER
	box.append(button)
	bt=sets.colorButton(chr(0x2021),level.open,combo)
	box.append(bt)
	bt=sets.colorButton(chr(0x1f5ab),save.data)
	box.append(bt)
	for bt in box:
		bt.set_sensitive(False)
	b.append(box)
	return b

def open():
	for b in box:
		b.set_sensitive(True)
	point.lastselect=None

def close():
	if control:
		button.emit(sets._click_)
	for b in box:
		b.set_sensitive(False)
	sz=len(points.points)
	for i in range(sz-1,-1,-1):
		points.points[i]._remove_(i)
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
			p=points.points[j]
			if draw.offset+(w if drawscroll.landscape
				 else h)<p._offset_:
				if i<j:
					graph.put(j,p,w,h)
				return
			p._put_(w,h,j)
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
	else:
		point.struct(x,y)
	graph.area.queue_draw()
