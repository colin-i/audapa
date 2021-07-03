
from gi.repository import Gtk,Gdk

from . import sets
from . import draw
from . import drawscroll
from . import pbox

const=6
points=[]

class struct(Gtk.DrawingArea):
	def __init__(self,x,y):
		Gtk.DrawingArea.__init__(self)
		self._control_ = Gtk.GestureClick()
		self._control_.connect("pressed",self._press_,None)
		self.add_controller(self._control_)
		self.set_size_request(2*const,2*const)
		#
		p=self._pos_(x,y)
		self._offset_=draw.offset+p[0]
		self._height_=p[1]
		self._put_(draw.wstore,draw.hstore)
		#
		self._control_.emit("pressed",0,0,0)
		for p in points:
			if self._offset_<p._offset_:
				points.insert(points.index(p),self)
				return
		points.append(self)
	def _pos_(self,x,y):
		if drawscroll.landscape:
			o=x
			h=draw.sampsize*y/draw.hstore
		else:
			o=y
			h=draw.sampsize*x/draw.wstore
		h-=draw.sampsize*draw.baseline
		return [int(o),int(h)]
	def _draw_none_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(sets.get_fgcolor2()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		cr.rectangle(0,0,width,height)
		cr.stroke()
	def _draw_cont_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(sets.get_fgcolor2()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		cr.rectangle(0,0,width,height)
		cr.fill()
	def _put_(self,w,h):
		c=self._coord_(w,h)
		draw.cont.put(self,c[0],c[1])
	def _coord_(self,w,h):
		z=self._offset_-draw.offset-const
		if drawscroll.landscape:
			y=self._height_*h/draw.sampsize
			y+=h*draw.baseline-const
			return [z,y]
		y=self._height_*w/draw.sampsize
		y+=w*draw.baseline-const
		return [y,z]
	def _press_(self,a,n,x,y,d):
		global lastselect
		if lastselect:
			lastselect.set_draw_func(lastselect._draw_none_,None,None)
			pbox.info._set_text_(pbox.inf(self._offset_,self._height_))
		else:
			pbox.open(self._offset_,self._height_)
		lastselect=self
		self.set_draw_func(self._draw_cont_,None,None)
	def _remove_(self):
		self.remove_controller(self._control_)
