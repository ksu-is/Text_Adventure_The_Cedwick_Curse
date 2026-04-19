import textwrap #import textwrap for display purposes
import sys
import time #import time for dialouge speech delay

a = 2
b = 0.2
c =0.08

inventory = [] #initialize lists
choices = []
dialogue_list= []

#def summary():
    #print("Thank you for playing!")
    #print("You have obtained these items:", inventory)
    #print("You have made these choices:", choices)
    #print("You decided to say this: ", dialouge_list)

def invalidoption():  #creating the invalidoption function for invalid inputs from player
    print("You entered an invalid option, please try again")

def intro ():           #define intro section and display
    intro_doc = open("0_intro.txt","r", encoding="utf-8")
    intro_text = intro_doc.read()
    paragraphs = intro_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=110))
        print()  # blank line between paragraphs
    
    print("                                       * * *")
intro()

def opening():
    opening_doc = open("1_opening.txt","r", encoding="utf-8")
    open_text = opening_doc.read()
    paragraphs = open_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=110))
        print()  # blank line between paragraphs

    print("                                       * * *")
opening()

def choice_no_2():  #defining choice for no answer in choice_2, leading to end
    choice_2_doc = open("2_choice_no.txt","r", encoding="utf-8")
    choice_2_text = choice_2_doc.read()
    paragraphs = choice_2_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=110))
        print()  # blank line between paragraphs

    print("                                       * * *")
    
def choice_yes_3():    #defining choice for yes answer in choice_2, leading to continuing
    choice_3_doc = open("3_choice_yes.txt","r", encoding="utf-8")
    choice_3_text = choice_3_doc.read()
    paragraphs = choice_3_text.split("\n\n")

    for p in paragraphs:
        print(textwrap.fill(p, width=110))
        print()  # blank line between paragraphs

    print("                                       * * *")

print("Will you help the girl? 2(no), or 3(yes)")

choice_2 = input("Enter 2 to Not help the girl or 3 to Yes, Help the girl")
if choice_2 == "2":
    choice_no_2()
elif choice_2 == "3":
    choice_yes_3()
else:
    invalidoption()


