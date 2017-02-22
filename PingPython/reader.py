from PingPython import commands

c = commands
print ("Starting PingPython...\nInsert command (add, delete, clear, run, help, exit)")

def reader():
    command = input('-> ')

    if command == 'add':
        c.add()
        reader()

    elif command == 'delete':
        c.delete()
        reader()

    elif command == 'clear':
        c.clear()
        reader()

    elif command == 'run':
        c.run()
        reader()

    elif command == 'exit':
        c.exit()

    else:
        c.help()
        reader()

reader()










