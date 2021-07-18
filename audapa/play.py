import pyaudio
import wave

from gi.repository import GLib

from . import sets
from . import draw
from . import seloff
from . import points

wavefile=None
output=0x23F5
timer=0

def activate(en,d):
	terminate()
	launch()
def toggle(b,d):
	if not wavefile:
		launch()
		start()
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
	f=entry.get_text()
	wavefile=wave.open(f,'rb')
	audio = pyaudio.PyAudio() # create pyaudio instantiation
	sampwidth=wavefile.getsampwidth()
	format = audio.get_format_from_width(sampwidth)
	rate = wavefile.getframerate()
	channels = wavefile.getnchannels()
	draw.length=wavefile.getnframes()
	data = wavefile.readframes(draw.length)
	wavefile.rewind()#for playing
	# create pyaudio stream
	stream = audio.open(format=format,rate=rate,channels=channels,
		output = True,start=False,stream_callback=callback)
	#open
	points.read(f)
	draw.open(format,sampwidth,channels,data)
	seloff.open()
def start():
	stream.start_stream()
	button._set_text_(chr(0x23F8))
	global timer
	timer=GLib.timeout_add_seconds(1,is_act,None)
def pausing():
	stream.stop_stream()
	button._set_text_(chr(output))
def pause():
	pausing()
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
		seloff.stop.emit(sets._click_)

def is_act(d):
	if not stream.is_active():
		pausing()
		global timer
		timer=0
		wavefile.rewind()
		return False
	return True

def scan(sampwidth,channels):
	formats={pyaudio.paInt16:'h',pyaudio.paUInt8:'B',pyaudio.paInt8:'b',
		pyaudio.paFloat32:'f',pyaudio.paInt32:'i'}
	format = audio.get_format_from_width(sampwidth)
	fm=formats[format]
	return ['<'+fm*channels,fm]

def save(b,d):
	f_in=entry.get_text()
	with wave.open(f_in,'wb') as file:
		c=wavefile.getnchannels()
		file.setnchannels(c)
		s=wavefile.getsampwidth()
		file.setsampwidth(s)
		file.setframerate(wavefile.getframerate())
		#.setparams((1, 4, Fs, 0, 'NONE', 'not compressed'))
		sc=scan(s,c)[0]
		b=b"".join((wave.struct.pack(sc,i[0]) for i in draw.samples))
		file.writeframes(b)#writeframesraw
	points.write(f_in)
def saveshort(b,d):
	points.write(entry.get_text())
