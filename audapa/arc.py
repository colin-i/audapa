
from . import drawscroll
from . import graph

import math

def draw(cr,x0,y0,x1,y1):
	land=drawscroll.landscape
	if land:
		x=x1-x0
		y=abs(y1-y0)
		if x>y:
			pass
			#rads= x,y
		else:
			rads=graph.rads(y,x)
			aux=math.cos(rads)
			cat=x/aux
			c=(cat/2)/aux
			raddif=(math.pi/2-rads)*2
		if y1<y0:
			cr.arc(x0+c,y0,c,math.pi,math.pi+raddif)
		else:
			cr.arc(x0+c,y0,c,math.pi-raddif,math.pi)
	else:
		pass
		#x=abs(x1-xo)
		#y=y1-y0
