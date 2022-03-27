
import math

from . import draw
from . import sets
from . import point

def test(x,y,p):
	d=float(sets.distance.get_text())
	if d:
		a=draw.cont.get_last_child() #iterate from last to first
		return recurse(x,y,p,a,d)
	return True

def recurse(x,y,p,a,d):
	if a:
		if a!=p:
			xa,ya=draw.cont.get_child_position(a)
			xb=xa+point.const-x
			yb=ya+point.const-y
			c=math.sqrt(pow(xb,2)+pow(yb,2))
			if c<d:
				print(c.__str__()+" is less than the minimum required distance of "+d.__str__())
				return False
		return recurse(x,y,p,a.get_prev_sibling(),d)
	return True
