
from gi.repository import Gtk

class struct(Gtk.DrawingArea):
	def __init__(self):
		Gtk.DrawingArea.__init__(self)
		self.set_draw_func(self._draw_,None,None)
		self.set_size_request(10,10)
	def _draw_(self,widget,cr,width,height,d,u):
		cr.rectangle(0,0,width,height)
		cr.fill()