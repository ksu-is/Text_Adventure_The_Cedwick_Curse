import textwrap #import textwrap for display purposes

inventory = [] #initialize lists
choices = []
dialogue_list= []

#def summary():
    #print("Thank you for playing!")
    #print("You have obtained these items:", inventory)
    #print("You have made these choices:", choices)
    #print("You decided to say this: ", dialouge_list)

#def intro():
text = "There was once a mansion that belonged to a family in the early 1900s, the Cedwicks."
print(textwrap.fill(text, width=80))
print()
text = "As their wealth grew, however, so did their greed."  
print(textwrap.fill(text, width=80))
text = "The Cedwick family had Frank, Jane and Aelita their daughter. They had maids and landscapers take care of the house and of Aeita, while Frank and Jane went away on vacation after vacation or to the next factory site."
print(textwrap.fill(text, width=80))
text ="It was Hallow's Eve and Frank's company broke ground on a new factory, a top of an ancient Burial ground."
print(textwrap.fill(text, width=80))
print()
text = "'You have trespassed on our land and tarnished out sacred place!', an old ghastly witch doctor shouted at Frank."
print(textwrap.fill(text, width=80))
print()
text ="'Forever and on you shall never die. Until a man with a fear of snakes comes and this curse will live on foreever!'"
print(textwrap.fill(text, width=80))
print()
text = "The witch doctor raised her arms, swirled her staff around as a bolt of lightning crashed down from the sky and struck Frank."
print(textwrap.fill(text,width=80))
print()
text = "Nothing was left of them. Aelita inherited the business but died tragically of starvation once the maids absconded with the Cedwick’s wealth. Her family roamed their ill-fated house as spectres, desperate to save what they had left of their ‘fortune’."
print(textwrap.fill(text,width=80))
print()