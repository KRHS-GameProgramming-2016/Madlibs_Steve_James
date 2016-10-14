def isSwear(word):
    swearList = ["poop",
                 "pee",
                 "cunt",
                 "bitch",
                 "fuck",
                 "slut",
                 "penis",
                 "dick",
                 "phallus",
                 "pussy",
                 "vagina",
                 "phuck",
                 "sloot",
                 "rape",
                 "dick", 
                 "shit",
                 "cock",
                 "cok",
                 "wanker",
                 "ass",
                 "blow",
                 "boner",
                 "bollox",
                 "bullshit",
                 "butt",
                 "clit",
                 "cooner",
                 "cum",
                 "dumbass",
                 "fag",
                 "faggot",
                 "gay",
                 "69",
                 "34",
                 "james",
                 "connar"]
    if word in swearList:
        return True
    else:
        return False
        


def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        for c in response:
            if c != " ":
                goodInput = True
        if not goodInput:
            print "you need something more then just spaces!" 
        elif isSwear(response):
            goodInput = False
            print "U WOT M8? "
        elif len(response) == 0:    #never hit!
            goodInput = False
            print "Type something!!"
        
            
    return response



def getWeapon(prompt):
    goodInput = False
    weapon = "sword, axe, ax, bow, spear, flail, mace, shortsword, longsword, battleaxe, battleax, polearm, billhook, caltrop, halberd, crossbow, pike, poleax, poleaxe, quarterstaff, spear, warhammer"
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in weapon:
                goodInput = False
                print "medival weapon only please!"
    return response







def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print "Numbers only please!"
    return response
