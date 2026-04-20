import textwrap #import textwrap for display purposes
import sys
import time #import time for dialouge speech delay

a = 2
b = 0.2
c =0.08

inventory = [] #initialize lists
choices = []


def summary():
    print("Thank you for playing!")
    print("You have obtained these items:", inventory)
    print("You have made these choices:", choices)
    end = input("Press Enter to exit")
   

def invalidoption():  #creating the invalidoption function for invalid inputs from player
    print("You entered an invalid option, please try again")

def intro ():           #define intro section and display
    intro_doc = open("0_intro.txt","r", encoding="utf-8")
    intro_text = intro_doc.read()
    paragraphs = intro_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs
    
    print("                                       * * *")
    next = input("Press Enter to continue")
intro()

def opening():
    opening_doc = open("1_opening.txt","r", encoding="utf-8")
    open_text = opening_doc.read()
    paragraphs = open_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    print("                                       * * *")
    next = input("Press Enter to continue")
opening()

def choice_no_2():  #defining choice for no answer in choice_2, leading to end
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
    
def choice_yes_3():    #defining choice for yes answer in choice_2, leading to continuing
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

print("Will you help the girl? yes(y) or no(n)")

choice_2 = input("Enter Y to Help the girl or N to Ignore her: ")
if choice_2.lower() == "n":
    choice_no_2()
elif choice_2.lower() == "y":
    choice_yes_3()
else:
    invalidoption()


def self_desc():   #import and display 4th txt file
    self_desc_doc = open("4_self_desc.txt","r", encoding="utf-8")
    self_desc_text = self_desc_doc.read()
    paragraphs = self_desc_text.split("/n/n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        time.sleep(a)
        print()

print("                                       * * *")
next = input("Press Enter to continue")
print()

def help_her():                                                    #import and display 5th txt file: 5_help_her
    help_her_doc = open("5_help_her.txt","r", encoding="utf-8")
    help_her_text = help_her_doc.read()
    paragraphs = help_her_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    print("                                       * * *")
    next = input("Press Enter to continue")
help_her()

def help_her():                                                     #import and display 5th txt file: 6_darkness_arrives
    help_her_doc = open("5_help_her.txt","r", encoding="utf-8")
    help_her_text = help_her_doc.read()
    paragraphs = help_her_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=90))
        #time.sleep(a)
        print()  # blank line between paragraphs

    print("                                       * * *")
    next = input("Press Enter to continue")
help_her()