pkname='audapa'

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
