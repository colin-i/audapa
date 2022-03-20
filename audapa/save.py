
import math

from . import points
from . import arc
from . import draw
from . import reload

def data(b,d):
	effect()
def effect():
	apply()
	saved()
def saved():
	reload.file()
	redraw()

margin=1

def redraw():
	draw.surf()
	draw.reset()
	draw.area.queue_draw()

def set(i,v):
	draw.samples[i]=int(v) #there are troubles at write file without int
def apply():
	s=len(points.points)
	if s>=2:
		for i in range(1,s):
			prev=points.points[i-1]
			cur=points.points[i]
			x0=prev._offset_
			y0=prev._height_
			x1=cur._offset_
			y1=cur._height_
			if cur._inter_ or prev._inter_:
				apply_arc(x0,y0,x1,y1,prev._convex_)
			else:
				apply_line(x0,y0,x1,y1)

def apply_arc(x0,y0,x1,y1,conv):
	x=x1-x0
	y=abs(y1-y0)
	#get radius
	radius,rads=arc.radius(x,y)
	#get center
	_,yc,rstart,rend=arc.center(x0,y0,x1,y1,conv,x,y,radius,rads)
	#iterate
	if rstart==0 or rend==math.pi or rstart==math.pi or rend==0:
	#x axis
		xpos=radius-x
		includingmargin=x+margin #is x1-i, [0-4) (4-8] will be bad
		for i in range(0,includingmargin):
			#supra radius
			a=xpos/radius
			#to radians
			a=math.acos(a)
			#height
			h=math.sin(a)*radius
			if rstart==0:
				set(x0+i,y1+h)
			elif rstart==math.pi:
				set(x1-i,y0-h)
			elif rend==math.pi:
				set(x1-i,y0+h)
			else:
			#rend==0
				set(x0+i,y1-h)
			xpos+=1
	else:
	#y axis
		for i in range(x,-1,-1):
			a=i/radius
			a=math.asin(a)
			h=math.cos(a)*radius
			if rstart==math.pi/2:
				set(x1-i,yc+h)
			elif rstart==math.pi*3/2:
				set(x0+i,yc-h)
			elif rend==math.pi/2:
				set(x0+i,yc+h)
			else:
			#rend==math.pi*3/2
				set(x1-i,yc-h)

def apply_line(x0,y0,x1,y1):
	for i in range(x0,x1):
		set(i,0)
