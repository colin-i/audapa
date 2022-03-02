
import math

from . import points
from . import arc
from . import draw

def data(b,d):
	s=len(points.points)
	for i in range(1,s):
		prev=points.points[i-1]
		cur=points.points[i]
		x0=prev._offset_
		y0=prev._height_
		x1=cur._offset_
		y1=cur._height_
		x=x1-x0
		y=abs(y1-y0)
		#get radius
		radius,rads=arc.radius(x,y)
		#get center
		_,yc,rstart,rend=arc.center(x0,y0,x1,y1,prev._convex_,x,y,radius,rads)
		n=x1-x0
		#iterate
		if rstart==0 or rend==math.pi or rstart==math.pi or rend==0:
		#x axis
			xpos=radius-n
			includingmargin=n+1 #is x1-i, [0-4) (4-8] will be bad
			for i in range(0,includingmargin):
				#supra radius
				a=xpos/radius
				#to radians
				a=math.acos(a)
				#height
				h=math.sin(a)*radius
				if rstart==0:
					height=y1+h
					draw.samples[x0+i]=height
				elif rstart==math.pi:
					height=y0-h
					draw.samples[x1-i]=height
				elif rend==math.pi:
					height=y0+h
					draw.samples[x1-i]=height
				else:
				#rend==0
					height=y1-h
					draw.samples[x0+i]=height
				xpos+=1
		else:
		#y axis
			for i in range(n,-1,-1):
				a=i/radius
				a=math.asin(a)
				h=math.cos(a)*radius
				if rstart==math.pi/2:
					height=yc+h
					draw.samples[x0+i]=height
				elif rstart==math.pi*3/2:
				elif rend==math.pi/2:
				else:
				#rend==math.pi*3/2
	draw.surf()
	draw.reset()
	draw.area.queue_draw()
