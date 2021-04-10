
from gi.repository import GLib

from . import record

def stop(x):
	record.terminate()
	main.quit()
	global n
	n=x

main = GLib.MainLoop()
n=True
