
from . import points
from . import play
from . import draw
from . import save

def create(b,d):
	if not play.wavefile:
		f=play.entry.get_text()
		#read points and build info
		info=points.read(f)
		if info:
			sampwidth,channels,rate,draw.length=info
			play.open(sampwidth,channels,rate)
			#samples
			draw.samples=[0] * draw.length # [0 for i in range(draw.length)]
			save.apply()
			#for playback
			play.save_file(f,sampwidth,channels,rate)
			play.waveopen(f)
