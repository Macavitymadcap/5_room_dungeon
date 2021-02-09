# Imports
from time import sleep
from random import randint

# Variables
professions = ["fighter", "mage", "rogue"]
yes_no = ["yes", "no",]
directions = ["north", "south", "east", "west"]

# Dice
d4 = randint(1, 4)
d6 = randint(1, 6)
d8 = randint(1, 8)
d10 = randint(1, 10)
d12 = randint(1, 12)
d20 = randint(1, 20)
d100 = randint(1, 100)

# Classes
class Character:
  def __init__(self, name, hit_points, armour_class, attack_name, attack_bonus, attack_damage):
    self.name = name
    self.hit_points = hit_points
    self.armour_class = armour_class
    self.attack_name = attack_name
    self.attack_bonus = attack_bonus
    self.attack_damage = attack_damage
    
  def damage(self, take_damage = 0):
    self.hit_points -= take_damage
  
  def heal(self, heal_value = 0):
    self.hit_points += heal_value
  
  def attack(self, ac):
    roll = d20 + self.attack_bonus
    if roll >= ac:
      print("The " + self.name + " rolls " + str(roll) + " to attack with its " + self.attack_name + " dealing " + str(self.attack_damage) + " damage.")
    else:
      print("The " + self.name + " rolls " + str(roll) + " to attack with its " + self.attack_name + " and misses.")
      
# Instances
fighter= Character("fighter", 10, 17, "longsword", 5, d8 + 3)
goblin = Character("goblin", 7, 15, "scimitar", 5, d6 + 2)


# Character Creation
name = input("Well met adventurer! What is your name?\n")
sleep(1)
print("\nAhh, " + name + ": a warrior's name!\n")
sleep(2)
print("Or is it? Choose your class:")
sleep(1)
profession = ""
while profession not in professions:
  profession = input("fighter/mage/rogue\n")
  if profession == "fighter":
    sleep(1)
    print("\nStab things and ask questions later, I like your style.\n")
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
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
sleep(2)
# Prologue
print("Legend tells of a dungeon not far from town said to contain treasures of incalculable wealth ...\n")
sleep(4)
print("Incalculable not only because no one knows what the treasures are, but also because none have such wealth with which the treasures could be compared ...\n")
sleep(6)
print("Chief among the dungeon's claims to fame, however, is that no one has ever retrieved the treasures contained therein ...\n")
sleep(5)
print("For the dungeon is filled with perilous puzzles, tyrannous traps, mighty monsters and other such alliterative dangers ...\n")
sleep(5)
if profession == "fighter":
  print("Being a mighty fighter, however, believe you have the strength needed to overcome the obstacles inside the dungeon ...\n")
elif profession == "mage":
  print("Being a wise mage, however, you know you have the necessary intelligence to best the perils contained within dungeon ...\n")
else:
  print("Being a crafty rogue, however, you reckon you have the guile required to sneak through the dungeon grab the treasure ...\n")
sleep(5)
print("And so you head off out of town in search of wealth, glory, and (most importantly) the entrance to the dungeon.\n")
sleep(5)
print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
sleep(2)

# Room 1 - Entrance
print("Having travlled many miles over treacherous terrain you come finally to the site of the fabled dungeon:\n")
sleep(3)
