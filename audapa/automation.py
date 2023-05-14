
from gi.repository import Gtk

import math

from . import sets
from . import play
from . import draw
from . import points
from . import save
from . import point
from . import move
from . import pbox

default_toler="1"
toler=Gtk.EntryBuffer(text=default_toler)

#there is a min dist in Settigs, why another one? That is for manually placed points.
default_mdist="5"
mdist=Gtk.EntryBuffer(text=default_mdist)

def open(b,combo):
	box=Gtk.Grid(hexpand=True)
	box.attach(sets.colorLabel("Tolerance"),0,0,1,1)
	box.attach(sets.colorEntry(toler),1,0,1,1)
	box.attach(sets.colorLabel("‰"),2,0,1,1)
	box.attach(sets.colorLabel("Min distance"),0,1,1,1)
	box.attach(sets.colorEntry(mdist),1,1,2,1)
	box.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,2,3,1)
	box.attach(sets.colorButton("Done",done,"Apply",combo),0,3,3,1)
	combo[0].set_child(box)

def cancel(b,combo):
	combo[0].set_child(combo[1])

def done(b,combo):
	a=toler.get_text()
	abool=a.isdigit()
	b=mdist.get_text()
	bbool=b.isdigit()
	if abool and bbool:
		a=int(a)
		b=int(b)
		if a>1000:
			toler.set_text("1000",-1)
		elif b==0:
			mdist.set_text("1",-1)
		else:
			a=math.ceil(pow(2,8*play.wavefile.getsampwidth())*a/1000);

			points.points.clear()
			if point.lastselect:
				pbox.close()
				point.lastselect=None

			if not sets.get_fulleffect():
				samplesorig=draw.samples.copy() #for line/arc effects from save, but is corrected step by step
			calculate(draw.samples,draw.length,a,b)
			if not sets.get_fulleffect():
				draw.samples=samplesorig

			move.saved(combo)
			if sets.get_fulleffect():
				save.effect()
	else:
		if not abool:
			toler.set_text(default_toler,-1)
		if not bbool:
			mdist.set_text(default_mdist,-1)

def calculate(samples,length,tolerance,min_dist):
	#exclude blank extremes
	for i in range(0,length): #not including length element
		if samples[i]!=0:
			break
	for j in range(length-1,-1,-1):
		if samples[j]!=0:
			break
	j=j+1

	if (i+min_dist)<j: #only if there is a length of min 2 points
		pnts=[]
		pnts.append(points.newp(i,samples[i],False,True))

		points.add(0,0,False,True,0) #p1
		points.add(0,0,False,True,1) #p2

		while (i+min_dist)<j:  #can be i<j and to add below, but k=k+1 can still be on j
			sum=0
			points.points[0]._offset_=i
			points.points[0]._height_=samples[i]
			for k in range(i,i+min_dist):
				sum+=samples[k]
			k=k+1
			#apply min distance
			points.points[1]._offset_=k
			h=samples[k]
			points.points[1]._height_=h
			save.apply() #or save.apply_line, will exclude at right
			for k in range(k+1,j):
				points.points[1]._offset_=k
				points.points[1]._height_=samples[k]
				save.apply()
				newsum=0
				for l in range(i,k):
					newsum+=samples[l]
				if abs(newsum-sum)>tolerance:
					#get back when tolerance was fine
					k=k-1
					points.points[1]._offset_=k
					points.points[1]._height_=h
					save.apply()
					break
				h=samples[k]
				sum+=h
			pnts.append(points.newp(k,h,False,True))
			i=k
		points.points=pnts
