
import subprocess
import sys

test=subprocess.run([sys.executable,'-m','pip','install','PyGObject>=3.40'])
if test.returncode:
	exit(test.returncode)
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

test=subprocess.run([sys.executable,'-m','pip','install','PyAudio>=0.2.11'])
if test.returncode:
	exit(test.returncode)
import pyaudio

subprocess.run([sys.executable,'-m','pip','install','--user','.'])
