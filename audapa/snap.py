
from . import point
from . import draw
from . import graph


def autodrag(p,x,y):
	p._dend_(x,y)
	graph.area.queue_draw()

def base(b,d):
	p=point.lastselect
	hg=p._height_
	p._height_=0
	x,y=p._coord_(draw.wstore,draw.hstore)
	p._height_=hg
	autodrag(p,x,y)

def left(b,d):
	pass

def right(b,d):
	pass

def top(b,d):
	pass

def bottom(b,d):
	pass
