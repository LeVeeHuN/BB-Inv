from os import system
import sys

def cls():
    if sys.platform == "win32":
        system("cls")
    elif sys.platform == "linux":
        system("clear")
    else:
        print("Console clear is not implemented yet on this platform.")
        print("Please contact the developer on the following e-mail and describe the problem and the system you are using.")
        print("levente@bbco.hu")
        try:
            system("clear")
        except:
            pass