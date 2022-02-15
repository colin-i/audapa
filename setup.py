pkname='audapa'

from setuptools import setup
setup(name=pkname,
	version='1.0.0',
	packages=[pkname],
	#optionals
	python_requires='>=3.8',
	install_requires=[
		"pycairo>=1.20.0","PyGObject>=3.40",
		"appdirs>=1.4.3",
		"PyAudio>=0.2.11"],
	description='Audio',
	url='https://github.com/colin-i/audapa',
	author='colin-i',
	author_email='costin.botescu@gmail.com',
	license='MIT',
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
