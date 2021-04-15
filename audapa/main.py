import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from . import loop
from . import sets
from . import record
from . import play
from . import draw
from . import drawscroll

def cl(b,d):
	d.stop(False)

sets.init()
play.init()
drawscroll.win.set_vexpand(True)
drawscroll.win.set_child(draw.area)
win = Gtk.Window()
win.set_decorated(False)#such a heavy load here if True
win.maximize()
win.show()
input=0x1F399
while loop.n:
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	bx=Gtk.Box()
	bx.append(sets.colorButton(chr(input), record.start, input))
	bx.append(sets.colorButton(chr(0x2699), sets.sets, [win,box]))
	bx.append(sets.colorButton("X", cl, loop))
	bx.append(play.entry)
	bx.append(play.button)
	box.append(bx)
	box.append(drawscroll.win)
	win.set_child(box)
	loop.main.run()
