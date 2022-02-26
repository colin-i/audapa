
import math

from . import points
from . import arc

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
		radius,rads,unused=arc.radius(x,y)
		#get center
		xc,yc,rstart,rend=arc.center(x0,y0,x1,y1,prev._convex_,x,y,radius,rads)
		#iterate
		if rstart==0 or rend==math.pi or rstart==math.pi or rend==0:
		#x with cos
			x1-=x0
			for i in range(1,x1):
				#supra radius
				a=i/radius
				#to radians
				a*=math.pi/2
				#height knew
				h=math.sin(a)*radius
		else:
		#x with sin
			pass
