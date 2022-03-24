
from . import point
from . import points
from . import draw
from . import drawscroll

def left_type():
	p=point.lastselect
	ix=points.points.index(p)
	if ix!=0:
		x,y=draw.cont.get_child_position(draw.cont.get_prev_child(p))
		if drawscroll.landscape:
			return x
		else:
			return y
	return 0
def right_type():
	p=point.lastselect
	ix=points.points.index(p)
	if x+1==len(points.points) or points.points[x+1]._offset_>(draw.offset+draw.size):
		limit==draw.size
	else:
		limit=points.points[x+1]._offset_-draw._offset_

def left(b,d):
	if drawscroll.landscape:
		limit=left_type()
	else:
		limit=0

def right(b,d):
	if drawscroll.landscape()
		limit=right_type()
	else:
		limit=draw.area.get_width()

def up(b,d):
	if drawscroll.landscape:
		limit=0
	else:
		limit=left_type()

def down(b,d):
	if drawscroll.landscape:
		limit=draw.area.get_height()
	else:
		limit=right_type()
