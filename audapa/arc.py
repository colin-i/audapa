
from . import drawscroll
from . import graph

import math

def draw(cr,x0,y0,x1,y1,convex,ln):
	land=drawscroll.landscape
	if land:
		x=x1-x0
		y=abs(y1-y0)
	else:
		x=abs(x1-x0)
		y=y1-y0
	c,raddif,radsmall=vals(x,y,ln)
	if convex:
		if x>y:
			if (land and y0<y1) or (x0<x1 and land==False):
				arc(cr,x0,y0+c,c,math.pi*3/2,math.pi*3/2+raddif,radsmall)
				return
			if land:
				arc(cr,x1,y1+c,c,math.pi*3/2-raddif,math.pi*3/2,radsmall)
				return
			arc(cr,x1,y1-c,c,math.pi/2-raddif,math.pi/2,radsmall)
			return
		if (land and y0<y1) or (x0<x1 and land==False):
			arc(cr,x1-c,y1,c,-raddif,0,radsmall)
			return
		if land:
			arc(cr,x0+c,y0,c,math.pi,math.pi+raddif,radsmall)
			return
		arc(cr,x0-c,y0,c,0,raddif,radsmall)
		return
	if x>y:
		if (land and y0<y1) or (x0<x1 and land==False):
			arc(cr,x1,y1-c,c,math.pi/2,math.pi/2+raddif,radsmall)
			return
		if land:
			arc(cr,x0,y0-c,c,math.pi/2-raddif,math.pi/2,radsmall)
			return
		arc(cr,x0,y0+c,c,math.pi*3/2-raddif,math.pi*3/2,radsmall)
		return
	if (land and y0<y1) or (x0<x1 and land==False):
		arc(cr,x0+c,y0,c,math.pi-raddif,math.pi,radsmall)
		return
	if land:
		arc(cr,x1-c,y1,c,0,raddif,radsmall)
		return
	arc(cr,x1+c,y1,c,math.pi,math.pi+raddif,radsmall)
def vals(x,y,l):
	if x>y:
		rads=graph.rads(x,y)
		aux=math.cos(rads)
		cat=y/aux
		ad=aux*l  #ysmall
		op=math.sin(rads)*l  #xsmall
	else:
		rads=graph.rads(y,x)
		aux=math.cos(rads)
		cat=x/aux
		ad=aux*l  #xsmall
		op=math.sin(rads)*l  #ysmall
	c=(cat/2)/aux
	radsmall=math.atan2(op,c-ad)
	raddif=(math.pi/2-rads)*2
	return (c,raddif,radsmall)
def arc(cr,x,y,c,a,b,radsmall):
	cr.arc(x,y,c,a+radsmall,b-radsmall)
