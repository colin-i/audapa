
import math

from . import draw
from . import sets
from . import point
from . import points

def test(x,y,p):
	d=float(sets.distance.get_text())
	if d:
		a=draw.cont.get_last_child() #iterate from last to first
		return recurse(x,y,p,a,d)
	return True

def check(a,b,d):
	x=a[0]+point.const-b[0]
	y=a[1]+point.const-b[1]
	c=math.sqrt(pow(x,2)+pow(y,2))
	if c<d: #<= can be another way
		return c
	return -1

def recurse(x,y,p,a,d):
	if a:
		if a!=p:
			c=check(draw.cont.get_child_position(a),[x,y],d)
			if c!=-1:
				print(c.__str__()+" is less than the minimum required distance of "+d.__str__())
				return False
		return recurse(x,y,p,a.get_prev_sibling(),d)
	return True

def test_all():
	sz=len(points.points)
	if sz:
		d=float(sets.distance.get_text())
		a=points.points[0]._coord_(draw.wstore,draw.hstore)
		for i in range(1,sz):
			b=points.points[i]._coord_(draw.wstore,draw.hstore)
			c=check(a,b,d)
			if c!=-1:
				return False
			a=b
	return True
