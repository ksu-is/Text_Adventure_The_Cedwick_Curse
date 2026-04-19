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

intro_doc = open("0_intro.txt","r", encoding="utf-8")
intro_text = intro_doc.read()
paragraphs = intro_text.split("\n\n")

for p in paragraphs:
    print(textwrap.fill(p, width=80))
    print()  # blank line between paragraphs
