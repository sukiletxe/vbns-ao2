import serial, threading, cStringIO, cmd, time
import string
import tts
import sys, fix_win32com
if hasattr(sys, "frozen"):
    fix_win32com.fix()
rate_map = (-10, -8, -6, -4, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
rate, pitch = 5, 5
tts.set_output(cmd.args.sapi)
tts.speak("ready", True)
port = serial.serial_for_url(cmd.args.port, 9600)
port.setDsrDtr(0)
cmdchar = '\x05'
buffer = cStringIO.StringIO()
in_command = False
num=""
lst=[]
stopped=True
def parse(ch):
 global in_command, num, lst
 if ch == '\x18':
  reset()
  tts.silence()
 elif ch == cmdchar:
  in_command = True
 elif in_command and ch in string.digits:
  num += ch
 elif in_command and ch in string.letters:
  in_command = False
  if buffer.tell() > 0:
   lst.append(buffer.getvalue())
   buffer.reset()
   buffer.truncate()
  if ch in handlers:
   lst.append((handlers[ch], int(num)))
  num=""
 elif in_command: #fall through, unrecognized char
  in_command = False
  return
 elif not in_command and (ch == '\r' or ch == '\0'):
  if ch == '\0': port.write('\0')
  if buffer.tell() > 0: lst.append(buffer.getvalue())
  process(lst)
  reset()
 else:
  buffer.write(ch)
def process(lst):
 sb = cStringIO.StringIO()
 for item in lst:
  if isinstance(item, basestring):
   sb.write(item)
  elif isinstance(item, tuple):
   sb.write(item[0](item[1]))
 v = sb.getvalue()
 if v.strip() == '': return
 tts.speak(v, False)

def speed(x):
 return "\x01%dS " % rate_map[x]
def pitch(x):
 return ""
def reset():
 global buffer, lst, in_command, num
 buffer.reset()
 buffer.truncate()
 lst = []
 num=""
 in_command=False
handlers = {
'E': speed,
'P': pitch
}
def stop():
 global stopped
 stopped=True
 parse('\r')
def habla():
 t=threading.Timer(0.3, stop)
 t.start()
while True:
 parse(port.read(1))
 if cmd.args.habla == True and stopped==True:
  stopped=False
  habla()
(1)