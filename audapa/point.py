
from gi.repository import Gtk,Gdk

from . import sets
from . import draw

class struct(Gtk.DrawingArea):
	a=6
	def __init__(self,x,y):
		Gtk.DrawingArea.__init__(self)
		self.set_draw_func(self._draw_,None,None)
		self.set_size_request(2*self.a,2*self.a)
		draw.cont.put(self,x-self.a,y-self.a)
	def _draw_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(sets.get_fgcolor2()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		cr.rectangle(0,0,width,height)
		cr.stroke()
