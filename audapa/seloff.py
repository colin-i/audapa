
from gi.repository import Gtk

from . import sets
from . import bar
from . import draw
from . import r_offset
from . import drawscroll
from . import delete
from . import play
from . import forms

on='+'
#off='-'
control=None

def init():
	global start,end
	b=Gtk.Box(homogeneous=True)
	start=r_offset.inttext("0")
	start.set_halign(Gtk.Align.START)
	b.append(start)
	end=r_offset.inttext("0")
	end.set_halign(Gtk.Align.END)
	b.append(end)
	return b

def press(g,n,x,y,d):
	r_offset.calculate(int(x if drawscroll.landscape else y))

def add(a,b,c,lst):
	d=sets.colorButton(a,b,c)
	bar.box.append(d)
	lst.append(d)
	return d
def open():
	global stop,moveleft,moveright
	lst=[]
	button=add(on,toggle,draw.cont,lst)
	add(chr(0x2421),delete.act,None,lst)
	add(chr(0x1f5ce),play.save,None,lst)#4be
	moveleft=add("&lt;",drawscroll.move,False,lst)
	moveright=add("&gt;",drawscroll.move,True,lst)
	stop=add("x",close,{'b':button,'list':lst},lst)
	#
	drawscroll.open()
	forms.open()
def close(s,d):
	b=d['b']
	if control:
		b.emit(sets._click_)
	for x in d['list']:
		bar.box.remove(x)
	reset()
	draw.close()
	drawscroll.close()
	forms.close()
def reset():
	start._set_text_("0")
	end._set_text_("0")

def toggle(b,a):
	global control
	if control:
		a.remove_controller(control)
		control=None
		b._set_text_(on)
	else:
		control = Gtk.GestureClick()
		control.connect("pressed",press,None)
		a.add_controller(control)
		b._set_text_('-')
