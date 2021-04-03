pkname='audapa'

import subprocess
import sys
test=subprocess.run([sys.executable,'-m','pip','install','PyGObject>=3.40'])
if test.returncode:
	exit(test.returncode)
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk,GLib

from setuptools import setup
setup(name=pkname,
	version='1.0.0',
	packages=[pkname],
	
	install_requires=["PyGObject>=3.40","appdirs>=1.4.3"],
	description='Audio',
	url='https://github.com/colin-i/audaparta',
	author='bot',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	zip_safe=False,
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
