
points=[]

def insert(poi):
	for p in points:
		if poi._offset_<p._offset_:
			points.insert(points.index(p),poi)
			return
	points.append(poi)
def move(p,o):
	ini=points.index(p)
	ix=ini
	last=len(points)-1
	of=p._offset_
	if o<of:
		while ix<last:
			o=points[ix+1]._offset_
			if o<of:
				ix+=1
				continue
			break
	else:
		while ix>0:
			o=points[ix-1]._offset_
			if of<o:
				ix-=1
				continue
			break
	if ini!=ix:
		del points[ini]
		points.insert(ix,p)