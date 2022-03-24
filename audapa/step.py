
from . import point
from . import points
from . import draw
from . import drawscroll

def left(b,d):
	p=point.lastselect
	ix=points.points.index(p)
	if ix!=0:
		x,y=draw.cont.get_child_position(draw.cont.get_prev_child(p))
		if drawscroll.landscape:
			limit=x
		else:
			limit=y
	else:
		limit=0

def right(b,d):
	p=point.lastselect
	ix=points.points.index(p)
	if x+1==len(points.points) or points.points[x+1]._offset_>(draw.offset+draw.size):
		limit==draw.size
	else:
		limit=points.points[x+1]._offset_-draw._offset_

def up(b,d):
	p=point.lastselect
	limit=0

def down(b,d):
	p=point.lastselect
	limit=draw.area.get_height() if drawscroll.landscape else draw.area.get_width()
