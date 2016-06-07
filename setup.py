#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

setup(name=u"opensesame-windows-launcher",
	version='0.3.4',
	description=u"A graphical experiment builder for the social sciences",
	author=u"Sebastiaan Mathot",
	author_email=u"s.mathot@cogsci.nl",
	url=u"http://osdoc.cogsci.nl/",
	include_package_data=False,
	packages=[],
	data_files=[(u'', [
		'dist/library.zip',
		'dist/opensesame.exe',
		'dist/opensesamerun.exe'
		]),
		([u'Scripts', [
		'safelaunch-opensesame.py',
		'safelaunch-opensesamerun.py'
		]])],
	install_requires=['python-opensesame'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
		],
	)
