# vbns-AO2
## Introduction
This is a braille N'Speak emulator, which works with MS-DOS screen readers. It was originally created by [Tyler Spivey](https://www.allinaccess.com), and modified by Sukil Etxenike. [Here is the original version](http://batsupport.com/unsupported/dosbox/vbns.zip).

## Variants
This project has two versions:
* [One  which, as the original version, uses eSpeak](https://github.com/sukiletxe/vbns-espeak)
* And this one, which can interact with many Windows screen readers and SAPI.

## Requirements
You will need Com0Com for the emulator to work properly:
* [Download for Windows XP](http://sourceforge.net/projects/com0com/files/com0com/3.0.0.0/com0com-3.0.0.0-i386-and-x64-unsigned.zip/download)
* [Download for Windows 7 and newer (x64)](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x64_signed.exe&can=2&q=)
* [download for Windows 7 and newer (x86](http://code.google.com/p/powersdr-iq/downloads/detail?name=setup_com0com_W7_x86_signed.exe&can=2&q=)

To run the emulator, simply specify the port, and whether you want to use SAPI, like this:

emu com8 --sapi

Will use the COM8 port (the default one for ASAP in Talking Dosbox), and will open a menu to select a SAPI voice. If you omit the --sapi switch, the screen reader will be automatically detected, and if you append a number to the switch, the voice corresponding to that number in the menu will be used.

Note: If the detected screen reader is JAWS or you choose to use SAPI, you may see a message like this:

>Rebuilding cache of generated files for COM support...
> Checking 105C4321-CB93-11D4-9839-00C0F0214711x0x1x0
> Checking C866CA3A-32F7-11D2-9602-00C04F8EE628x0x5x4
> Done.

This is a warning (not an error) of Python, which as far as I know, can't be removed. However, it can be safely ignored, as the program will run properly.

### To run from source and compile
You will need:
* Python (I use version 2.7.10).
* Pyserial (you can install it using PIP)
* [Python for Windows Extensions](http://sourceforge.net/projects/pywin32/)
* accessible_output2, libloader and platform_utils, by Christopher Toth and Tyler Spivey. They are included, although they can be downloaded from <http://hg.q-continuum.net>.
* [Pandoc](http://pandoc.org/) to generate the documentation.

You will need py2exe to make a compiled executable. Also, to make the compiled executable run properly, you will need to delete the gen_py folder of the win32com package, usually found at C:\Python27\Lib\site-packages\win32com.

