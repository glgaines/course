#!/usr/bin/env python
import os
import sys
import site

if __name__ == "__main__":
    if sys.platform.startswith('linux'):
        # Linux-specific code here...
        # setup the virtualenv
        try:
            venv_path = '/home/faunris/venv'
            os.environ['VIRTUAL_ENV'] = venv_path
            execfile('%s/bin/activate_this.py' % venv_path, dict(__file__= '%s/bin/activate_this.py' % venv_path) )

            # Loop over the directory with eggs and add them to the PYTHONPATH
            import glob
            for dir in glob.glob(os.environ['VIRTUAL_ENV'] + '/src/*'):
                if os.path.isdir(dir):
                    site.addsitedir(dir)
        except IOError:
            del os.environ['VIRTUAL_ENV']
#    _PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#    sys.path.insert(0, os.path.dirname(_PROJECT_DIR))
#    _PROJECT_NAME = _PROJECT_DIR.split('/')[-1]
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
