import argparse, os, sys
from configobj import ConfigObj
merged = argparse.namespace() # Used to merge config and command line

def parse_cmd(namespace):
    """
    Code that parses the command line, previously top level.
    """
    description = "This is a Braille n'speak emulator which receives input from a serial port (which can be emulated) and outputs it to a Windows screen reader, SAPI 5 or espeak-ng."
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("port", nargs = "?", default = "com8", help = "Specifies the COM port to which the emulator connects.")
    parser.add_argument("--sapi", nargs = '?', type = int, const = -1, default = 0, help = "If present and blank, a menu will be displayed to choose the SAPI5 voice used by the emulator; if present with a number, the emulator will use the voice corresponding to that number; and if absent, the program will try to detect your screen reader.")
    parser.add_argument( "-ev", "--espeak-voice", default = "", const="en", nargs="?", help = "Specifies the Espeak voice that the emulator will use. This should be given in language[-dialect]+[variant] format, (e. g.: en, en-us, en+max, en-us+max). Note that you can't use --espeak-voice and --sapi together.", dest="espeak")
    parser.add_argument("--habla", help = "If specified, makes the emulator compatible with Habla", action = "store_true")
    # We merge the configuration options with the command line ones.
    return parser.parse_args(namespace= namespace)

def parse_config(namespace, config = 'emu.ini'):
    """
    Parse configuration file.
    """
    if os.path.exists(os.path.join(os.curdir, config):
        cdict = ConfigObj(config)
        # Put config in our namespace
        for key, value in cdict:
            setattr(namespace, key, value)
    return namespace

args = parse_cmd(parse_config(merged))
