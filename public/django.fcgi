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

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
