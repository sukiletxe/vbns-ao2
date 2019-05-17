import argparse
parser = argparse.ArgumentParser(prog = "Braille 'n Speak Emulator")
parser.add_argument("port", help = "Specifies the COM port to which the emulator connects.")
parser.add_argument("--sapi", nargs = '?', type = int, const = -1, default = 0, help = "If present and blank, a menu will be displayed to choose the SAPI5 voice used by the emulator; if present with a number, the emulator will use the voice corresponding to that number; and if absent, the program will try to detect your screen reader.")
parser.add_argument( "-ev", "--espeak-voice", default = "en", const="", nargs="?", help = "Specifies the Espeak voice that the emulator will use. This should be given in language[-dialect]+[variant] format, (e. g.: en, en-us, en+max, en-us+max). Note that you can't use --espeak-voice and --sapi together.", dest="espeak")
parser.add_argument("--habla", help = "If specified, makes the emulator compatible with Habla", action = "store_true")
args = parser.parse_args()
