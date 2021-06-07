
from . import seloff
from . import draw
from . import r_offset
from . import drawscroll

def act(b,d):
	st=seloff.start._get_()
	en=seloff.end._get_()
	del draw.samples[st:en]
	draw.length-=en-st
	rem=r_offset.atleft._get_()
	if(rem>=draw.length):
		n=drawscroll.win.get_width() if drawscroll.landscape else drawscroll.win.get_height()
		draw.offset=max(0,st-int(n/2))
	else:
		draw.ostore=-1#flag for draw
	draw.redraw()
	seloff.reset()
	r_offset.cged(drawscroll.win.get_hadjustment()) if drawscroll.landscape else r_offset.cged(drawscroll.win.get_vadjustment())
