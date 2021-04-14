import pyaudio
import wave

from gi.repository import Gtk,Gdk

from . import sets

samples=[]

def draw_none(area,cr,width,height,signedrate,d):
	co=Gdk.RGBA()
	if co.parse(sets.get_color()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	cr.set_line_width(0.5)#default 2.0; cairo scale is 1
	n=len(samples)
	if width>=height:
		y=height/2
		if n:
			painthor(cr,n,y,height/signedrate)
		else:
			cr.move_to(0,y)
			cr.line_to(width,y)
	else:
		x=width/2
		if n:
			paintver(cr,n,x,width/signedrate)
		else:
			cr.move_to(x,0)
			cr.line_to(x,height)
	cr.stroke()

area=Gtk.ScrolledWindow(vexpand=True)
draw=Gtk.DrawingArea()
draw.set_draw_func (draw_none,None,None)
area.set_child(draw)

formats={pyaudio.paInt16:'h',pyaudio.paUInt8:'B',pyaudio.paInt8:'b',
	pyaudio.paFloat32:'f',pyaudio.paInt32:'i'}

def prepare(format,sampwidth,channels,data,n,rate):
	blockAlign=sampwidth*channels
	fm=formats[format]
	scan='<'+fm*channels
	n*=blockAlign
	global samples
	samples=[]
	for offset in range(0, n, blockAlign):
		s=wave.struct.unpack(scan, data[offset:offset+blockAlign])
		samples.append(s)
	draw.set_draw_func (draw_none,rate / (2 if fm.islower() else 1),None)
	draw.queue_draw()

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