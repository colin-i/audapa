pkname='audapa'

from setuptools import setup
setup(name=pkname,
	version='1.0.0',
	packages=[pkname],
	#optionals
	python_requires='>=3.8',
	install_requires=["PyGObject>=3.40","appdirs>=1.4.3","PyAudio>=0.2.11",
		"Wave>=0.0.2"],
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
