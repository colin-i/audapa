import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

from . import sets

def delay(w):
	w.show()
	return False
def cl(w,d):
	mainloop.quit()
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
