import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from . import loop
from . import sets
from . import play
from . import drawscroll
from . import r_offset
from . import bar
from . import forms
from . import info

def main():
	if len(sys.argv)>1:
		cleanup()
		return
	sets.init()
	win = Gtk.Window()
	win.set_decorated(False)#such a heavy load here if True
	win.maximize()
	win.show()
	#while loop.n:
	play.init()
	drawscroll.init()
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	combo=[win,box]
	box.append(bar.init(combo))
	box.append(drawscroll.win)
	box.append(forms.init(combo))
	box.append(r_offset.init())
	win.set_child(box)
	info.win=win
	info.box=box
	loop.main.run()

import os
import sys

def cleanup():
	#remove config and exit
	c=sets.get_config_dir()
	if os.path.isdir(c):
		f=sets.get_config_file()
		if not os.path.isfile(f):
			f=None
	else:
		c=None
	p=sets.get_data_dir()
	if os.path.isdir(p):
		if len(os.listdir(path=p))>0:
			print(p.__str__()+" is not empty.")
			p=None
	else:
		p=None
	if c or p:
		print("Would remove:");
		if c:
			if f:
				print(f)
			print(c)
		if p:
			print(p)
		print("yes ?");
		str = ""
		while True:
			x = sys.stdin.read(1) # reads one byte at a time, similar to getchar()
			if x == '\n':
				break
			str += x
		if str=="yes":
			r=" removed"
			if c:
				if f:
					os.remove(f)
					print(f+r)
				os.rmdir(c)
				print(c.__str__()+r)
			if p:
				os.rmdir(p)
				print(p.__str__()+r)
		else:
			print("expecting \"yes\"")

if __name__ == "__main__":
    main()
