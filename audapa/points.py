
import os
import pathlib
import json

from . import sets
from . import point

points=[]

def insert(poi):
	ln=len(points)
	for ix in range(0,ln):
		p=points[ix]
		if poi._offset_<p._offset_:
			points.insert(ix,poi)
			if ix>0:
				if (points[ix-1]._inter_==False
					 and p._inter_==False):
					poi._inter_=True
			return ix
	points.append(poi)
	return ln
def move(p,o,ini,w,h,dels):
	ix=ini
	last=len(points)-1
	of=p._offset_
	forward=o<of
	if forward:
		while ix<last:
			o=points[ix+1]._offset_
			if o<of:
				if p._inter_:
					p._offset_=o
					return ix
				ix+=1
				continue
			break
	else:
		while ix>0:
			o=points[ix-1]._offset_
			if of<o:
				if p._inter_:
					p._offset_=o
					return ix
				ix-=1
				continue
			break
	if ini!=ix:
		indx=ini+1 if forward else ini-1
		pnt=points[indx]
		if pnt._inter_:
			pr=pnt.get_parent()
			if pr:
				pr.remove(pnt)
				if forward:
					dels.append([points[indx+1]._coord_(w,h),pnt._coord_(w,h)])
				else:
					dels.append([pnt._coord_(w,h),points[indx-1]._coord_(w,h)])
			pnt._remove_(indx)
			if forward:
				ix-=1
			else:
				ini-=1
		del points[ini]
		points.insert(ix,p)
	return ix
def dpath(f_in):
	p=os.path.dirname(f_in)
	return os.path.join(p,'_'+sets.pkgname+'cache_')
def fpath(d_in,f_in):
	return os.path.join(d_in,os.path.basename(f_in)+'.json')
def write(f_in):
	p=dpath(f_in)
	f_out=fpath(p,f_in)
	if len(points):
		pathlib.Path(p).mkdir(exist_ok=True)#parents=False, FileExistsError exceptions will be ignored
		with open(f_out,"w") as f:
			d=[]
			for po in points:
				d.append([po._offset_,po._height_,po._inter_])
			json.dump(d,f)
	elif os.path.exists(f_out):
		  os.remove(f_out)
def read(f_in):
	f_out=fpath(dpath(f_in),f_in)
	if os.path.exists(f_out):
		with open(f_out) as f:
			d=json.load(f)
			for p in d:
				po=point.struct()
				po._offset_=p[0]
				po._height_=p[1]
				po._inter_=p[2]
				points.append(po)