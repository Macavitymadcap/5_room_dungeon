# Imports
from time import sleep
from random import randint
from sys import stdout

# Dice
def roll_d(x):
    return randint(1, x)

def roll_mult_d(dice, times):
    return sum([randint(1, dice) for i in range(times)])

# Classes
class Character:
  def __init__(self, name, hit_points, armour_class, attack_name, attack_bonus, attack_damage):
    self.name = name
    self.hit_points = hit_points
    self.armour_class = armour_class
    self.attack_name = attack_name
    self.attack_bonus = attack_bonus
    self.attack_damage = attack_damage

class Spinner:
    SYMBOLS = '|/-\\'

    def __init__(self):
        self.index = 0

    def __call__(self):
        stdout.write(Spinner.SYMBOLS[self.index] + '\b')
        self.index = (self.index + 1) % len(Spinner.SYMBOLS)

# Combat Function
def combat(player, enemy):
    flee_attempt = 0
    print("You and the " + enemy.name + " are locked in combat!\n")
    sleep(2)
    while player.hit_points > 0 and enemy.hit_points > 0 and flee_attempt <= 50:
        combat_options = ["attack", "flee"]
        print("You currently have " + str(player.hit_points) + " hit points.\n")
        sleep(2)
        print("What do you do?")
        sleep(1)
        choice = ""
        while choice not in combat_options:
            choice = input("attack/flee\n")
            sleep(2)
            if choice == "attack":
                roll = roll_d(20) + player.attack_bonus
                if roll >= enemy.armour_class:
                    damage = player.attack_damage
                    enemy.hit_points -= damage
                    print("\nYou roll " + str(roll) + " hitting the " + enemy.name + " with your " + player.attack_name + " dealing " + str(damage) + " damage.\n")
                    sleep(2)
                    if enemy.hit_points > 0:
                        print("\nThe " + enemy.name + " attacks!\n")
                        sleep(2)
                        enemy_roll = roll_d(20) + enemy.attack_bonus
                        if enemy_roll >= player.armour_class:
                            enemy_damage = enemy.attack_damage
                            player.hit_points -= enemy_damage
                            print("\nThe " + enemy.name + " rolls " + str(enemy_roll) + " hitting you with its " + enemy.attack_name + " for " + str(enemy_damage) + " damage.\n")
                            sleep(2)
                        else:
                            print("\nThe " + enemy.name + " rolls " + str(enemy_roll) + " missing you.\n")
                            sleep(2)
                    else:
                        print("\nYou have slain the " + enemy.name + ". Huzzah!\n")
                        sleep(2)
                else:
                    print("\nYou roll " + str(roll) + " missing the " + enemy.name + ".")
                    sleep(2)
                    print("\nThe " + enemy.name + " attacks!\n")
                    enemy_roll = roll_d(20) + enemy.attack_bonus
                    if enemy_roll >= player.armour_class:
                        enemy_damage = enemy.attack_damage
                        player.hit_points -= enemy_damage
                        print("\nThe " + enemy.name + " rolls " + str(enemy_roll) + " hitting you with its " + enemy.attack_name + " for " + str(enemy_damage) + " damage.\n")
                        sleep(2)
                        if player.hit_points <= 0:
                            print("\nYou have been slain by the" + enemy.name + "\n")
                            sleep(2)
                            print("Game Over!")
                            quit()
                    else:
                        print("\nThe " + enemy.name + " rolls " + str(enemy_roll) + " missing you.\n")
                        sleep(2)
            elif choice == "flee":
                flee_attempt = roll_d(100)
                if flee_attempt > 50:
                    print("\nWith your tail between your legs you manage to escape the " + enemy.name + ".\n")
                    sleep(2)
                else:
                    print("\nThere is no escape from the " + enemy.name + ", you must continue to fight.\n")
                    sleep(2)
                    print("\nThe " + enemy.name + " attacks!\n")
                    enemy_roll = roll_d(20) + enemy.attack_bonus
                    if enemy_roll >= player.armour_class:
                        enemy_damage = enemy.attack_damage
                        player.hit_points -= enemy_damage
                        print("\nThe " + enemy.name + " rolls " + str(enemy_roll) + " hitting you with its " + enemy.attack_name + " for " + str(enemy_damage) + " damage.\n")
                        sleep(2)
                        if player.hit_points <= 0:
                            print("\nYou have been slain by the " + enemy.name + "\n")
                            sleep(2)
                            print("Game Over!")
                            quit()
                    else:
                        print("\nThe " + enemy.name + " rolls " + str(enemy_roll) + " missing you.\n")
                        sleep(2)
            else:
                print("\nYou can try to attack or try to flee. There are no other choices.\n")
                sleep(2)

# Instances
fighter = Character("fighter", 12, 17, "longsword", 5, roll_d(8) + 3)
rogue = Character("rogue", 10, 14, "double daggers", 5, roll_mult_d(4, 2) + 3)
wizard = Character("wizard", 8, 14, "firebolt", 5, roll_d(10))
goblin = Character("goblin", 7, 15, "scimitar", 4, roll_d(6) + 2)
orc = Character("orc", 15, 13, "greataxe", 5, roll_d(12) + 3)

# Variables
professions = ["fighter", "wizard", "rogue"]
yes_no = ["yes", "no"]
spin = Spinner()
player = None

# Character Creation
name = input("Well met adventurer! What is your name?\n")
sleep(1)
print("\nAhh, " + name + ": a warrior's name!\n")
sleep(2)
print("Or is it? Choose your class:")
sleep(1)
profession = ""
while profession not in professions:
  profession = input("fighter/rogue/wizard\n")
  if profession == "fighter":
    player = fighter
    sleep(1)
    print("\nStab things and ask questions later, I like your style.\n")
  elif profession == "wizard":
    player = wizard
    sleep(1)
    print("\nWhen in doubt, set it aflame: a noble strategy.\n")
  elif profession == "rogue":
    sleep(1)
    print("\nSome say sneaking around lacks honour; I say it keeps you alive.\n")
  else:
    player = rogue
    sleep(1)
    print("\nThese are basic-bitch rules: choose one of the classes stated below by typing it as you see it written.\n")
sleep(2)
print(name + " the " + profession + ", are you ready to face ...\n")
sleep(2)
print("THE FIVE ROOM DUNGEON!\n")
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
    print("Game Over!")
    quit()
  else:
    sleep(1)
    print("\nIt's a yes/no question pal.\n")
 
for i in range(30):
    spin()
    sleep(0.1)
Spinner()
print("\n")

# Prologue
print("\nLegend tells of a dungeon not far from town said to contain treasures of incalculable wealth ...\n")
sleep(4)
print("Incalculable not only because no one knows what the treasures are, but also because none have such wealth with which the treasures could be compared ...\n")
sleep(6)
print("Chief among the dungeon's claims to fame, however, is that no one has ever retrieved the treasures contained therein ...\n")
sleep(5)
print("For the dungeon is filled with perilous puzzles, tyrannous traps, mighty monsters and other such alliterative dangers ...\n")
sleep(5)
if profession == "fighter":
  print("Being a mighty fighter, however, believe you have the strength needed to overcome the obstacles inside the dungeon ...\n")
elif profession == "wizard":
  print("Being a wise mage, however, you know you have the necessary intelligence to best the perils contained within ...\n")
else:
  print("Being a crafty rogue, however, you reckon you have the guile required to grab the treasure and sneak out with your life ...\n")
sleep(5)
print("And so you head off out of town in search of wealth, glory, and (most importantly) the entrance to the dungeon.\n")

for i in range(30):
    spin()
    sleep(0.1)
Spinner()
print("\n")

# Room 1 - Entrance
print("Having travelled many miles over treacherous terrain you come finally to the site of the fabled dungeon ...\n")
sleep(3)
print("Carved into the south side of Mt. Bryntor you see a smooth rectangle, 6 foot high and 2 foot wide ...\n")
sleep(3)
print("You might call it a door save for the fact it lacks a feature vital to all portals: a handle, or any other means of opening it ...\n")
sleep(4)
print("What do you do?")
sleep(1)
response = ""
ent_opt_1 = ["go back home", "investigate the area"]
while response not in ent_opt_1:
    response = input("go back home/investigate the area\n")
    if response == "go back home":
        sleep(1)
        print("\nFor many a year will tale be told of how " + name + " the " + profession + " gave up on their epic quest at the first hurdle.\n")
        sleep(3)
        print("Game Over!")
        quit()
    elif response == "investigate the area":
        sleep(1)
        print("\nTaking a moment to survey the area a patch of stone of lighter grey than the rest of the mountain ctaches your eye just off to the left\n")
    else:
        sleep(1)
        print("\nThere's only two options. Pick one by typing it exactly as you see it.\n")
        sleep(2)

