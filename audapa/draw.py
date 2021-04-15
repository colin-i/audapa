import pyaudio
import wave

from gi.repository import Gtk,Gdk

from . import sets

samples=[]

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
def draw_cont(widget,cr,width,height,signedsampsize,d):
	n=len(samples)
	if calculate(n):
		return
	co=Gdk.RGBA()
	if co.parse(sets.get_color()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	cr.set_line_width(0.5)
	if width>=height:
		y=height/2
		painthor(cr,width,y,height/signedsampsize)
	else:
		x=width/2
		paintver(cr,height,x,width/signedsampsize)
	cr.stroke()

area=Gtk.ScrolledWindow()
draw=Gtk.DrawingArea()
draw.set_draw_func (draw_none,None,None)
area.set_child(draw)

formats={pyaudio.paInt16:'h',pyaudio.paUInt8:'B',pyaudio.paInt8:'b',
	pyaudio.paFloat32:'f',pyaudio.paInt32:'i'}

def prepare(format,sampwidth,channels,data,n):
	blockAlign=sampwidth*channels
	fm=formats[format]
	scan='<'+fm*channels
	tot=n*blockAlign
	global samples
	samples=[]
	for offset in range(0, tot, blockAlign):
		s=wave.struct.unpack(scan, data[offset:offset+blockAlign])
		samples.append(s)
	p=8*sampwidth
	if fm.islower():
		p-=1
	draw.set_draw_func (draw_cont,2**p,None)
	calculate(n)#switching files

def painthor(cr,n,y,ratio):
	for i in range(0,n):
		cr.move_to(i,y)
		z=samples[i][0]
		r=ratio*z+y
		cr.line_to(i,r)
def paintver(cr,n,x,ratio):
	for i in range(0,n):
		cr.move_to(x,i)
		z=samples[i][0]
		c=ratio*z+x
		cr.line_to(c,i)

def calculate(n):
	w=area.get_width()
	h=area.get_height()
	if w>=h:
		if n<w:
			n=w
		#30000 maximum size of an X window
		elif n>(mx:=(w*2)):
			n=mx
		if draw.get_width()!=n or draw.get_height()!=h:
			draw.set_size_request(n,h)
			return True
	else:
		if n<h:
			n=h
		elif n>(mx:=(h*2)):
			n=mx
		if draw.get_width()!=w or draw.get_height()!=n:
			draw.set_size_request(w,n)
			return True
	return False