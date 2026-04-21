import textwrap #import textwrap for display purposes
import sys
import time     #import time for dialouge speech delay
import os

a = 2                                           #global variables for time delay
b = 0.2
c = 0.08

inventory = []                                                      #initialize lists
choices = []

def summary():                                                      #creating summary function to display stats at the end of a run
    print("Thank you for playing!")
    print("You have obtained these items:", inventory)
    print("You have made these choices:", choices)
    
    while True:
        choice = input("Unsatisfied with your choices. Would you like to play again? (Y/N): ").lower()

        if choice == "y":                                       #gives player option to restart the game and clears previously made choices and inventory
            inventory.clear()
            choices.clear()
            intro()   
            break
        elif choice == "n":
            print("Thank you for playing!")
            end = input("Press enter to exit")
            sys.exit()
        else:
            print("Invalid option, please enter Y or N.")

def invalidoption():                                                #creating the invalidoption function for invalid inputs from player during choices
    print("You entered an invalid option, please try again")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')                #clears previous text from screen for cleaner display

def intro ():                                                       #define intro section and display
    intro_doc = open("0_intro.txt","r", encoding="utf-8")
    intro_text = intro_doc.read()
    paragraphs = intro_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()                             #blank line between paragraphs
    
    print("                                       * * *")
    next = input("Press Enter to continue")
    print()
intro()

def opening():
    clear_screen()
    opening_doc = open("1_opening.txt","r", encoding="utf-8")
    open_text = opening_doc.read()
    paragraphs = open_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()
opening()

def choice_no_2():                                                  #defining choice for no answer in choice_2, leading to end
    clear_screen()
    choice_2_doc = open("2_choice_no.txt","r", encoding="utf-8")
    choice_2_text = choice_2_doc.read()
    paragraphs = choice_2_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs
    
    choices.append("You chose to not enter the mansion and not help the girl. Who knows what happened to her?")

    print("                                       * * *")
    summary()
    print()

def self_desc(): 
    clear_screen()                                                   #import and display 4th txt file: 4_self_desc
    self_desc_doc = open("4_self_desc.txt","r", encoding="utf-8")
    self_desc_text = self_desc_doc.read()
    paragraphs = self_desc_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()
    inventory.append("Bullwhip")
    print("                                       * * *")
    next = input("Press Enter to continue")
    print()


def choice_yes_3():                                                 #defining choice for yes answer in choice_2, leading to continuing
    clear_screen()
    choice_3_doc = open("3_choice_yes.txt","r", encoding="utf-8")
    choice_3_text = choice_3_doc.read()
    paragraphs = choice_3_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
       #time.sleep(a)
        print()  # blank line between paragraphs

    choices.append("You chose to enter the mansion and help the girl.")

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()
    self_desc()

print("Will you help the girl? yes(y) or no(n)")

while True:                                                         #coding for a choice using while true loop
    choice_1 = input("Enter Y to Help the girl or N to Ignore her: ")
    print()
    if choice_1.lower() == "n":
        choice_no_2()
        break
    elif choice_1.lower() == "y":
        choice_yes_3()
        break
    else:
        invalidoption()


def help_her():                                                    #import and display 5th txt file: 5_help_her
    clear_screen()
    help_her_doc = open("5_help_her.txt","r", encoding="utf-8")
    help_her_text = help_her_doc.read()
    paragraphs = help_her_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()
help_her()

def darkness():                                                     #import and display 6th txt file: 6_darkness_arrives
    clear_screen()
    darkness_doc = open("6_darkness_arrives.txt","r", encoding="utf-8")
    darkness_text = darkness_doc.read()
    paragraphs = darkness_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
    
        print()  # blank line between paragraphs

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()
darkness()

def stand_ground():                                                     #import and display 7th txt file: 7_stand_your_ground
    clear_screen()
    stand_ground_doc = open("7_stand_your_ground.txt","r", encoding="utf-8")
    stand_ground_text = stand_ground_doc.read()
    paragraphs = stand_ground_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    choices.append("You chose to stand and fight the darkness. Your whip wasn't effective. Darkness consumed you.")

    print("                                       * * *")
    summary()
    print()

def dive():                                                     #import and display 8th txt file: 8_dive_to_safety
    clear_screen()
    dive_doc = open("8_dive_to_safety.txt","r", encoding="utf-8")
    dive_text = dive_doc.read()
    paragraphs = dive_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    choices.append("You dove into a nearby room in hopes of survival.")

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()

print("What do you do? (1)Stand your ground or (2)Dive to safety?")     #create choice_2 if/else

choice_2 = input("Enter 1 to Stand your ground or 2 to Dive to safety: ")
print()
if choice_2.lower() == "1":
    stand_ground()
elif choice_2.lower() == "2":
    dive()
else:
    invalidoption()

def pews():                                                     #import and display 9th txt file: 9_pews
    clear_screen()
    pews_doc = open("9_pews.txt","r", encoding="utf-8")
    pews_text = pews_doc.read()
    paragraphs = pews_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    choices.append("You searched the pews.")

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()

    altar()                                                        #continue to altar() after pews()

def altar():                                                     #import and display 10th txt file: 10_altar
    clear_screen()
    altar_doc = open("10_altar.txt","r", encoding="utf-8")
    altar_text = altar_doc.read()
    paragraphs = altar_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    choices.append("You investiaged the altar.")

    print("                                       * * *")
    next = input("Press Enter to continue")
    print()

print("What do you want to do? (1)search the pews or (2)investigate the altar?")     #create choice_2 if/else

choice_3 = input("Enter 1 to search the pews or 2 to investigate the altar: ")
if choice_3 == "1":
    pews()
elif choice_3 == "2":
    altar()
else:
    invalidoption()