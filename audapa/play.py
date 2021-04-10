import pyaudio
import wave

from gi.repository import GLib

from . import sets

wavefile=None
output=0x23F5
	
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
	global audio,stream,wavefile,timer
	wavefile=wave.open(entry.get_text(),'rb')
	audio = pyaudio.PyAudio() # create pyaudio instantiation
	# create pyaudio stream
	stream = audio.open(format = audio.get_format_from_width(wavefile.getsampwidth()),
		rate = wavefile.getframerate(),
		channels = wavefile.getnchannels(),
		output = True,
		stream_callback=callback)
	start()
	timer=GLib.timeout_add_seconds(1,is_act,None)
def start():
	stream.start_stream()
	button._set_color_(chr(0x23F8))
def pause():
	stream.stop_stream()	
	button._set_color_(chr(output))
def stop():
	# stop the stream, close it, terminate the pyaudio instantiation
	pause()
	stream.close()
	audio.terminate()
	# close the file
	global wavefile
	wavefile.close()
	wavefile=None
	GLib.source_remove(timer)
def terminate():
	if wavefile:
		stop()

def is_act(d):
	if not stream.is_active():
		if not stream.is_stopped():
			stop()
			return False
	return True