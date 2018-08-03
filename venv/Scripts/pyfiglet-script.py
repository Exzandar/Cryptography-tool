#!F:\Python\PROJ1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyfiglet==0.7.5','console_scripts','pyfiglet'
__requires__ = 'pyfiglet==0.7.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyfiglet==0.7.5', 'console_scripts', 'pyfiglet')()
    )
