import pyaudio
import wave

from gi.repository import Gtk,Gdk

from . import sets

def draw_none(area,cr,width,height,d,d2):
	co=Gdk.RGBA()
	if co.parse(sets.get_color()):
		cr.set_source_rgb(co.red,co.green,co.blue)
	cr.set_line_width(0.5)#default 2.0; cairo scale is 1
	if width<height:
		x=width/2
		cr.move_to(x,0)
		cr.line_to(x,height)
	else:
		y=height/2
		cr.move_to(0,y)
		cr.line_to(width,y)
	cr.stroke()

area=Gtk.ScrolledWindow(vexpand=True)
draw=Gtk.DrawingArea()
draw.set_draw_func (draw_none,None,None)
area.set_child(draw)

formats={pyaudio.paInt16:'h',pyaudio.paUInt8:'B',pyaudio.paInt8:'b',
	pyaudio.paFloat32:'f',pyaudio.paInt32:'i'}

def prepare(format,sampwidth,channels,data,n):
	blockAlign=sampwidth*channels
	scan='<'+formats[format]*channels
	n*=blockAlign
	samples=[]
	for offset in range(0, n, blockAlign):
		samples.append(wave.struct.unpack(scan, data[offset:offset+blockAlign]))
