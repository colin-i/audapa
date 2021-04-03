import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

import time

from . import sets

a=0
def delay(w):
	print('z')
	global a
	if a==2:
		return False
	elif a==1:
		w.set_visible(True)
		time.sleep(1)
		print('q')
		w.map()
		time.sleep(1)
		print('w')
	else:
		w.realize()
	a+=1
	return True
def cl(w,d):
	mainloop.quit()
sets.start()
win = Gtk.Window()
win.set_title('Audapa')
win.connect('close-request', cl, None)
b=Gtk.Button.new_with_label(chr(0x2699))
b.connect('clicked', sets.sets, win)
win.set_child(b)
win.maximize()
mainloop = GLib.MainLoop()
GLib.timeout_add(5000,delay,win)
mainloop.run()
