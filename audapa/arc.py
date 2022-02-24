
from . import drawscroll
from . import graph
from . import point

import math

def draw(cr,x0,y0,x1,y1,convex):
	land=drawscroll.landscape
	if land:
		x=x1-x0
		y=abs(y1-y0)
	else:
		x=abs(x1-x0)
		y=y1-y0
	c,raddif,radsmall=vals(x,y)
	xc,yc,rstart,rend=center(x0,y0,x1,y1,convex,x,y,c,land,raddif)
	cr.arc(xc,yc,c,rstart+radsmall,rend-radsmall)
def center(x0,y0,x1,y1,convex,x,y,c,land=True,raddif=None):
	if land:
		if convex: #convex on land
			if x>y:
				if y0<y1:
					#...
					#   ...
					xc=x0
					yc=y0+c
					if raddif!=None:
						return (xc,yc,math.pi*3/2,math.pi*3/2+raddif)
				else:
					#   ...
					#...
					xc=x1
					yc=y1+c
					if raddif!=None:
						return (xc,yc,math.pi*3/2-raddif,math.pi*3/2)
			else:
				if y0<y1:
					#.
					#.
					# .
					# .
					xc=x1-c
					yc=y1
					if raddif!=None:
						return (xc,yc,-raddif,0)
				else:
					# .
					# .
					#.
					#.
					xc=x0+c
					yc=y0
					if raddif!=None:
						return (xc,yc,math.pi,math.pi+raddif)
		else:
			if x>y:
				if y0<y1:
					#...
					#   ...
					xc=x1
					yc=y1-c
					if raddif!=None:
						return (xc,yc,math.pi/2,math.pi/2+raddif)
				else:
					#   ...
					#...
					xc=x0
					yc=y0-c
					if raddif!=None:
						return (xc,yc,math.pi/2-raddif,math.pi/2)
			else:
				if y0<y1:
					#.
					#.
					# .
					# .
					xc=x0+c
					yc=y0
					if raddif!=None:
						return (xc,yc,math.pi-raddif,math.pi)
				else:
					# .
					# .
					#.
					#.
					xc=x1-c
					yc=y1
					if raddif!=None:
						return (xc,yc,0,raddif)
	else:
		if convex:
			if x>y:
				if x0<x1:
					#...
					#   ...
					xc=x1
					yc=y1-c
					return (xc,yc,math.pi/2,math.pi/2+raddif)
				else:
					#   ...
					#...
					xc=x0
					yc=y0+c
					return (xc,yc,math.pi*3/2-raddif,math.pi*3/2)
			else:
				if x0<x1:
					#.
					#.
					# .
					# .
					xc=x0+c
					yc=y0
					return (xc,yc,math.pi-raddif,math.pi)
				else:
					# .
					# .
					#.
					#.
					xc=x1+c
					yc=y1
					return (xc,yc,math.pi,math.pi+raddif)
		else:
			if x>y:
				if x0<x1:
					#...
					#   ...
					xc=x0
					yc=y0+c
					return (xc,yc,math.pi*3/2,math.pi*3/2+raddif)
				else:
					#   ...
					#...
					xc=x1
					yc=y1-c
					return (xc,yc,math.pi/2-raddif,math.pi/2)
			else:
				if x0<x1:
					#.
					#.
					# .
					# .
					xc=x1-c
					yc=y1
					return (xc,yc,-raddif,0)
				else:
					# .
					# .
					#.
					#.
					xc=x0-c
					yc=y0
					return (xc,yc,0,raddif)
	return (xc,yc)
def radius(x,y):
	if x>y:
		rads=graph.rads(x,y)
		aux=math.cos(rads)
		cat=y/aux
	else:
		rads=graph.rads(y,x)
		aux=math.cos(rads)
		cat=x/aux
	c=(cat/2)/aux
	return (c,rads,aux)
def vals(x,y):
	c,rads,aux=radius(x,y)
	l=point.const
	if x>y:
		ad=aux*l             #ysmall
		op=math.sin(rads)*l  #xsmall
	else:
		ad=aux*l             #xsmall
		op=math.sin(rads)*l  #ysmall
	radsmall=math.atan2(op,c-ad)
	raddif=(math.pi/2-rads)*2
	return (c,raddif,radsmall)
