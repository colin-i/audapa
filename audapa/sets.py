
from gi.repository import Gtk
import json
import configparser

import appdirs
import os.path
import pathlib
def get_config_file():
	p=pathlib.Path(appdirs.user_config_dir('audapa'))
	p.mkdir(exist_ok=True)
	return os.path.join(p,'config.ini')

color=Gtk.EntryBuffer()

def reset(b,combo):
	config = configparser.ConfigParser()
	config['conf']={}
	c=config['conf']
	c['color']=color.get_text()
	with open(get_config_file(), "w") as configfile:
		config.write(configfile)
	combo[0].set_child(combo[1])
def sets(b,combo):
	bx=Gtk.Grid(hexpand=True)
	t=colorLabel("Font Color")
	bx.attach(t,0,0,1,1)
	en=colorEntry(color)
	bx.attach(en,1,0,1,1)
	b=Gtk.Button.new_with_label("Done")
	b.connect('clicked', reset, combo)
	bx.attach(b,0,1,2,1)
	combo[0].set_child(bx)

def colorLabel(t):
	a=Gtk.Label()#halign=Gtk.Align.START
	z="<span"#p is error
	if (c:=color.get_text()):
		z+=" color='"+c+"'"
	z+=">"+t+"</span>"
	a.set_markup(z)
	return a
def colorEntry(b):
	a=Gtk.Entry(buffer=b,hexpand=True)
	if (c:=color.get_text()):
		cont=a.get_style_context()
		p=Gtk.CssProvider()
		p.load_from_data (b"entry { color: "+c.encode()+b"; }")
		cont.add_provider(p,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	return a

def start():
	config = configparser.ConfigParser()
	if(config.read(get_config_file())):
		c=config['conf']
		color.set_text(c['color'],-1)