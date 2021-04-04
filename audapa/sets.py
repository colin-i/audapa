
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
	bx=Gtk.Box()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	en=colorEntry(color)
	bx.append(en)
	b=Gtk.Button.new_with_label("Done")
	b.connect('clicked', reset, combo)
	bx.append(b)
	combo[0].set_child(bx)

def colorEntry(b):
	en=Gtk.Entry.new_with_buffer(b)
	if (c:=color.get_text()):
		cont=en.get_style_context()
		p=Gtk.CssProvider()
		p.load_from_data (b"entry { color: "+c.encode()+b"; }")
		cont.add_provider(p,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	return en

def start():
	config = configparser.ConfigParser()
	if(config.read(get_config_file())):
		c=config['conf']
		color.set_text(c['color'],-1)