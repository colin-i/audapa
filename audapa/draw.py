import pyaudio
import wave

from gi.repository import Gtk,Gdk

from . import sets
from . import drawscroll
from . import play

#area

offset=0
#length

#samples
#size

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
	n=length-offset
	if drawscroll.calculate(n):
		return
	co=Gdk.RGBA()
	if co.parse(sets.get_color()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	cr.set_line_width(0.5)
	global size
	if width>=height:
		y=height/2
		size=min(width,n)
		painthor(cr,y,height/signedsampsize)
	else:
		x=width/2
		size=min(height,n)
		paintver(cr,x,width/signedsampsize)
	cr.stroke()

def init():
	global area
	area=Gtk.DrawingArea()
	area.set_draw_func (draw_none,None,None)
	return area
def close():
	global offset,length
	offset=0
	length=0
	area.set_draw_func (draw_none,None,None)
	drawscroll.calculate(0)
	play.stop()

formats={pyaudio.paInt16:'h',pyaudio.paUInt8:'B',pyaudio.paInt8:'b',
	pyaudio.paFloat32:'f',pyaudio.paInt32:'i'}

def prepare(format,sampwidth,channels,data):
	blockAlign=sampwidth*channels
	fm=formats[format]
	scan='<'+fm*channels
	tot=length*blockAlign
	global samples
	samples=[]
	for i in range(0, tot, blockAlign):
		s=wave.struct.unpack(scan, data[i:i+blockAlign])
		samples.append(s)
	p=8*sampwidth
	if fm.islower():
		p-=1
	area.set_draw_func (draw_cont,2**p,None)
	drawscroll.calculate(length)

def painthor(cr,y,ratio):
	for i in range(0,size):
		cr.move_to(i,y)
		z=samples[i][0]
		r=ratio*z+y
		cr.line_to(i,r)
def paintver(cr,x,ratio):
	for i in range(0,size):
		cr.move_to(x,i)
		z=samples[i][0]
		c=ratio*z+x
		cr.line_to(c,i)
