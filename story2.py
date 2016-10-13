from input import *

#By Steven_Rayno2020

def story():
    Name1 = getWord("Enter a Name! ")
    Mythical1 = getWord("Enter a Mythical Beast! ")
    Weapon1 = getWeapon("Enter a Medival Weapon! ")
    Name2 = getWord("Enter another Name! ")
    Spell1 = getMagic("Enter a Projectile! ")
    Year1 = getAmount("Enter a Number! ")
    Nightmare1 = getWord("Enter a scary object! ")
    Money1 = getAmount("Enter an amount! ")
    Name3 = getWord("Enter a malicious name! ")
    
    text = " "
    text += "Once apon a time " + Name1
    text += " was taking a stroll towards the castle. "
    text += "Then suddenly a " + Mythical1
    text += " appeared, destroying the local militia. " + Name1
    text += " whipped out his " + Weapon1
    text += " to quell the beast, but suddenly " + Name1
    text += "'s Arch nemisis, " + Name2
    text += " appeared, Weilding deadly spells of Magic "
    text += "before shooting a " + Spell1
    text += " at " + Name1
    text += " sending him to space for " + Year1
    text += " years. "
    text += " After that " + Name2
    text += " Went to the bar to drink his problems away. "
    text += " After spending his " + Money1
    text += " dollars at the bar, " + Name2
    text += " Wobbled away from the bar, drunk out of his mind. " + Name2
    text += " Went back to his master, " + Name3
    return text
