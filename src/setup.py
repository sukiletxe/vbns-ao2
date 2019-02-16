from  setuptools import setup, find_packages
import py2exe
import platform
from glob import glob
import accessible_output2

setup(
    name = "Virtual Braille n'Speak emulator",
    author = "Tyler Spivey, Sukil Etxenike",
    author_email = "sukiletxe@yahoo.es",
    version = "1.0",
    data_files= [("", ['../readme.html'])] + accessible_output2.find_datafiles(),
    packages = find_packages(),
    options = {
        "py2exe":{
            "optimize": 2,
            "dll_excludes": ["CRYPT32.dll"],
            "compressed": True,
        }
    },  
    console=['emu.py'],
)