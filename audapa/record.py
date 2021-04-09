import pyaudio
import wave

wavefile=None

def callback(in_data, frame_count, time_info, status):
	wavefile.writeframes(in_data)
	return (None, pyaudio.paContinue)

def start(b,ready):
	global audio,stream,wavefile
	if not wavefile:
		audio = pyaudio.PyAudio() # create pyaudio instantiation
		chans=1
		bits=pyaudio.paInt16 # 16-bit resolution
		rate=16000 # 16kHz sampling rate
		# create pyaudio stream
		stream = audio.open(format = bits,rate = rate,channels = chans,
			input = True,
			frames_per_buffer=4096, # 2^12 samples for buffer
			stream_callback=callback)
		wavefile = wave.open('test1.wav','wb')
		wavefile.setnchannels(chans)
		wavefile.setsampwidth(audio.get_sample_size(bits))
		wavefile.setframerate(rate)
		#visual
		b.set_label(chr(0x23F9))
		return
	# stop the stream, close it, terminate the pyaudio instantiation
	stream.stop_stream()
	stream.close()
	audio.terminate()
	# close the file
	wavefile.close()
	wavefile=None
	b.set_label(chr(ready))
