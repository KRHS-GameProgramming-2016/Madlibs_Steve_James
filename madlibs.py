from splash import *
from input import *
import story1
import story2
import story3

def madlibs():
    print splash()
    raw_input()
    end = False
    cheat = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q":
            print "Good Bye! "
            end = True
        elif option == "c":
            if not cheat:
                cheat = True
                print "CHEAT ACTIVATED"
            else:
                cheat = False
                print "CHEAT DEACTIVATED"
        elif option == "1":
            print story1.story()
        elif option == "2":
            print story2.story(cheat)
        elif option == "3":
            print story3.story()

madlibs()
