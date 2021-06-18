
from gi.repository import Gtk,Gdk

from . import sets
from . import draw

const=6
points=[]

class struct(Gtk.DrawingArea):
	def __init__(self,x,y):
		Gtk.DrawingArea.__init__(self)
		self.set_draw_func(self._draw_,None,None)
		self.set_size_request(2*const,2*const)
		draw.cont.put(self,x-const,y-const)
		#
		self._offset_=x
		for p in points:
			if x<p._offset_:
				points.insert(points.index(p),self)
				return
		points.append(self)
	def _draw_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(sets.get_fgcolor2()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		cr.rectangle(0,0,width,height)
		cr.stroke()
