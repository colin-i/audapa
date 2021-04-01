import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib
import json
import os
def delay(w):
	w.show()
	return False
def cl(w,d):
	mainloop.quit()
def reset(b,en):
	if (txt:=en.get_text()):
		t=os.path.expandvars(txt)
		if not os.path.dirname(t):
			t=os.path.join(os.path.dirname(os.path.realpath(__file__)),t)
		with open(t, "w") as write_file:
			json.dump(txt, write_file)
def sets(b,w):
	bx=Gtk.Box()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	en=Gtk.Entry()
	bx.append(en)
	b=Gtk.Button.new_with_label(chr(0x2699))
	b.connect('clicked', reset, en)
	bx.append(b)
	w.set_child(bx)
win = Gtk.Window()
win.set_title('Audaparta')
win.connect('close-request', cl, None)
b=Gtk.Button.new_with_label(chr(0x2699))
b.connect('clicked', sets, win)
win.set_child(b)
win.maximize()
GLib.idle_add(delay,win)
mainloop = GLib.MainLoop()
mainloop.run()
