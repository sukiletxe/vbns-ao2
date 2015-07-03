# vbns-AO2
This is a braille N'Speak emulator, which works with MS-DOS screen readers. It was originally created by [Tyler Spivey](https://www.allinaccess.com), and modified by Sukil Etxenike. [Here is the original version](http://batsupport.com/unsupported/dosbox/vbns.zip).

This project has two versions:
* [One  which, as the original version, uses eSpeak](https://github.com/sukiletxe/vbns-espeak)
* And this one, which can interact with many Windows screen readers and SAPI.

Note that at this stage, this version is **not** ready to be even tested. It actually has no difference with the eSpeak version.

## Requirements
You will need Com0Com for the emulator to work properly:
* [Download for Windows XP](http://sourceforge.net/projects/com0com/files/com0com/3.0.0.0/com0com-3.0.0.0-i386-and-x64-unsigned.zip/download)
* [Download for Windows 7 and newer (x64)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x64_signed.exe&can=2&q=)
* [download for Windows 7 and newer (x86](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x86_signed.exe&can=2&q=)

### To run from source and compile
You will need:
* Python (I use version 2.7.10).
* Pyserial
* accessible_output2 and libloader, get them from <http://hg.q-continuum.net>

You will need py2exe to make a compiled executable.

