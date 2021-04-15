from gi.repository import Gtk

from . import draw

win=Gtk.ScrolledWindow()
#size

def calculate(n):
	w=win.get_width()
	h=win.get_height()
	d=draw.area
	global size
	if w>=h:
		#30000 maximum size of an X window
		if n>(size:=(w*3)):
			n=size
		if d.get_width()!=n or d.get_height()!=h:
			d.set_size_request(n,h)
			return True
	else:
		if n>(size:=(h*3)):
			n=size
		if d.get_width()!=w or d.get_height()!=n:
			d.set_size_request(w,n)
			return True
	return False

def edge(wn,pos,d):
	if pos==Gtk.PositionType.RIGHT:
		x=draw.offset+draw.size
		if x<draw.length:
			draw.offset+=(size/2)-win.get_width()
			wn.get_vadjustment().set_value(size/2)
			draw.area.queue_draw()
	elif pos==Gtk.PositionType.BOTTOM:
		y=draw.offset+draw.size
		if y<draw.length:
			draw.offset+=(size/2)-win.get_height()
			wn.get_vadjustment().set_value(size/2)
			draw.area.queue_draw()
	elif pos==Gtk.PositionType.LEFT:
		if draw.offset>0:
			w=size/2
			if w>draw.offset:
				w=draw.offset
			draw.offset-=w
			wn.get_vadjustment().set_value(w)
			draw.area.queue_draw()
	else:
		if draw.offset>0:
			h=size/2
			if h>draw.offset:
				h=draw.offset
			draw.offset-=h
			wn.get_vadjustment().set_value(h)
			draw.area.queue_draw()
win.connect('edge-reached',edge,None)