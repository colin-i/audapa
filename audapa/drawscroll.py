from gi.repository import Gtk

from . import draw
from . import r_offset

def calculate(n):
	w=win.get_width()
	h=win.get_height()
	d=draw.area
	if w>=h:
		#30000 maximum size of an X window
		if n>(size:=(w*2)):
			n=size
		if d.get_width()!=n or d.get_height()!=h:
			d.set_size_request(n,h)
			return True
	else:
		if n>(size:=(h*2)):
			n=size
		if d.get_width()!=w or d.get_height()!=n:
			d.set_size_request(w,n)
			return True
	return False

def edge(wn,pos,d):
	if pos==Gtk.PositionType.RIGHT:
		x=draw.offset+draw.size
		if x<draw.length:
			draw.offset+=win.get_width()
			r_offset.cged(win.get_hadjustment())
			draw.area.queue_draw()
	elif pos==Gtk.PositionType.BOTTOM:
		x=draw.offset+draw.size
		if x<draw.length:
			draw.offset+=win.get_height()
			r_offset.cged(win.get_vadjustment())
			draw.area.queue_draw()
	elif pos==Gtk.PositionType.LEFT:
		if draw.offset>0:
			draw.offset-=min(win.get_width(),draw.offset)#can be unfixed
			r_offset.cged(win.get_hadjustment())
			draw.area.queue_draw()
	else:
		if draw.offset>0:
			draw.offset-=min(win.get_height(),draw.offset)
			r_offset.cged(win.get_vadjustment())
			draw.area.queue_draw()

def init():
	global win
	win=Gtk.ScrolledWindow(vexpand=True)
	win.set_child(draw.init())
	win.connect('edge-overshot',edge,None)
	win.get_hadjustment().connect('value-changed',r_offset.cgd,None)
	win.get_vadjustment().connect('value-changed',r_offset.cgd,None)
