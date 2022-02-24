
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
		y=y1-y0
		#get radius
		radius=arc.radius(x,y)[0]
		#get center
		xc,yc=arc.center(x0,y0,x1,y1,prev._convex_,x,y,radius)
		#iterate
		for i in range(x0,x1):
			i-=xc #from here is float, cannot for with floats
			#angle knew
			#height knew
