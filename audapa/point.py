
from gi.repository import Gtk,Gdk

from . import sets
from . import draw
from . import drawscroll

const=6
points=[]

class struct(Gtk.DrawingArea):
	def __init__(self,x,y):
		Gtk.DrawingArea.__init__(self)
		self.set_draw_func(self._draw_,None,None)
		self.set_size_request(2*const,2*const)
		#
		if drawscroll.landscape:
			self._offset_=draw.offset+x
			self._height_=draw.sampsize*y/draw.hstore
		else:
			self._offset_=draw.offset+y
			self._height_=draw.sampsize*x/draw.wstore
		self._height_-=draw.sampsize*draw.baseline
		self._put_(draw.wstore,draw.hstore)
		for p in points:
			if self._offset_<p._offset_:
				points.insert(points.index(p),self)
				return
		points.append(self)
	def _draw_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(sets.get_fgcolor2()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		cr.rectangle(0,0,width,height)
		cr.stroke()
	def _put_(self,w,h):
		z=self._offset_-draw.offset-const
		if drawscroll.landscape:
			y=self._height_*h/draw.sampsize
			y+=h*draw.baseline-const
			draw.cont.put(self,z,y)
			return
		y=self._height_*w/draw.sampsize
		y+=w*draw.baseline-const
		draw.cont.put(self,y,z)