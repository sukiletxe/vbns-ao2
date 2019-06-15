# vbns
## Introduction
This is a braille N'Speak emulator, which works with MS-DOS screen readers. If a MS-DOS screen reader (such as ASAP or Habla) is run in a MS-DOS emulator, for example Dosbox, and the propper software is installed (see below) a screen reader of eSpeak will output the information sent to the MS-DOS screen reader. It was originally created by [Tyler Spivey](https://www.allinaccess.com), and modified by Sukil Etxenike. [Here is the original version](http://batsupport.com/unsupported/dosbox/vbns.zip).

## Speech outputs
This project supports two output methods:

* [One  which, as the original version, uses eSpeak](https://github.com/sukiletxe/vbns-espeak)
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
* accessible_output2, libloader and platform_utils, by Christopher Toth and Tyler Spivey. They are included and the first one is modified. The originals can be downloaded from <http://hg.q-continuum.net>.
* Markdown, pywin32, and pyserial (install using pip, and run `pywin32_postinstall.py -install` afterwards).
* [7-Zip](http://7-zip.org) to compress the compiled executable using the included batch file.

You will need py2exe to make a compiled executable. Also, to make the compiled executable run properly, you will need to delete the gen_py folder of the win32com package, usually found at C:\Python27\Lib\site-packages\win32com.

