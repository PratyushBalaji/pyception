import os

def program():
    print("Welcome to the python program that runs python programs")
    print()
    path = input("What is the directory of the file? : ")
    os.system("cd "+path)
    print("These are all the python files in this directory : ")
    input("Press 'enter' to continue")
    os.system("dir /S *.py")
    print()
    print()
    print()
    filename = input("What is the file you want to run? (Include '.py') : ")
    print()
    input("Press enter to run the file")
    os.system("py "+filename)

program()