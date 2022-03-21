



def distance(x,y,p):
	#recurse(0,len,x,y,p)
	pass

def recurse(start,stop,x,y,p):
	if start!=stop:
		a=start+int((stop-start)/2)
		#to_left=test(a)
		if to_left:
			recurse(start,a)
		else:
			recurse(a,stop)
