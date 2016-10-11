from splash import *
from input import *
import story1
import story2

def madlibs():
    print splash()
    raw_input()
    end = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q ": 
            end = True
        elif option == "1":
            print story1.story()
        elif option == "3":
            print story3.story()


madlibs()
