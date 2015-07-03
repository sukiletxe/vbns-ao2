import argparse
parser = argparse.ArgumentParser(prog = "Braille'n Speak Emulator")
parser.add_argument("comport", metavar = "port", help = "Specifies the COM port to which the emulator connects.")
parser.add_argument("voice", help = "Specifies the Espeak voice that the emulator will use. This should be given in language[-dialect]+[variant] format, (e. g.: en, en-us, en+max, en-us+max).")
parser.add_argument("--habla", help = "If specified, makes the emulator compatible with Habla", action = "store_true")
args = parser.parse_args()
