import comms


print("Starting PingPython...\nEnter input add delete clear list run exit help")
c = comms;


def reader():
    inn = input("Enter command")

    if inn == "add" or inn == "a":
        c.add()
        reader()
    elif inn == "addmore" or inn == "am":
        c.addmore()
        reader()
    elif inn == "delete" or inn == "del" or inn == "d":
        c.delete()
        reader()
    elif inn == "clear" or inn == "clr" or inn == "c":
        c.clear()
        reader()
    elif inn == "list" or inn == "lst" or inn == "l":
        c.list()
        reader()
    elif inn == "run" or inn == "r":
        c.run()
        reader()
    elif inn == "exit" or inn == "quit" or inn == "e" or inn == "q":
        c.exit()
    else:
        c.help()
        reader()


reader()



