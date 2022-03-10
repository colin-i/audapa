
from gi.repository import Gtk

from . import sets
from . import draw
from . import points
from . import save
from . import graph

dif=Gtk.EntryBuffer()

#signbutton,maxlabel
sign_positive="+"

def open(b,combo):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	#+/- button or not   entry   maxim
	global signbutton,maxlabel,calculated,middlerate
	b2=Gtk.Box()
	if draw.baseline!=0:
		signbutton=sets.colorButton(sign_positive,sign,"Sign")
		b2.append(signbutton)
	en=sets.colorEntry(dif)
	b2.append(en)
	b2.append(sets.colorLabel("from 0 to "))
	maxlabel=sets.colorLabel(maximum())
	b2.append(maxlabel)
	box.append(b2)
	#atstart   middle[-1,1]   - or calculated
	cdata,mdata=calculate()
	st=sets.colorLabel(cdata)
	middlerate=sets.colorLabel(mdata)
	calculated=sets.colorLabel("-")
	b3=Gtk.Box(homogeneous=True)
	b3.append(st)
	b3.append(middlerate)
	b3.append(calculated)
	box.append(b3)
	#Calculate
	calc=sets.colorButton("Calculate",calcs,"Test")
	box.append(calc)
	#Cancel
	exit=sets.colorButton("Cancel",abort,"Abort",combo)
	box.append(exit)
	bt=sets.colorButton("Done",click,"Apply",combo)
	box.append(bt)
	combo[0].set_child(box)
	#copies
	global pointsorig,samplesorig
	#.copy() => it is not deep, _height_ same
	pointsorig=[]
	for p in points.points:
		pointsorig.append(p._height_)
	samplesorig=draw.samples.copy()

def click(b,combo):
	done(combo) #this here, else problems at get_native().get_surface()
	save.saved()
	graph.redraw()

def sign(b,d):
	if b.get_child().get_text()==sign_positive:
		b._set_text_("-")
	else:
		b._set_text_(sign_positive)
	maxlabel._set_text_(maximum())

def abort(b,combo):
	for i in range(len(pointsorig)-1,-1,-1):
		points.points[i]._height_=pointsorig[i]
	draw.samples=samplesorig
	done(combo)

def size_sign():
	if draw.baseline!=0:
		positiv=signbutton.get_child().get_text()==sign_positive
	else:
		positiv=True
	return (get_size(),positiv)
def get_size():
	if draw.baseline!=0:
		return int(draw.sampsize*draw.baseline)
	return draw.sampsize

def maximum():
	a,positiv=size_sign()
	a-=1 #not targeting 32768, but [0,32767]
	x=0
	for p in points.points:
		if p._height_>=0:
			h=p._height_
		else:
			h=-p._height_
		if positiv:
			h=a-h
		if h>x:
			x=h
	return x.__str__()

def calcs(b,d):
	c=dif.get_text()
	if c.isdigit():
		a=int(c)
		b=int(maxlabel.get_text())
		if a>b:
			dif.set_text(b.__str__(),-1)
			return
		sz,sgn=size_sign()
		if sgn:
			for p in points.points:
				if p._height_>=0:
					p._height_+=a
					if p._height_>=sz:
						p._height_=sz-1
				else:
					p._height_-=a
					if p._height_<-sz:
						p._height_=-sz
		else:
			for p in points.points:
				if p._height_>=0:
					if a>=p._height_:
						p._height_=0
					else:
						p._height_-=a
				else:
					if a>=-p._height_:
						p._height_=0
					else:
						p._height_+=a
		maxlabel._set_text_(maximum())
		save.apply()
		cdata,mdata=calculate()
		calculated._set_text_(cdata)
		middlerate._set_text_(mdata)

def done(combo):
	combo[0].set_child(combo[1])

def calculate():
	s=len(points.points)
	if s>=2:
		n=0
		start=points.points[0]._offset_
		stop=points.points[s-1]._offset_+save.margin
		for i in range(start,stop):
			n+=abs(draw.samples[i])
		med=n/(stop-start)
		#
		a=get_size()/2
		b=med-a
		mid=b/a
		#
		return (med.__str__(),mid.__str__())
	return ("-","-")
