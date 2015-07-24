from  setuptools import setup, find_packages
import py2exe
import os
import glob
import accessible_output2
setup(
    console=['emu.py'],
    zipfile = None,
    data_files= ['../readme.html'] + accessible_output2.find_datafiles(),
    options = {
        "py2exe":{
            "bundle_files": 1,
            "includes": ['cmd', 'tts', 'accessible_output2', 'libloader', 'platform_utils'],
            "ignores": ['FCNTL', 'System', 'System.IO.Ports', 'TERMIOS', 'clr'],
            "excludes":['_ssl', 'pyreadline', 'difflib', 'doctest', 'optparse', 'pickle', 'calendar']
        }
    }
)