
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
	config['color']=color.get_text()
	with open(get_config_file(), "w") as configfile:
		config.write(configfile)
	combo[0].set_child(combo[1])
def sets(b,w):
	bx=Gtk.Box()
	bx.set_orientation(Gtk.Orientation.VERTICAL)
	en=colorEntry(color)
	bx.append(en)
	b=Gtk.Button.new_with_label("Done")
	b.connect('clicked', reset, [w,b])
	bx.append(b)
	w.set_child(bx)

def colorEntry(b):
	en=Gtk.Entry.new_with_buffer(b)
	if (c:=color.get_text()):
		cont=en.get_style_context()
		p=Gtk.CssProvider()
		p.load_from_data (b"entry { color: "+c+"; }")
		cont.add_provider(p,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	return en

def start():
	config = configparser.ConfigParser()
	if(config.read(get_config_file())):
		color.set_text(config['color'])