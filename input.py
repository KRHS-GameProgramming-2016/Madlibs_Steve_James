#Improved by Steven_Rayno2020, tested by Jpoltack :D
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
                 "piss",
                 "jizz",
                 "kunt",
                 "mcfagget",
                 "feg",
                 "feggot",
                 "muff",
                 "negro",
                 "nigga",
                 "pecker",
                 "poon",
                 "prick",
                 "renob",
                 "shiz",
                 "snatch",
                 "splooge",
                 "tard",
                 "testicle",
                 "tits",
                 "tit",
                 "twats",
                 "taint",
                 "vag",
                 "whore",
                 "wank",
                 "sex",
                 "sexy",
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
                     "c",
                     "m",
                     "j",
                     "h",
                     "d",
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
            print "TRIGGERED1!!11!1 "
        elif len(response) == 0:    #never hit!
            goodInput = False
            print "Type something!!"
        
            
    return response

#By Steven_Rayno2020
def getSwear(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        for c in response:
            if c != " ":
                goodInput = True
        if not goodInput:
            print "you need something more then just spaces!" 
        elif not isSwear(response):
            goodInput = False
            print "TRIGGERED1!!11!1 IT'S NOT SWEARY ENOUGH"
        elif len(response) == 0:    #never hit!
            goodInput = False
            print "Type something!!"
    return response

#By Steven_Rayno2020
def getWeapon(prompt):
    goodInput = False
    weapons = ["sword",
               "axe",
               "ax",
               "bow",
               "spear",
               "flail",
               "mace",
               "shortsword",
               "longsword",
               "battleaxe",
               "battleax",
               "polearm",
               "billhook",
               "caltrop",
               "halberd",
               "crossbow",
               "pike",
               "poleax",
               "poleaxe",
               "quarterstaff",
               "spear",
               "warhammer"]
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if response not in weapons:
            goodInput = False
            print "Medival Weapon only please!"
            
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
            elif isSwear(response):
                goodInput = False
                print "TRIGGERED1!!11!1 "
    return response
