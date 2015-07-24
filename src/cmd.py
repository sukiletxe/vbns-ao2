import argparse
parser = argparse.ArgumentParser(prog = "Braille 'n Speak Emulator")
parser.add_argument("comport", metavar = "port", help = "Specifies the COM port to which the emulator connects.")
parser.add_argument("--sapi", nargs = '?', type = int, const = -1, default = 0, help = "If present and blank, a menu will be displayed to choose the SAPI5 voice used by the emulator; if present with a number, the emulator will use the voice corresponding to that number; and if absent, the program will try to detect your screen reader.")
parser.add_argument("--habla", help = "If specified, makes the emulator compatible with Habla", action = "store_true")
args = parser.parse_args()
