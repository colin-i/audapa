import pyaudio
import wave

from gi.repository import Gtk,Gdk
import cairo

from . import sets
from . import drawscroll
from . import play
from . import seloff
from . import forms

#area,cont
offset=0
#length
#samples
#size

#sampsize,baseline,surface,ostore,wstore,hstore

def draw_none(widget,cr,width,height,d,u):
	co=Gdk.RGBA()
	if co.parse(sets.get_color()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	cr.set_line_width(0.5)#default 2.0; cairo scale is 1
	if width>=height:
		y=height/2
		cr.move_to(0,y)
		cr.line_to(width,y)
	else:
		x=width/2
		cr.move_to(x,0)
		cr.line_to(x,height)
	cr.stroke()
def draw_cont(widget,cr,width,height,d,d2):
	n=length-offset
	if drawscroll.calculate(n):
		return
	global ostore,wstore,hstore
	if ostore!=offset or wstore!=width or hstore!=height:
		global size
		ostore=offset
		wstore=width
		hstore=height
		size=min(width,n) if drawscroll.landscape else min(height,n)
		unsel(offset,offset+size)
		draw_sel()
	cr.set_source_surface (surface, 0, 0)
	cr.paint ()
def draw_sel():
	start=seloff.start._get_()
	end=seloff.end._get_()
	if start<(offset+size) and end>offset:
		sel(max(start,offset),min(end,offset+size))
def redraw():
	forms.redraw(wstore,hstore)
	global surface
	surface = area.get_native().get_surface().create_similar_surface(cairo.Content.COLOR,wstore,hstore)
	area.queue_draw()

def init():
	global area,cont
	area=Gtk.DrawingArea()
	area.set_draw_func (draw_none,None,None)
	over=Gtk.Overlay()
	over.set_child(area)
	cont=Gtk.Fixed()#fixed is not tracking window default-width
	over.add_overlay(cont)
	return over
def close():
	global offset,length#for r_offset
	offset=0
	length=0
	area.disconnect(res_id)
	area.set_draw_func (draw_none,None,None)
	drawscroll.calculate(0)
	play.stop()
def open(format,sampwidth,channels,data):
	blockAlign=sampwidth*channels
	scan,fm=play.scan(sampwidth,channels)
	tot=length*blockAlign
	global samples
	samples=[]
	for i in range(0, tot, blockAlign):
		s=wave.struct.unpack(scan, data[i:i+blockAlign])
		samples.append(s)
	global ostore,wstore,hstore,sampsize,baseline
	ostore=-1
	#wstore=-1 one flag is enaugh
	#hstore=-1
	sampsize=2**(8*sampwidth)
	baseline=(1/2) if fm.islower() else 0
	global res_id
	res_id=area.connect_after ("resize", resize_cb, None)
	area.set_draw_func (draw_cont,None,None)
	drawscroll.set_landscape()
	drawscroll.calculate(length)

def resize_cb(a,w,h,d):
	drawscroll.set_landscape()
	forms.redraw(w,h)
	global surface
	surface = a.get_native().get_surface().create_similar_surface(cairo.Content.COLOR,w,h)

def paintland(cr,y,ratio,a,b):
	for i in range(a,b):
		j=i-offset
		cr.move_to(j,y)
		z=samples[i][0]
		r=ratio*z+y
		cr.line_to(j,r)
def paintport(cr,x,ratio,a,b):
	for i in range(a,b):
		j=i-offset
		cr.move_to(x,j)
		z=samples[i][0]
		c=ratio*z+x
		cr.line_to(c,j)
def sel(a,b):
	paint(a,b,sets.get_fgcolor())
def unsel(a,b):
	paint(a,b,sets.get_color())
def paint(a,b,clr):
	cr=cairo.Context(surface)
	cr.set_line_width(0.5)#this at start?nothing
	co=Gdk.RGBA()
	if co.parse(clr):
		cr.set_source_rgb(co.red,co.green,co.blue)
	if drawscroll.landscape:
		paintland(cr,hstore*baseline,hstore/sampsize,a,b)
	else:
		paintport(cr,wstore*baseline,wstore/sampsize,a,b)
	cr.stroke()
