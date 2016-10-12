from input import *

#By Steven_Rayno2020

def story():
    Name1 = getWord("Enter a Name! ")
    Mythical1 = getWord("Enter a Mythical Beast! ")
    Weapon1 = getWord("Enter a Medival Weapon! ")
    Name2 = getWord("Enter a Name! ")
    Spell1 = getWord("Enter a Projectile! ")
    
    text = " "
    text += "Once apon a time " + Name1
    text += " was taking a stroll towards the castle. "
    text += "Then suddenly a " + Mythical1
    text += " appeared, destroying the local militia. " + Name1
    text += " whipped out a " + Weapon1
    text += " to quell the beast, but suddenly " + Name1
    text += " Arch nemisis, " + Name2
    text += " appeared, Weilding deadly spells of Magic "
    text += "before shooting a " + Spell1
    text += " at " + Name1
    return text
