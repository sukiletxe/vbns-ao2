from  setuptools import setup, find_packages
import py2exe
import platform, fnmatch, os
from glob import glob
import accessible_output2
def get_data():
  if platform.architecture()[0][:2] == "32":
   return [("Microsoft.VC90.CRT", glob("windows_vc++/msvc32/Microsoft.VC90.CRT/*"))]
  elif platform.architecture()[0][:2] == "64":
   return [("Microsoft.VC90.CRT", glob("windows_vc++/msvc64/Microsoft.VC90.CRT/*"))]

def get_espeak():
    answer = []
    tmp = []
    for root, dirs, files in os.walk("espeak-data"):
        for item in glob(os.path.join(root, "*")):
            if os.path.isfile(item):
                tmp.append(item)
        new = (root, tmp)
        tmp = []
        answer.append(new)
    answer.append(("", ["espeak.dll"]))
    return answer

setup(
    name = "Virtual Braille n'Speak emulator",
    author = "Tyler Spivey, Sukil Etxenike",
    author_email = "sukiletxe@yahoo.es",
    version = "1.0",
    data_files= [("", ['../readme.html'])] + accessible_output2.find_datafiles()+get_data()+get_espeak(),
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