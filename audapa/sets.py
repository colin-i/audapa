
from gi.repository import Gtk
import json
import configparser

class colorLabel(Gtk.Label):
	def __init__(self,t):
		Gtk.Label.__init__(self)
		self._set_text_(t)
	def _set_text_(self,t):
		z="<span"#p is error
		if (c:=color.get_text()):
			z+=" color='"+c+"'"
		z+=">"+t+"</span>"
		self.set_markup(z)
_click_ = "clicked"
class colorButton(Gtk.Button):
	def __init__(self,t,f,i,d=None):
		Gtk.Button.__init__(self,child=colorLabel(t))
		self.connect(_click_,f,d)
		self.set_tooltip_text(i)
	def _set_text_(self,t):
		self.get_child()._set_text_(t)
class colorEntry(Gtk.Entry):
	def __init__(self,b=Gtk.EntryBuffer()):
		Gtk.Entry.__init__(self,buffer=b,hexpand=True)
		self._color_()
	def _color_(self):
		if (c:=color.get_text()):
			cont=self.get_style_context()
			self._provider_=Gtk.CssProvider()
			self._provider_.load_from_data (b"entry { color: "+c.encode()+b"; }")
			cont.add_provider(self._provider_,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		else:
			self._provider_=None
	def _recolor_(self):
		if self._provider_:
			cont=self.get_style_context()
			cont.remove_provider(self._provider_)
		self._color_()

pkgname='audapa'
import appdirs
import os.path
import pathlib
from html import escape

from . import draw
from . import forms

def get_config_dir():
	return pathlib.Path(appdirs.user_config_dir(pkgname))
get_config_dir().mkdir(exist_ok=True)
def get_config_file():
	return os.path.join(get_config_dir(),'config.ini')

def get_data_dir():
	return pathlib.Path(appdirs.user_data_dir(pkgname))
get_data_dir().mkdir(exist_ok=True)
def get_data_file(f):
	return os.path.join(get_data_dir(),f)

color=Gtk.EntryBuffer(text="purple")
def get_color():
	return color.get_text()
fgcolor=Gtk.EntryBuffer(text="red")
def get_fgcolor():
	return fgcolor.get_text()
fgcolor2=Gtk.EntryBuffer(text="green")
def get_fgcolor2():
	return fgcolor2.get_text()
fgcolor3=Gtk.EntryBuffer(text="blue")
def get_fgcolor3():
	return fgcolor3.get_text()
zero_button=Gtk.CheckButton()

def add(bx,tx,x,n):
	return adder(bx,tx,colorEntry(x),n)
def adder(bx,tx,x,n):
	t=colorLabel(tx)
	bx.attach(t,0,n,1,1)
	bx.attach(x,1,n,1,1)
	return n+1
def sets(b,combo):
	bx=Gtk.Grid(hexpand=True)
	n=add(bx,"Font/Stroke Color",color,0)
	n=add(bx,"Foreground Color",fgcolor,n)
	n=add(bx,"Foreground Color2",fgcolor2,n)
	n=add(bx,"Foreground Color3",fgcolor3,n)
	n=adder(bx,"Zero outside start and end at "+forms.formal_write,zero_button,n)
	b=colorButton("Done", reset, "Return", {'c':combo,'t':
		{'cl':color.get_text(),'fcl':fgcolor.get_text()}})
	bx.attach(b,0,n,2,1)
	combo[0].set_child(bx)

def init():
	config = configparser.ConfigParser()
	if(config.read(get_config_file())):
		c=config['conf']
		color.set_text(c['color'],-1)
		fgcolor.set_text(c['fgcolor'],-1)
		fgcolor2.set_text(c['fgcolor2'],-1)
		fgcolor3.set_text(c['fgcolor3'],-1)
		zero_button.set_active(False if c['zero']=='False' else True)

def reset(b,di):
	config = configparser.ConfigParser()
	config['conf']={}
	c=config['conf']
	c['color']=color.get_text()
	c['fgcolor']=fgcolor.get_text()
	c['fgcolor2']=fgcolor2.get_text()
	c['fgcolor3']=fgcolor3.get_text()
	c['zero']=zero_button.get_active().__str__()
	with open(get_config_file(), "w") as configfile:
		config.write(configfile)
	win=di['c'][0]
	box=di['c'][1]
	if di['t']['cl']==c['color']:
		win.set_child(box)
		if di['t']['fcl']!=c['fgcolor']:
			draw.draw_sel()
		return
	draw.reset()
	search(box)
	win.set_child(box)
def search(p):
	x=p.get_first_child()
	while x:
		if isinstance(x,colorLabel):
			x._set_text_(escape(x.get_text()))
		elif isinstance(x,colorEntry):
			x._recolor_()
		else:
			search(x)
		x=x.get_next_sibling()
