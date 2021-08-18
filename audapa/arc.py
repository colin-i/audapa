
from . import drawscroll
from . import graph

import math

def draw(cr,x0,y0,x1,y1):
	land=drawscroll.landscape
	if land:
		x=x1-x0
		y=abs(y1-y0)
		if x>y:
			rads=graph.rads(x,y)
			aux=math.cos(rads)
			cat=y/aux
			#
			c=(cat/2)/aux
			raddif=(math.pi/2-rads)*2
			if y0<y1:
				cr.arc(x0,y0+c,c,math.pi*3/2,math.pi*3/2+raddif)
			else:
				cr.arc(x1,y1+c,c,math.pi*3/2-raddif,math.pi*3/2)
		else:
			rads=graph.rads(y,x)
			aux=math.cos(rads)
			cat=x/aux
			#
			c=(cat/2)/aux
			raddif=(math.pi/2-rads)*2
			if y0<y1:
				cr.arc(x1-c,y1,c,-raddif,0)
			else:
				cr.arc(x0+c,y0,c,math.pi,math.pi+raddif)
	else:
		pass
		#x=abs(x1-xo)
		#y=y1-y0
