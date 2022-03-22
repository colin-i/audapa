
from . import draw

def test(x,y,p):
	a=draw.cont.get_last_child() #iterate from last to first
	recurse(x,y,p,a)
	return True

def recurse(x,y,p,a):
	if a:
		recurse(x,y,p,a.get_prev_sibling())
