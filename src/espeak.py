import _espeak, cmd, string
class Synth(object):
 def __init__(self):
  _espeak.initialize()
  _espeak.setVoiceByName(cmd.args.voice)
 def speak(self, text):
  _espeak.speak(text)
 def skip(self): pass
 def cancel(self): _espeak.stop()
