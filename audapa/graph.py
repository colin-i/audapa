
from gi.repository import Gtk,Gdk
import cairo
import math

from . import points
from . import sets
from . import point
from . import drawscroll

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
	line_draw(cr,c0,c1)
def line_draw(cr,c0,c1):
	#don't let line width corners to intersect
	p0,p1,r=coords(cr,c0[0],c0[1],c1[0],c1[1])
	cr.move_to(p0[0],p0[1])
	cr.line_to(p1[0],p1[1])
	cr.stroke()
def coords(cr,x0,y0,x1,y1,extra=0):
	x=x1-x0
	y=y1-y0
	l=point.const-extra
	if drawscroll.landscape:
		t=y/x if x else math.inf
		r=math.atan(t)
		x=math.cos(r)*l
		y=math.sin(r)*l
	else:
		t=x/y if y else math.inf
		r=math.atan(t)
		x=math.sin(r)*l
		y=math.cos(r)*l
	return ([x0+x,y0+y],[x1-x,y1-y],r)
def lines(dels,puts):
	cr=cairo.Context(surface)
	cr.save()
	cr.set_operator(cairo.Operator.CLEAR)
	for d in dels:
		clearline(cr,d[0],d[1])
	cr.restore()
	co=Gdk.RGBA()
	if co.parse(sets.get_fgcolor2()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	for p in puts:
		line_draw(cr,p[0],p[1])
def xy_r(h,r):
	if drawscroll.landscape:
		return (math.sin(r)*h,math.cos(r)*h)
	return (math.cos(r)*h,math.sin(r)*h)

def take(ix,pnt,w,h):
	sz=len(points.points)
	if ix>0:
		c1=pnt._coord_(w,h)
		d=[[points.points[ix-1]._coord_(w,h),c1]]
		if ix+1<sz:
			d.append([c1,points.points[ix+1]._coord_(w,h)])
		return d
	elif sz>1:
		c1=pnt._coord_(w,h)
		c0=points.points[1]._coord_(w,h)
		return [[c1,c0]]
	return None
def clearline(cr,c0,c1):
	p0,p1,r=coords(cr,c0[0],c0[1],c1[0],c1[1],1)   #it's tested
	h=cr.get_line_width()/2+1   #it's tested
	x,y=xy_r(h,r)
	cr.move_to(p0[0]-x,p0[1]+y)
	cr.line_to(p0[0]+x,p0[1]-y)
	cr.line_to(p1[0]+x,p1[1]-y)
	cr.line_to(p1[0]-x,p1[1]+y)
	cr.line_to(p0[0]-x,p0[1]+y)
	cr.fill()
