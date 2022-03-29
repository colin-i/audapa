
from gi.repository import Gtk

from . import sets
from . import points
from . import level
from . import draw
from . import blank
from . import move
from . import save

spread=Gtk.EntryBuffer()
reduce=Gtk.CheckButton()

def open(b,combo):
	bx=Gtk.Grid(hexpand=True)
	bx.attach(sets.colorLabel("Spread/Compress N samples"),0,0,1,1)
	bx.attach(sets.colorEntry(spread),1,0,1,1)
	bx.attach(sets.colorLabel("Compress"),0,1,1,1) #Enlarge
	bx.attach(reduce,1,1,1,1)
	bx.attach(sets.colorButton("Cancel",cancel,"Abort",combo),0,2,2,1)
	bx.attach(sets.colorButton("Done",done,"Apply",combo),0,3,2,1)
	combo[0].set_child(bx)

def cancel(b,combo):
	#if snapshot: restore
	combo[0].set_child(combo[1])

def done(b,combo):
	a=spread.get_text()
	if a.isdigit():
		ps=points.points
		s=len(ps)
		if s>=2:
			b=int(a)
			n=ps[s-1]._offset_-ps[0]._offset_
			if reduce.get_active():
				if b>n:
					spread.set_text(n.__str__(),-1)
					return
				#if snapshot: restore
				#snapshot1
				end=ps[s-1]._offset_
				apply(-b,-1)
				if sets.get_fulleffect():
					#snapshot2
					compress(b,end)
			else:
				if sets.get_fulleffect():
					enlarge(b)
				apply(b,1)
			conclude(combo)
			return
		combo[0].set_child(combo[1])
		return
	level.not_a_digit(spread)
def conclude(combo):
	move.saved(combo)
	if sets.get_fulleffect():
		blank.saved()
		save.effect()

def enlarge(n):
	s=len(draw.samples)
	extra=s-points.points[len(points.points)-1]._offset_
	#there is a nicer move but this is lazy
	right=draw.samples[s-extra:]
	del draw.samples[s-extra:]
	draw.samples=draw.samples+([0]*n)+right

def compress(n,end):
	#copy right at position
	s=len(draw.samples)
	extra=s-end
	for i in range(end,s):
		draw.samples[i-n]=draw.samples[i]
	#remove N in safe
	del draw.samples[s-n:]

def apply(n,sign):
	ps=points.points
	leng=len(ps)
	total=ps[leng-1]._offset_-ps[0]._offset_
	rest=[]
	rest_sum=0
	for i in range(1,leng):
		sz=(ps[i]._offset_-ps[i-1]._offset_)*n
		sp=int(sz/total)
		rs=sz%total
		ps[i]._offset_+=sp
		rest.append([rs,i])
		rest_sum+=rs
		for j in range(i+1,leng):
			ps[j]._offset_+=sp
	rest.sort(reverse=True) #by first
	unassigned=int(rest_sum/total) #'float' object cannot be interpreted as an integer
	for i in range(0,unassigned):
		pos=rest[i][1]
		ps[pos]._offset_+=sign
		for j in range(pos+1,leng):
			ps[j]._offset_+=sign
