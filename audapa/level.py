
from gi.repository import Gtk

from . import sets
from . import draw
from . import points

dif=Gtk.EntryBuffer()

#signbutton,maxlabel
sign_positive="+"

def open(b,combo):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	#+/- button or not   entry   maxim
	global signbutton,maxlabel
	b2=Gtk.Box()
	if draw.baseline!=0:
		signbutton=sets.colorButton(sign_positive,sign,"Sign")
		b2.append(signbutton)
	en=sets.colorEntry(dif)
	b2.append(en)
	maxlabel=sets.colorLabel(maximum())
	b2.append(maxlabel)
	box.append(b2)
	#atstart   middle[-1,1]   - or calculated
	st=sets.colorLabel("0")
	md=sets.colorLabel("0")
	cal=sets.colorLabel("0")
	b3=Gtk.Box(homogeneous=True)
	b3.append(st)
	b3.append(md)
	b3.append(cal)
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

def click(b,combo):
	abort(b,combo)

def sign(b,d):
	if b.get_child().get_text()==sign_positive:
		b._set_text_("-")
	else:
		b._set_text_(sign_positive)
	maxlabel._set_text_(maximum())

def abort(b,combo):
	combo[0].set_child(combo[1])

def maximum():
	a=draw.sampsize
	if draw.baseline!=0:
		a=int(a*draw.baseline)
		positiv=signbutton.get_child().get_text()==sign_positive
	else:
		positiv=True
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
