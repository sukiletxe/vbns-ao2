import accessible_output2.outputs as ao2
import cmd
def speak(text, interrupt = False):
    global o
    o.speak(text, interrupt)

def silence():
    try:
        o.silence()
    except:
        pass

def get_output():
    global o
    if o.name == "Unnamed Output":
        return o.get_first_available_output()
    return o

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

def set_output(output):
    global o, vlist
    if output != 0:
        o = ao2.sapi5.SAPI5()
        vlist = o.list_voices()
        if output == -1:
            menu()
        else:
            o.set_voice(vlist[cmd.args.sapi-1])
    else:
        o = ao2.auto.Auto()
        o = get_output()