
from gi.repository import Gtk,GLib

from . import sets
from . import play
from . import draw
from . import points
from . import save
from . import point
from . import move
from . import pbox
from . import loop

default_toler="1"
toler=Gtk.EntryBuffer(text=default_toler)

#there is a min dist in Settigs, why another one? That is for manually placed points.
default_mdist="5"
mdist=Gtk.EntryBuffer(text=default_mdist)

stop=Gtk.CheckButton()
default_stop="100"
stop_after=Gtk.EntryBuffer(text=default_stop)

print_test=Gtk.CheckButton()
skip_phase2=Gtk.CheckButton()

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

	box.attach(sets.colorLabel("Verbosity"),0,3,1,1)
	box.attach(print_test,1,3,2,1)

	box.attach(sets.colorLabel("Skip phase 2"),0,4,1,1)
	box.attach(skip_phase2,1,4,2,1)

	box.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,5,3,1)
	box.attach(sets.colorButton("Done",done,"Apply",combo),0,6,3,1)
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
			a=round(pow(2,8*play.wavefile.getsampwidth())*a/1000)

			points.points.clear()

			#samplesorig= #used to not store height on another var at phase1, and at phase2
			waiter(combo)
			GLib.timeout_add(0,worker,[a,b,c,draw.samples.copy(),combo])
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
			tests2=0

		while (i+min_dist+1)<j:  #j can be length
			points.points[0]._offset_=i
			points.points[0]._height_=samplesorig[i]

			for k in range(i+min_dist+1,j):
				points.points[1]._offset_=k
				points.points[1]._height_=samplesorig[k]
				save.apply() #or save.apply_line, will exclude at right
				newdif=0
				for l in range(i,k):
					newdif+=abs(samples[l]-samplesorig[l])

				if newdif>tolerance: #get back one place
					k=k-1
					samples[k]=samplesorig[k]  #this can be restored at last, why not there? who cares, too much code
					points.points[1]._offset_=k
					points.points[1]._height_=samplesorig[k]
					save.apply()
					if print_test.get_active():
						newdif=0
						for l in range(i,k):
							newdif+=abs(samples[l]-samplesorig[l])
					break
			pnts.append(points.newp(k,samplesorig[k],False,True)) #'struct' object has no attribute 'copy'

			if print_test.get_active():
				tests+=newdif
				tests2+=k-i

			if stop.get_active():
				if len(pnts)==max:
					break

			i=k
		if print_test.get_active():
			print("dif sum "+str(tests))  #the two tolerances at start will trade precision for more code
			print("points len "+str(len(pnts)))
			print("avg dist "+str(tests2/len(pnts)))
			tests=0

		#phase 2 apply arcs for better match
		pnts2=pnts.copy()
		if skip_phase2.get_active()==False:
			points.add(0,0,False,True,2) #p3
			points.points[1]._inter_=True
			aux=points.points[1]
			ix=0
			sz=len(pnts)-1
			for i in range(0,sz):
				xleft=pnts[i]._offset_;xright=pnts[i+1]._offset_
				ystart=pnts[i]._height_;yend=pnts[i+1]._height_
				points.points[0]._offset_=xleft;points.points[0]._height_=ystart
				points.points[2]._offset_=xright;points.points[2]._height_=yend

				#calculate current dif
				startdif=0
				for k in range(xleft,xright):
					startdif+=abs(samples[k]-samplesorig[k])

				bestmatch=[startdif]+([None]*4)
				arc(True,True  ,xleft,xright,ystart,yend,bestmatch,samples,samplesorig)
				arc(True,False ,xleft,xright,ystart,yend,bestmatch,samples,samplesorig)
				arc(False,True ,xleft,xright,ystart,yend,bestmatch,samples,samplesorig)
				arc(False,False,xleft,xright,ystart,yend,bestmatch,samples,samplesorig)

				if bestmatch[0]!=startdif:
					points.points[0]._concav_=bestmatch[1];points.points[1]._concav_=bestmatch[2]
					points.points[1]._offset_=bestmatch[3];points.points[1]._height_=bestmatch[4]
					save.apply()

					pnts2[ix]._concav_=points.points[0]._concav_
					ix+=1
					pnts2.insert(ix,points.newp(points.points[1]._offset_,points.points[1]._height_,True,points.points[1]._concav_))
				else: #restore the line
					points.points[1]=points.points[2]
					points.points.pop()
					save.apply()
					points.points.insert(1,aux)
				ix+=1

				if print_test.get_active():
					tests+=bestmatch[0]
					print(" "+str(i),end='',flush=True)
			if print_test.get_active():
				print()
				print("dif sum "+str(tests))
				print("points len "+str(len(pnts2)))

		points.points=pnts2

def arc(a,b,xleft,xright,ystart,yend,bestmatch,samples,samplesorig):
	points.points[0]._concav_=a;points.points[1]._concav_=b
	for x in range(xleft,xright):
		points.points[1]._offset_=x
		for y in range(ystart,yend):
			points.points[1]._height_=y
			save.apply() #or save.apply_arc

			thisdif=0
			for k in range(xleft,xright):
				thisdif+=abs(samples[k]-samplesorig[k])

			if thisdif<bestmatch[0]:
				bestmatch[0]=thisdif
				bestmatch[1]=a
				bestmatch[2]=b
				bestmatch[3]=x
				bestmatch[4]=y

def waiter(combo):
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	box.append(sets.colorLabel("Working..."))
	b=sets.colorButton("Resume",resume,"Continue",None)
	b.set_sensitive(False)
	box.append(b)
	combo[0].set_child(box)

def resume(b,d):
	pass

def worker(data):
	samplesorig=data[3]
	combo=data[4]

	calculate(draw.samples,draw.length,data[0],data[1],data[2],samplesorig)
	#from time import sleep
	#sleep(2)

	if point.lastselect:
		pbox.close()
		point.lastselect=None

	if not sets.get_fulleffect():
		draw.samples=samplesorig

	move.saved(combo)
	if sets.get_fulleffect():
		save.saved()

	return False
