from splash import *
from input import *
import story1
import story2
import story3

def madlibs():
    print splash()
    raw_input()
    end = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q":
            print "Good Bye! "
            end = True
        elif option == "c":
            pass
        elif option == "1":
            print story1.story()
        elif option == "2":
            print story2.story()
        elif option == "3":
            print story3.story()


madlibs()
