import _espeak, cmd, string
class Synth(object):
 def __init__(self):
  _espeak.initialize()
  _espeak.setVoiceByName(cmd.args.espeak)
 def speak(self, text):
  _espeak.speak(text.decode("cp437"))
 def skip(self): pass
 def cancel(self): _espeak.stop()
