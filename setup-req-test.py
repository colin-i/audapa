
import subprocess
import sys

test=subprocess.run([sys.executable,'-m','pip','install','PyGObject>=3.40'])
if test.returncode:
	exit(test.returncode)
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib,Gdk

test=subprocess.run([sys.executable,'-m','pip','install','PyAudio>=0.2.11'])
if test.returncode:
	exit(test.returncode)
import pyaudio

test=subprocess.run([sys.executable,'-m','pip','install','pycairo>=1.20.0'])
if test.returncode:
	exit(test.returncode)
import cairo

test=subprocess.run([sys.executable,'-m','pip','install','appdirs>=1.4.3'])
if test.returncode:
	exit(test.returncode)
import appdirs

if len(sys.argv)<2:
	subprocess.run([sys.executable,'setup.py','install','--user'])
