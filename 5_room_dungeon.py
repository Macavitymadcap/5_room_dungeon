# Imports
from time import sleep
from random import randint

# Variables
professions = ["fighter", "mage", "rogue"]
yes_no = ["yes", "no",]
directions = ["north", "south", "east", "west"]

# Character Creation
name = input("Well met adventurer! What is your name?\n")
sleep(1)
print("\nAhh, " + name + ": a warrior's name!\n")
sleep(2)
print("Or is it? What is your profession?")
sleep(1)
profession = ""
while profession not in professions:
  profession = input("fighter/mage/rogue\n")
  if profession == "fighter":
    sleep(1)
    print("\nStab things and ask questions later, I like your style. \n")
  elif profession == "mage":
    sleep(1)
    print("\nWhen in doubt, set it aflame: a noble strategy.\n")
  elif profession == "rogue":
    sleep(1)
    print("\nSome say sneaking around lacks honour; I say it keeps you alive.\n")
  else:
    sleep(1)
    print("\nThese are basic-bitch rules: choose one of the classes stated below by typing it as you see it written.\n")
sleep(2)
print(name + " the " + profession + ", are you ready to face ...\n")
sleep(2)
print("THE FIVE ROOM DUNGEON?\n")
sleep(2)
response = ""
while response not in yes_no:
  print("Well, are you?")
  sleep(1)
  response = input("yes/no\n")
  if response == "yes":
    sleep(1)
    print("\nA wise choice! Your story begins ...\n")
  elif response == "no":
    sleep(1)
    print("\nWell that was an anti-climax.\n")
    sleep(2)
    print("Goodbye.\n")
    quit()
  else:
    sleep(1)
    print("\nIt's a yes/no question pal.\n")
sleep(2)

# Prologue
print("Legend tells of a dungeon not far from town said to contain treasures of incalculable wealth ...\n")
sleep(5)
print("Incalculable not only because no one knows what the treasures are, but also because none have such wealth with which the treasures could be compared ...\n")
sleep(5)
print("Chief among the dungeon's claims to fame, however, is that no one has ever retrieved the treasures contained therein ...\n")
sleep(5)
print("For the dungeon is filled with perilous puzzles, tyrannous traps, mighty monsters and other such alliterative dangers ...\n")
sleep(5)
if profession == "fighter":
  print("Being a mighty fighter, however, believe you have the strength needed to overcome the obstacles inside the dungeon ...\n")
elif profession == "mage":
  print("Being a wise mage, however, you know you have the necessary intelligence to best the perils contained within dungeon ...\n")
else:
  print("Being a crafty rogue, however, you reckon you have the guile required to sneak through the dungeon and come back out treasure in hand ...\n")
sleep(5)
print("And so you head off out of town in search of wealth, glory, and (most importantly) the entrance to the dungeon.\n")
sleep(5)

# Room 1 - Entrance

