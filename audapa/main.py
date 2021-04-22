import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from . import loop

from . import sets
from . import play
from . import drawscroll
from . import r_offset
from . import bar

sets.init()
win = Gtk.Window()
win.set_decorated(False)#such a heavy load here if True
win.maximize()
win.show()
while loop.n:
	play.init()
	drawscroll.init()
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	box.append(bar.init(win,box))
	box.append(drawscroll.win)
	box.append(r_offset.init())
	win.set_child(box)
	loop.main.run()
