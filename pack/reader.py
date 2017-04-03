import comms


print("PPPPPPPPP                        PPPPPPPPP           PP    PP\n"
      "PPP     PP   PP                  PPP     PP          PP    PP\n"
      "PPP     PPP      PP       PPPPP  PPP     PPP        PPPP   PPPPPP  PPPPPP  PP\n"
      "PPP     PP   PP  PPPPP   PP  PP  PPP     PP  PP  PP  PP    PP  PP  PP  PP  PPPPP\n"
      "PPPPPPPPP    PP  PP  PP   PPPPP  PPPPPPPPP    PPPP   PPPP  PP  PP  PPPPPP  PP  PP\n"
      "PPP                          PP  PPP           PP\n"
      "PPP                      PP  PP  PPP          PP\n"
      "PPP                       PPPP   PPP         PP\n"
      "\nStarting PingPython...\nEnter input add delete clear list run exit help")
c = comms;

# needs to be 'real' commandline
def reader():
    inn = input("Enter command")

    if inn == "add" or inn == "a":
        c.add()
    elif inn == "addmore" or inn == "am":
        c.addmore()
    elif inn == "delete" or inn == "del" or inn == "d":
        c.delete()
    elif inn == "clear" or inn == "clr" or inn == "c":
        c.clear()
    elif inn == "list" or inn == "lst" or inn == "l":
        c.list()
    elif inn == "run" or inn == "r":
        c.run()
    elif inn == "exit" or inn == "quit" or inn == "e" or inn == "q":
        c.exit()
    elif inn == "readfromfile" or inn == "rf" or inn == "read" or inn == "f":
        c.readFromFile()
    elif inn == "savetofile" or inn == "sf" or inn == "save" or inn == "s":
        c.readFromFile()
    elif inn == "help" or inn == "h":
        c.help()
    else:
        print("Something went wrong. For help please enter 'help' or 'h'")
    reader()


reader()



