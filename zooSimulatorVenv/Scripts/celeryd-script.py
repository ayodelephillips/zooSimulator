#!c:\users\sammy\dev\zoosimulator\zoosimulatorvenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'celery==3.1.26.post2','console_scripts','celeryd'
__requires__ = 'celery==3.1.26.post2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('celery==3.1.26.post2', 'console_scripts', 'celeryd')()
    )
