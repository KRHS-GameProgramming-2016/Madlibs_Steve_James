from input import *

#By Steven_Rayno2020

def story():
    Name1 = getWord("Enter a Name! ")
    Mythical1 = getWord("Enter a Mythical Beast! ")
    Weapon1 = getWord("Enter a Medival Weapon! ")
    
    text = " "
    text += "Once apon a time " + Name1
    text += " was taking a stroll downtown "
    text += "then suddenly a " + Mythical1
    text += " was rampaging down the sidewalk. " + Name1
    text += " whipped out a " + Weapon1
    text += " to quell the beast "
    return text
