# vbns
## Introduction
This is a braille N'Speak emulator, which sends the input from a serial port to a Windows screen reader, SAPI 5 or Espeak-NG. It can be used with a MS-DOS emulator (like Dosbox) and a MS-DOS screen reader (such as asap or habla) to hear the text sent by the screen reader in Windows itself. It was originally created by [Tyler Spivey](https://www.allinaccess.com), and modified by Sukil Etxenike. [Here is the original version](http://batsupport.com/unsupported/dosbox/vbns.zip).

## Speech outputs
This project supports two output methods:

* [One which, as the original version, uses eSpeak](https://github.com/sukiletxe/vbns-espeak)
* And accessible_output2 library, which can interact with many Windows screen readers and SAPI.

## Requirements
You will need Com0Com for the emulator to work properly:

* [Download for Windows XP](http://sourceforge.net/projects/com0com/files/com0com/3.0.0.0/com0com-3.0.0.0-i386-and-x64-unsigned.zip/download)
* [Download for Windows 7 and newer (x64)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x64_signed.exe&can=2&q=)
* [download for Windows 7 and newer (x86)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x86_signed.exe&can=2&q=)

To run the emulator, simply specify the port, and whether you want to use SAPI, Espeak or your screen reader, like this:

`emu com8 --sapi`

Will use the COM8 port (the default one for ASAP in Talking Dosbox), and will open a menu to select a SAPI voice. If you omit the --sapi switch, the screen reader will be automatically detected, and if you append a number to the switch, the voice corresponding to that number in the menu will be used.

To use an Espeak voice:

`emu com8 --espeak-voice=en`

Will use the COM8 port (the default one for ASAP in Talking Dosbox), and the english Espeak voice with the default variant.

### To run from source and compile
You will need:

* Python (I use version 2.7.15).
* accessible_output2, libloader and platform_utils, by Christopher Toth and Tyler Spivey. They are included. They can be downloaded from <http://hg.q-continuum.net>.
* Other dependencies.  Use `pip install -r requirements.txt` to install them, and run `pywin32_postinstall.py -install` afterwards.
* [7-Zip](http://7-zip.org) to compress the compiled executable using the included batch file.

To compile the executable, install `py2exe-py2`, and run `python setup.py py2exe`. Also, to make it run properly, you will need to delete the gen_py folder of the win32com package, usually found at C:\Python27\Lib\site-packages\win32com.

