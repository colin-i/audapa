
from gi.repository import Gtk,Gdk,GLib

from . import sets
from . import draw
from . import drawscroll
from . import pbox
from . import points
from . import graph

const=6

class struct(Gtk.DrawingArea):
	_drag_=False
	_inter_=False
	def __init__(self,*args):
		Gtk.DrawingArea.__init__(self)
		self._control_ = Gtk.GestureClick()
		self._control_.connect("pressed",self._press_,None)
		self.add_controller(self._control_)
		self.set_size_request(2*const,2*const)
		if len(args)==0:
			self.set_draw_func(self._draw_none_,None,None)
			return
		self._pos_(args[0],args[1])
		ix=points.insert(self)
		self._put_(draw.wstore,draw.hstore,ix)
		self._control_.emit("pressed",0,0,0)
	def _pos_(self,x,y):
		if drawscroll.landscape:
			o=x
			h=draw.sampsize*y/draw.hstore
		else:
			o=y
			h=draw.sampsize*x/draw.wstore
		self._offset_=int(draw.offset+o)
		self._height_=int(h-(draw.sampsize*draw.baseline))
	def _color_(self):
		if self._inter_==False:
			return sets.get_fgcolor2()
		return sets.get_fgcolor3()
	def _draw_none_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(self._color_()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		cr.rectangle(0,0,width,height)
		cr.stroke()
	def _draw_cont_(self,widget,cr,width,height,d,u):
		co=Gdk.RGBA()
		if co.parse(self._color_()):
			cr.set_source_rgb(co.red,co.green,co.blue)
		if self._drag_:
			cr.arc(const,const,const,0,2*GLib.PI)
		else:
			cr.rectangle(0,0,width,height)
		cr.fill()
	def _put_(self,w,h,ix):
		c=self._coord_(w,h)
		graph.put(ix,c,w,h)
		draw.cont.put(self,c[0]-const,c[1]-const)
	def _coord_(self,w,h):
		z=self._offset_-draw.offset
		if drawscroll.landscape:
			y=self._height_*h/draw.sampsize
			y+=h*draw.baseline
			return [z,y]
		y=self._height_*w/draw.sampsize
		y+=w*draw.baseline
		return [y,z]
	def _press_(self,a,n,x,y,d):
		global lastselect
		if lastselect:
			if lastselect!=self:
				lastselect.set_draw_func(lastselect._draw_none_,None,None)
				pbox.info._set_text_(pbox.inf(self._offset_,self._height_))
			else:
				if self._drag_==False:
					self._drag_=True
				else:
					self._drag_=False
				self.queue_draw()
				return
		else:
			pbox.open(self._offset_,self._height_)
		lastselect=self
		self.set_draw_func(self._draw_cont_,None,None)
	def _dend_(self,x,y):
		ini=points.points.index(self)
		w=draw.wstore
		h=draw.hstore
		dels=graph.take(ini,self._coord_(w,h),w,h)
		#
		o=self._offset_
		self._pos_(x,y)
		ix=points.move(self,o,ini)
		c=self._coord_(w,h)
		graph.put(ix,c,w,h,dels)
		draw.cont.move(self,c[0]-const,c[1]-const)
		pbox.info._set_text_(pbox.inf(self._offset_,self._height_))
	def _remove_(self,ix):
		self.remove_controller(self._control_)
		del points.points[ix]
