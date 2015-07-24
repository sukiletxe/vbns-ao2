import accessible_output2.outputs as ao2
import cmd
def speak(text, interrupt):
    global o
    o.speak(text, interrupt = 0)

def menu():
    global o, vlist
    print ("Select a voice from the following menu.")
    for item in range(0, len(vlist)):
        print("%d: %s" %(item+1, vlist[item]))
    print ("0: Use automatic output instead")
    v = raw_input(">")
    v=int(v)-1
    if v == -1:
        o = ao2.auto.Auto()
    elif v >= 0 and v <= len(vlist):
        o.set_voice(vlist[v])
    else:
        print("Invalid option.")
        menu()

def set_output():
    global o, vlist
    if cmd.args.sapi == 0:
        o = ao2.auto.Auto()
    else:
        o = ao2.sapi5.SAPI5()
        vlist = o.list_voices()
        if cmd.args.sapi == -1:
            menu()
        else:
            o.set_voice(vlist[cmd.args.sapi-1])
