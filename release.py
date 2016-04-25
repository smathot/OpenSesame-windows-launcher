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

import sys
import os
import subprocess
import shutil

TEMPLATE = u'''import subprocess
import sys
import os
os.chdir(os.path.dirname(sys.executable))
subprocess.call(['pythonw', 'Scripts/%s'])
'''

if os.path.exists('build'):
	shutil.rmtree('build')
if os.path.exists('dist'):
	shutil.rmtree('dist')

with open(u'opensesame.py', u'w') as fd:
	fd.write(TEMPLATE % u'opensesame.py')
with open(u'opensesamerun.py', u'w') as fd:
	fd.write(TEMPLATE % u'opensesamerun.py')

subprocess.call(['python', 'setup-opensesame.py', 'py2exe'])

os.remove('opensesame.py')
os.remove('opensesamerun.py')
