
from gi.repository import Gtk

from . import play
from . import sets

#win,box

def open(b,d):
	bx=Gtk.Grid(hexpand=True)
	nchannels, sampwidth, framerate, nframes, comptype, compname = play.wavefile.getparams()
	add("nchannels",nchannels)
	add("sampwidth",sampwidth)
	add("framerate",framerate)
	add("nframes",nframes)
	add("comptype",comptype)
	add("compname",compname)
	bx.attach(sets.colorButton("Done",done,"Back"),0,0,1,1)
	win.set_child(bx)

def add(n,v):
	pass

def done(b,d):
	win.set_child(box)
