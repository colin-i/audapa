
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
			self._height_=(sampsize*y/hstore)-(hstore*baseline)
		else:
			self._offset_=draw.offset+y
			self._height_=(sampsize*x/wstore)-(wstore*baseline)
		self._put_()
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
	def _put_():
		if drawscroll.landscape:
			y=_height_*hstore/sampsize
		else:
			y=_height_*hstore/sampsize
		draw.cont.put(self,self._offset_-draw.offset-const,y-const)