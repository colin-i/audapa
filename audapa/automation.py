
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

stop=Gtk.CheckButton()
default_stop="100"
stop_after=Gtk.EntryBuffer(text=default_stop)

print_test=Gtk.CheckButton()

def open(b,combo):
	box=Gtk.Grid(hexpand=True)
	box.attach(sets.colorLabel("Tolerance"),0,0,1,1)
	box.attach(sets.colorEntry(toler),1,0,1,1)
	box.attach(sets.colorLabel("‰"),2,0,1,1)
	box.attach(sets.colorLabel("Min distance"),0,1,1,1)
	box.attach(sets.colorEntry(mdist),1,1,2,1)
	bx=Gtk.Box()
	bx.append(sets.colorLabel("Stop after N non-inter points"))
	bx.append(stop)
	box.attach(bx,0,2,1,1)
	box.attach(sets.colorEntry(stop_after),1,2,2,1)
	box.attach(sets.colorLabel("Print test"),0,3,1,1)
	box.attach(print_test,1,3,2,1)
	box.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,4,3,1)
	box.attach(sets.colorButton("Done",done,"Apply",combo),0,5,3,1)
	combo[0].set_child(box)

def cancel(b,combo):
	combo[0].set_child(combo[1])

def done(b,combo):
	a=toler.get_text()
	abool=a.isdigit()
	b=mdist.get_text()
	bbool=b.isdigit()
	c=stop_after.get_text()
	cbool=c.isdigit()
	if abool and bbool and cbool:
		a=int(a)
		b=int(b)
		c=int(c)
		if a>1000:
			toler.set_text("1000",-1)
		elif b==0:
			mdist.set_text("1",-1)
		elif c<2:
			stop_after.set_text("2",-1)
		else:
			a=math.ceil(pow(2,8*play.wavefile.getsampwidth())*a/1000);

			points.points.clear()
			if point.lastselect:
				pbox.close()
				point.lastselect=None

			if not sets.get_fulleffect():
				samplesorig=draw.samples.copy() #for line/arc effects from save, but is corrected step by step
			calculate(draw.samples,draw.length,a,b,c,samplesorig)
			if not sets.get_fulleffect():
				draw.samples=samplesorig

			move.saved(combo)
			if sets.get_fulleffect():
				save.saved()
	else:
		if not abool:
			toler.set_text(default_toler,-1)
		if not bbool:
			mdist.set_text(default_mdist,-1)
		if not cbool:
			stop_after.set_text(default_stop,-1)

def calculate(samples,length,tolerance,min_dist,max,samplesorig):
	#exclude blank extremes
	for i in range(0,length): #not including length element
		if samples[i]!=0:
			break
	for j in range(length-1,-1,-1):
		if samples[j]!=0:
			break
	j=j+1

	if (i+min_dist+1)<j: #only if there is a length of min 2 points
		pnts=[]
		pnts.append(points.newp(i,samples[i],False,True))

		points.add(0,0,False,True,0) #p1
		points.add(0,0,False,True,1) #p2

		if print_test.get_active():
			tests=0

		while (i+min_dist+1)<j:  #j can be length
			sum=0
			points.points[0]._offset_=i
			points.points[0]._height_=samplesorig[i]
			for l in range(i,i+min_dist): #apply min distance
				sum+=samplesorig[l]

			for k in range(i+min_dist+1,j):
				sum+=samplesorig[k-1]

				points.points[1]._offset_=k
				points.points[1]._height_=samplesorig[k]
				save.apply() #or save.apply_line, will exclude at right
				newsum=0
				for l in range(i,k):
					newsum+=samples[l]

				newdif=abs(newsum-sum)
				if newdif>tolerance: #get back one place
					k=k-1
					samples[k]=samplesorig[k]  #and restore the sample in case it is last
					points.points[1]._offset_=k
					points.points[1]._height_=samplesorig[k]
					save.apply()
					if print_test.get_active():
						sum-=samplesorig[k]
						newsum=0
						for l in range(i,k):
							newsum+=samples[l]
						newdif=abs(newsum-sum)
					break
			pnts.append(points.newp(k,samplesorig[k],False,True)) #points.points[1]._height_
			i=k

			if print_test.get_active():
				tests+=newdif

			if stop.get_active():
				if len(pnts)==max:
					break
		if print_test.get_active():
			print(tests)  #the two tolerances at start will trade precision for more code

		#phase 2 apply arcs for better match
		points.add(0,0,False,True,2) #p3
		sz=len(pnts)-1
		for i in range(0,sz):
			points.points[0]._offset_=pnts[i]._offset_
			points.points[0]._height_=pnts[i]._height_
			points.points[2]._offset_=pnts[i+1]._offset_
			points.points[2]._height_=pnts[i+1]._height_

		points.points=pnts
