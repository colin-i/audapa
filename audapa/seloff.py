
from gi.repository import Gtk

from . import sets
from . import bar
from . import draw
from . import r_offset
from . import drawscroll
from . import delete

on='+'
off='-'
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

def open():
	global stop,moveleft,moveright
	lst=[]
	button=sets.colorButton(on,toggle,draw.area)
	bar.box.append(button)
	lst.append(button)
	b=sets.colorButton(chr(0x2421),delete.act,None)
	bar.box.append(b)
	lst.append(b)
	moveleft=sets.colorButton("&lt;",drawscroll.move,False)
	bar.box.append(moveleft)
	lst.append(moveleft)
	moveright=sets.colorButton("&gt;",drawscroll.move,True)
	bar.box.append(moveright)
	lst.append(moveright)
	stop=sets.colorButton("x",close,{'b':button,'list':lst})
	bar.box.append(stop)
	lst.append(stop)
	#
	drawscroll.open()
def close(s,d):
	b=d['b']
	if control:
		b.emit(sets._click_)
	for x in d['list']:
		bar.box.remove(x)
	reset()
	draw.close()
	drawscroll.close()
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
		b._set_text_(off)
