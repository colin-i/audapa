
from gi.repository import Gtk
import json
import configparser

from . import loop

import appdirs
import os.path
import pathlib
def get_config_file():
	p=pathlib.Path(appdirs.user_config_dir('audapa'))
	p.mkdir(exist_ok=True)
	return os.path.join(p,'config.ini')

class colorLabel(Gtk.Label):
	def __init__(self,t):
		Gtk.Label.__init__(self)
		self._set_color_(t)
	def _set_color_(self,t):
		z="<span"#p is error
		if (c:=color.get_text()):
			z+=" color='"+c+"'"
		z+=">"+t+"</span>"
		self.set_markup(z)
class colorButton(Gtk.Button):
	def __init__(self,t,f,d):
		Gtk.Button.__init__(self,child=colorLabel(t))
		self.connect('clicked',f,d)
	def _set_color_(self,t):
		self.get_child()._set_color_(t)
class colorEntry(Gtk.Entry):
	def __init__(self,b):
		Gtk.Entry.__init__(self,buffer=b,hexpand=True)
		if (c:=color.get_text()):
			cont=self.get_style_context()
			p=Gtk.CssProvider()
			p.load_from_data (b"entry { color: "+c.encode()+b"; }")
			cont.add_provider(p,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

color=Gtk.EntryBuffer()

def reset(b,di):
	config = configparser.ConfigParser()
	config['conf']={}
	c=config['conf']
	c['color']=color.get_text()
	with open(get_config_file(), "w") as configfile:
		config.write(configfile)
	if di['t']==c['color']:
		di['c'][0].set_child(di['c'][1])
	else:
		loop.stop(True)
def sets(b,combo):
	bx=Gtk.Grid(hexpand=True)
	t=colorLabel("Font Color")
	bx.attach(t,0,0,1,1)
	en=colorEntry(color)
	bx.attach(en,1,0,1,1)
	b=colorButton("Done", reset, {'c':combo,'t':color.get_text()})
	bx.attach(b,0,1,2,1)
	combo[0].set_child(bx)

def start():
	config = configparser.ConfigParser()
	if(config.read(get_config_file())):
		c=config['conf']
		color.set_text(c['color'],-1)