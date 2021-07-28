
from gi.repository import Gtk,Gdk
import cairo
import math

from . import points
from . import sets

def open(ovr):
	global area
	area=Gtk.DrawingArea()
	area.set_draw_func(draw_cont,None,None)
	ovr.add_overlay(area)
def close(ovr):
	ovr.remove_overlay(area)
def draw_cont(widget,cr,width,height,d,d2):
	cr.set_source_surface(surface, 0, 0)
	cr.paint()
def surf(w,h):
	global surface
	surface = area.get_native().get_surface().create_similar_surface(cairo.Content.COLOR_ALPHA,w,h)

def put(ix,c1,w,h):
	if ix>0:
		c0=points.points[ix-1]._coord_(w,h)
		line(c0,c1)
	elif len(points.points)>1:
		c0=points.points[1]._coord_(w,h)
		line(c1,c0)
def line(c0,c1):
	cr=cairo.Context(surface)
	co=Gdk.RGBA()
	if co.parse(sets.get_fgcolor2()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	#don't let line width corners to intersect
	p0,p1=coords(cr,c0[0],c0[1],c1[0],c1[1])
	cr.move_to(p0[0],p0[1])
	cr.line_to(p1[0],p1[1])
	cr.stroke()
def coords(cr,x0,y0,x1,y1):
	x=x1-x0
	y=y1-y0
	l=cr.get_line_width()
	t=x/y
	r=math.atan(t)
	x=math.sin(r)*l
	y=math.cos(r)*l
	return ([x0+x,y0+y],[x1-x,y1-y])
