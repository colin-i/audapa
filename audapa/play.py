import pyaudio
import wave

from gi.repository import GLib

from . import sets
from . import draw
from . import seloff

wavefile=None
output=0x23F5
timer=0

def activate(en,d):
	terminate()
	launch()
def toggle(b,d):
	if not wavefile:
		launch()
		return
	if stream.is_stopped():
		start()
	else:
		pause()

def init():
	global entry,button
	entry=sets.colorEntry()
	button=sets.colorButton(chr(output), toggle, None)
	entry.connect('activate',activate,None)

def callback(in_data, frame_count, time_info, status):
	data = wavefile.readframes(frame_count)
	return (data, pyaudio.paContinue)

def launch():
	global audio,stream,wavefile
	wavefile=wave.open(entry.get_text(),'rb')
	seloff.open()
	audio = pyaudio.PyAudio() # create pyaudio instantiation
	sampwidth=wavefile.getsampwidth()
	format = audio.get_format_from_width(sampwidth)
	rate = wavefile.getframerate()
	channels = wavefile.getnchannels()
	draw.length=wavefile.getnframes()
	data = wavefile.readframes(draw.length)
	wavefile.rewind()#for playing
	draw.prepare(format,sampwidth,channels,data)
	# create pyaudio stream
	stream = audio.open(format=format,rate=rate,channels=channels,
		output = True,start=False,stream_callback=callback)
def start():
	stream.start_stream()
	button._set_text_(chr(0x23F8))
	global timer
	timer=GLib.timeout_add_seconds(1,is_act,None)
def pause():
	stream.stop_stream()	
	button._set_text_(chr(output))
	global timer
	if timer:
		GLib.source_remove(timer)
		timer=0
def stop():
	# stop the stream, close it, terminate the pyaudio instantiation
	pause()
	stream.close()
	audio.terminate()
	# close the file
	global wavefile
	wavefile.close()
	wavefile=None
def terminate():
	if wavefile:
		stop()

def is_act(d):
	if not stream.is_active():
		stop()
		return False
	return True