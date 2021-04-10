
from gi.repository import GLib

from . import record
from . import play

def stop(x):
	record.terminate()
	play.terminate()
	main.quit()
	global n
	n=x

main = GLib.MainLoop()
n=True
