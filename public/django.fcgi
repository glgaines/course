#!/usr/bin/python
import os
import sys
import site

# setup the virtualenv
venv_path = '/home/faunris/venv'
os.environ['VIRTUAL_ENV'] = venv_path
execfile('%s/bin/activate_this.py' % venv_path, dict(__file__= '%s/bin/activate_this.py' % venv_path) )

# Loop over the directory with eggs and add them to the PYTHONPATH
import glob
for dir in glob.glob(os.environ['VIRTUAL_ENV'] + '/src/*'):
    if os.path.isdir(dir):
        site.addsitedir(dir)

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))
sys.path.insert(0, _PROJECT_DIR)
_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
