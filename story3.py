from input import *

#Written James_Gachelin

def story(swear, money, joe, harambe, dev):
    if swear:
        Name1 = getWord("Enter a (sweary) name! ")
        Gender1 = getGender("Enter a gender according to the name you chose! ")
    else: 
        Name1 = getWord("Enter a name! ")
        Gender1 = getGender("Enter a gender according to the name you chose! ")
    
    text = " "
    text += "Once appon a time. "
    text += "There was a boy called " + Name1
    text += " " + Gender1
    text += " was walking to school. Then he fell. "
    text == "The End. "
    
    return text
