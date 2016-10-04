def getMenuOption():
    goodInput = False
    goodResponses = [ "1",
                      "2",
                      "3",
                      "q"]
    while not goodinput:
        response = raw_input("Make a selection! ")
        if response.lower() to in goodResponses:
            goodInput = True
            else:
            print "Please make a valid selection "
    return response.lower()


def getWord(promt):
    goodInput = False
    while not goodinput:
        response = raw_input(promt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Get ur moind out of teh gutter plz. "
