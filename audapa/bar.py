
from gi.repository import Gtk

from . import loop
from . import record
from . import sets
from . import play

def cl(b,d):
	loop.stop()

input=0x1F399

def init(win,bx):
	global box
	box=Gtk.Box()
	box.append(sets.colorButton(chr(input), record.start, input))
	box.append(sets.colorButton(chr(0x2699), sets.sets, [win,bx]))
	box.append(sets.colorButton("X", cl, None))
	box.append(play.entry)
	box.append(play.button)
	return box