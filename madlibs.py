from splash import *
from input import *
import story1
import story2
import story3

def madlibs():
    print splash()
    raw_input()
    end = False
    swear = False
    money = False
    joe = False
    harambe = False
    dev = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q":
            print "Good Bye! "
            end = True
        elif option == "c":
            if not swear:
                swear = True
                print "SWEAR MODE ACTIVATED"
            else:
                swear = False
                print "SWEAR MODE DEACTIVATED"
        elif option == "m":
            if not money:
                money = True
                print "YOU HAVE STOLEN 5,000,000 U.S. DOLLARS. YOU MONSTER."
            else:
                swear = False
                print "YOU HAVE BEEN FINE FOR 5,000,000 U.S. DOLLARS. YOU DESERVED IT."
        elif option == "j":
            if not joe:
                joe = True
                print "THE DESTROYER OF WORLDS HAS BEEN UNLEASHED: joe."
            else:
                joe = False
                print "Joe is actually is a guy who helped me test the various modes that have been included. 10/10 Joe!"
        elif option == "h":
            if not harambe:
                harambe = True
                print "HARAMBE SHALL NEVER BE FORGOTTEN"
            else:
                harambe = False
                print "You deactivated Harambe mode. LEAVE. YOU. MONSTER OF AN GORILLA KILLER!!!"
        elif option == "d":
            if not dev:
                dev = True
                print "Congrats on finding this!!!"
            else:
                dev = False
                print "If you found this by accident, go find the other four hacks! And if you found all of them already, congrats, you can brag to your friends hwo you found all of the hacks. NOW LEAVE!"
        elif option == "1":
            print story1.story()
        elif option == "2":
            print story2.story(cheat)
        elif option == "3":
            print story3.story()

madlibs()
