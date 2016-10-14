from input import *

#By Steven_Rayno2020

def story():
    Name1 = getWord("Enter a Name! ")
    Mythical1 = getWord("Enter a Mythical Beast! ")
    Weapon1 = getWeapon("Enter a Medival Weapon! ")
    Name2 = getWord("Enter another Name! ")
    Spell1 = getWord("Enter a Projectile! ")
    Year1 = getNumber("Enter a Number! ")
    Nightmare1 = getWord("Enter a scary object! ")
    Money1 = getNumber("Enter an amount! ")
    Name3 = getWord("Enter a malicious name! ")
    Year2 = getNumber("Enetr a Number plz! ")
    
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
    text += " Went back to his master, Sir " + Name3
    text += " Before " + Name1
    text += " made a dramtic entrance before shooting " + Name2
    text += " and " + Name3
    text += " to space for " + Year2
    text += " years."
    return text
