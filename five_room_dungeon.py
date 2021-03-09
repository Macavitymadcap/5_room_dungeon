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
  def __init__(self, name, hp, ac, armour_name, attack_name, attack_bonus, attack_damage, attack_damage_bonus,):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.armour_name = armour_name
    self.attack_name = attack_name
    self.attack_bonus = attack_bonus
    self.attack_damage_bonus = attack_damage_bonus
    self.attack_damage = attack_damage

class PlayerCharacter(Character):
    def __init__(self, name, hp, ac, armour_name, attack_name, attack_bonus, attack_damage, attack_damage_bonus, max_hp, inventory=None):
        super().__init__(name, hp, ac, armour_name, attack_name, attack_bonus, attack_damage_bonus, attack_damage)
        self.max_hp = max_hp
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add_item(self, item):
        if item not in inventory:
            self.inventory.append(item)

    def remove_item(self, item):
        if item in inventory:
            self.inventory.remove(item)

    def character_sheet(self):
        return f"""
Name = {name}
Class = {self.name.capitalize()}
Hit Points = {self.hp}/{self.max_hp}
Armour Class = {self.ac} ({self.armour_name})
Attack = {self.attack_name.capitalize()}
Attack Bonus = +{self.attack_bonus}
Inventory = {self.inventory}"""

class Spinner:
    SYMBOLS = '|/-\\'

    def __init__(self):
        self.index = 0

    def __call__(self):
        stdout.write(Spinner.SYMBOLS[self.index] + '\b')
        self.index = (self.index + 1) % len(Spinner.SYMBOLS)

# Character Classes
fighter = PlayerCharacter("fighter", 12, 17, "chainmail and shield", "longsword", 5, roll_d(8), 3, 12, ["longsword", "chainmail", "shield", "bundle of torches"])
rogue = PlayerCharacter("rogue", 10, 14, "leather", "double daggers", 5, roll_mult_d(4, 2), 3, 10, ["two daggers", "leather armour", "bundle of torches"])
wizard = PlayerCharacter("wizard", 8, 14, "mage armour", "firebolt", 5, roll_d(10), 0, 8, ["spellbook", "wand", "bundle of torches"])

# Monsters
animated_knife = Character("animated knife", 12, 17, "natural armour", "dagger", 4,  roll_d(4), 1)
skeleton = Character("skeleton", 13, 13, "armour scraps", "shortsword", 4, roll_d(6), 2)

# Functions
def choose_option():
    sleep(1)
    print("\nChoose one of the options by typing it as you see it written.")
    sleep(1)
    
def what_do():
    print("\nWhat do you do?")
    sleep(1)

def show_sheet(player):
    print(player.character_sheet())

def enemy_attack(player, enemy):
    print("\nThe " + enemy.name + " attacks!")
    sleep(2)
    roll = roll_d(20)
    to_hit = roll + enemy.attack_bonus
    if roll == 20:
        damage = enemy.attack_damage + enemy.attack_damage + enemy.attack_damage_bonus
        player.hp -= damage
        print("\nThe " + enemy.name + " rolls a critical hit striking you with its " + enemy.attack_name + " dealing you " + str(damage) + "\ndamage.")
        sleep(2)
        if player.hp <= 0:
            print("\nYou have been slain by the " + enemy.name + ".")
            sleep(2)
            print("Game Over!")
            quit()
    elif to_hit >= player.ac:
        damage = enemy.attack_damage + enemy.attack_damage_bonus
        player.hp -= damage
        print("\nThe " + enemy.name + " rolls " + str(to_hit) + " hitting you with its " + enemy.attack_name + " dealing " + str(damage) + " damage.")
        sleep(2)
        if player.hp <= 0:
            print("\nYou have been slain by the " + enemy.name + ".")
            sleep(2)
            print("Game Over!")
            quit()
    else:
        print("\nThe " + enemy.name + " rolls " + str(to_hit) + " missing you.")
        sleep(2)

def player_attack(player, enemy):
    roll = roll_d(20)
    to_hit = roll + player.attack_bonus
    if roll == 20:
        damage = player.attack_damage + player.attack_damage + player.attack_damage_bonus
        enemy.hp -= damage
        print("\nYou roll a critical hit striking the " + enemy.name + " with your " + player.attack_name + " dealing " + str(damage) + "\ndamage.")
        if enemy.hp > 0:
            enemy_attack(player, enemy)
        else:
            print("\nYou have slain the " + enemy.name + ". Huzzah!")
            sleep(2)
    elif to_hit >= enemy.ac:
        damage = player.attack_damage + player.attack_damage_bonus
        enemy.hp -= damage
        print("\nYou roll " + str(to_hit) + " hitting the " + enemy.name + " with your " + player.attack_name + " dealing " + str(damage) + " damage.")
        sleep(2)
        if enemy.hp > 0:
            enemy_attack(player, enemy)
        else:
            print("\nYou have slain the " + enemy.name + ". Huzzah!")
            sleep(2)
    else:
        print("\nYou roll " + str(to_hit) + " missing the " + enemy.name + ".")
        sleep(2)
        enemy_attack(player, enemy)
    
def combat_heal(player, enemy):
    if "potion of healing" in player.inventory:
        heal_amount = roll_mult_d(4, 2) + 2
        player.hp += heal_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        player.inventory.remove("potion of healing")
        print("\nYou heal back up to " + str(player.hp) + " hit points.")
        sleep(2)
        enemy_attack(player, enemy)
    else:
        sleep(1)
        print("\nYou don't have any potions to heal you.")
        sleep(2)

def flee(player, enemy):
    flee_attempt = roll_d(100)
    if flee_attempt > 50:
        print("\nWith your tail between your legs you manage to escape the " + enemy.name + ".")
        sleep(2)
        print("Game Over!")
        sleep(2)
        quit()
    else:
        print("\nThere is no escape from the " + enemy.name + ", you must continue to fight.")
        sleep(2)
        enemy_attack(player, enemy)
            
def combat(player, enemy):
    flee_attempt = 0
    print("You and the " + enemy.name + " are locked in combat!")
    sleep(2)
    while player.hp > 0 and enemy.hp > 0 and flee_attempt <= 50:
        combat_options = ["attack", "flee", "heal"]
        show_sheet(player)
        sleep(2)
        what_do()
        choice = ""
        while choice not in combat_options:
            choice = input("attack/flee/heal\n> ").lower()
            sleep(2)
            if choice == "attack":
                player_attack(player, enemy)
            elif choice == "flee":
                flee(player, enemy)
            elif choice == "heal":
                combat_heal(player, enemy)
            else:
                choose_option()

def heal():
    if "potion of healing" in player.inventory:
        heal_amount = roll_mult_d(4, 2) + 2
        player.hp += heal_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        player.inventory.remove("potion of healing")
        print("\nYou heal back up to " + str(player.hp) + " hit points.")
    else:
        sleep(1)
        print("\nYou don't have any potions to heal you.")

# Variables
professions = ["fighter", "wizard", "rogue"]
yes_no = ["yes", "no"]
wall_opt = ["apologise", "deflect", "double down"]
spin = Spinner()

# Character Creation
name = input("Well met adventurer! What is your name?\n> ").capitalize()
sleep(1)
print(f"\nAhh, {name}: a warrior's name!\n")
sleep(2)
profession = ""
while profession not in professions:
    print("Or is it? Choose your class:")
    sleep(1)
    profession = input("fighter/rogue/wizard\n> ").lower()
    if profession == "fighter":
        sleep(1)
        print("\nStab things and ask questions later, I like your style.\n")
    elif profession == "wizard":
        sleep(1)
        print("\nWhen in doubt, set it aflame: a noble strategy.\n")
    elif profession == "rogue":
        sleep(1)
        print("\nSome say sneaking around lacks honour; I say it keeps you alive.\n")
    else:
        choose_option()
sleep(2)
print(name + " the " + profession + ", are you ready to face ...\n")
sleep(2)
print("THE FIVE ROOM DUNGEON!")
sleep(2)
response = ""
while response not in yes_no:
  print("\nWell, are you?")
  sleep(1)
  response = input("yes/no\n> ").lower()
  if response == "yes":
    sleep(1)
    print("\nA wise choice! Behold your character sheet:")
    sleep(2)
  elif response == "no":
    sleep(1)
    print("\nWell that was an anti-climax.\n")
    sleep(3)
    print("Game Over!")
    sleep(2)
    quit()
  else:
    choose_option()
player = None
if profession == "fighter":
    player = fighter
elif profession == "rogue":
    player = rogue
else:
    player = wizard
show_sheet(player)
sleep(7)
print("\nAnd now your adventure begins ...\n")
sleep(1)
for i in range(40):
    spin()
    sleep(0.1)
Spinner()
print("")

# Prologue
print("\nLegend tells of a dungeon not far from town beneath Mt. Bryntor said to\ncontain treasures of incalculable wealth ...\n")
sleep(6)
print("Incalculable not only because no one knows what the treasures are, but also\nbecause none have such wealth with which the treasures could be compared ...\n")
sleep(6)
print("Chief among the dungeon's claims to fame, however, is that no one has ever\nretrieved the treasures contained therein ...\n")
sleep(6)
print("For the dungeon is filled with perilous puzzles, tyrannous traps, mighty\nmonsters and other such alliterative dangers ...\n")
sleep(6)
if profession == "fighter":
    print("Being a mighty fighter, however, you believe you have the strength needed to\novercome the obstacles inside the dungeon ...\n")
elif profession == "wizard":
    print("Being a wise wizard, however, you know you have the necessary intelligence to\nbest the perils contained within ...\n")
else:
    print("Being a crafty rogue, however, you reckon you have the guile required to grab\nthe treasure and sneak out with your life ...\n")
sleep(6)
print("And so you head off out of town in search of wealth, glory, and (most\nimportantly) the entrance to the dungeon.\n")
sleep(6)
for i in range(40):
    spin()
    sleep(0.1)
Spinner()
print("")

# Room 1 - Puzzling Entrance
print("\nHaving travelled many miles over treacherous terrain you come finally to the\nsite of the fabled dungeon ...\n")
sleep(6)
print("Carved into the south side of Mt. Bryntor you see a smooth rectangle, 6 foot\nhigh and 2 foot wide ...\n")
sleep(6)
print("You might call it a door save for the fact it lacks a feature vital to all\nportals: a handle, or any other means of opening it ...")
sleep(6)
response = ""
ent_opt_1 = ["go back home", "investigate the area"]
while response not in ent_opt_1:
    what_do()
    response = input("go back home/investigate the area\n> ").lower()
    if response == "go back home":
        sleep(1)
        print("\nFor many a year will tale be told of how " + name + " the " + profession + "\ngave up on their epic quest at the first hurdle.\n")
        sleep(5)
        print("Game Over!")
        sleep(2)
        quit()
    elif response == "investigate the area":
        sleep(1)
        print("\nTaking a moment to survey the area a patch of stone of lighter grey than the\nrest of the mountain catches your eye just off to the left ...\n")
        sleep(5)
    else:
        choose_option()
print("Three raised buttons adorn the top of the light grey slab, each with a\ndifferent symbol carved into it; the first trees; the second waves and the\nlast clouds.\n")
sleep(7)
print("Beneath the drawings are carved these words: 'The world was formed of\nthree parts. Choose the order in which the parts came to be to reveal the\nentrance.'")
sleep(7)
entrance_puzzle = []
while entrance_puzzle != ["clouds", "waves", "trees"]:
    sleep(1)
    print("\nPush a button:")
    sleep(1)
    entrance_choice = input("clouds/trees/waves\n> ").lower()
    if entrance_choice == "clouds":
        entrance_puzzle.append("clouds")
        sleep(1)
        print("\nThe raised stone clicks into place ...")
    elif entrance_choice == "waves":
        entrance_puzzle.append("waves")
        sleep(1)
        print("\nThe raised stone clicks into place ...")
    elif entrance_choice == "trees":
        entrance_puzzle.append("trees")
        sleep(1)
        print("\nThe raised stone clicks into place ...")
    else:
        choose_option()
    if entrance_puzzle != ["clouds", "waves", "trees"] and len(entrance_puzzle) == 3:
        entrance_puzzle = []
        sleep(1)
        print("\nYou look over to the would be door, it remains shut, and turning back you see\nthe buttons pop back up  ...")
        sleep(3)
sleep(1)
print("\nYou hear the groaning of stone on stone and glancing to your right see the door\nsliding away, revealing a tunnel that leads down below ...")
sleep(6)
ent_opt_2 = ["descend into the dungeon", "go back home"]
response = ""
while response not in ent_opt_2:
    what_do()
    response = input("descend into the dungeon/go back home\n> ").lower()
    if response == "descend into the dungeon":
        sleep(1)
        print("\nLighting a torch you enter the tunnel and make your way below ...\n")
        sleep (3)
    elif response == "go back home":
        sleep(1)
        print("\nFor many a year will the tale be told of how " + name + " the " + profession + "\nwas scared by the opening of a door.\n")
        sleep(5)
        print("Game Over!")
        sleep(2)
        quit()
    else:
        choose_option()
for i in range(40):
    spin()
    sleep(0.1)
Spinner()
print("")

# Room 2 - Knife to Meet You
print("\nThe tunnel goes on for 40 feet before opening up to a small chamber. On the\nsouth wall is a door, in the middle of the room is a table.")
sleep(6)
def knife_door():
    response = ""
    knife_opt_1 = ["examine the door", "inspect the table"]
    while response not in knife_opt_1:
        what_do()
        response = input("examine the door/inspect the table\n> ").lower()
        if response == "examine the door":
            sleep(1)
            print("\nThe door is made of solid wood, halfway down the the right hand side is a\nbrass lock and handle.")
            sleep(4)
            knife_opt_2 = ["try handle", "inspect the table"]
            while response not in knife_opt_2:
                what_do()
                response = input("try the handle/inspect the table\n> ").lower()
                if response == "try the handle":
                    sleep(1)
                    print("\nYou turn the handle but the door remains locked, and you currently have no\nmeans of changing that.")
                    sleep(3)
                elif response == "inspect the table":
                    break 
                else:
                    choose_option()
        elif response == "inspect the table":
            break
        else:
            choose_option()
    sleep(1)
knife_door()
print("\nThe table is small and of wooden construction. Resting on top of it you see a\nkitchen knife, a brass key and a glass bottle filled with red liquid.")
sleep(6)
response = ""
knife_opt_3 = ["grab the knife", "pick up the key", "inspect the bottle"]
while response not in knife_opt_3:
    what_do()
    response = input("grab the knife/pick up the key/inspect the bottle\n> ").lower()
    if response in knife_opt_3:
        sleep(1)
        print("\nAs your hand reaches out towards the table the knife suddenly springs to life\nflying at your face ...\n")
        sleep(3)
        combat(player, animated_knife)
    else:
        choose_option()
sleep(1)
print("\nThe knife falls to ground no longer animate, leaving you free to inspect the\nitems on the table.")
sleep(3)
knife_door()
print("\nThe table is small and of wooden construction. On top of it is a brass key and a\nlittle bottle filled with a red liquid.\n")
sleep(5)
player.inventory.append("knife room key")
print("You pick the key and put it in your backpack.\n")
sleep(2)
print("Remaining on the table is the little bottle filled with red liquid.")
sleep(2)
response = ""
knife_opt_4 = ["inspect the bottle", "go to door"]
table = ["potion"]
while response not in knife_opt_4:
    what_do()
    response = input("inspect the bottle/go to door\n> ").lower()
    if response == "inspect the bottle":
        sleep(1)
        player.inventory.append("potion of healing")
        print("\nYou pick up the bottle and turning it over in your hand you see written on the\nbase of it the words 'Potion of Healing'.")
        sleep(6)
        response1 = ""
        potion_opt_1 = ["put in backpack", "drink now"]
        while response1 not in potion_opt_1:
            what_do()
            response1 = input("put in backpack/drink now\n")
            if response1 == "drink now":
                sleep(1)
                heal()
                sleep(2)
            elif response1 == "put in backpack":
                player.inventory.append("potion of healing")
                print("\nYou place the potion in your backpack. It may well come in handy later.")
                sleep(4)
            else:
                choose_option()
    elif response == "go to door":
        break
    else:
        choose_option()
print("\nYou walk over to the door and try the key in the lock. It fits, and you turn the\nhandle opening the door revealing a corridor that extends on for at least 40\nfeet.")
sleep(6)
response = ""
knife_opt_7 = ["walk into the corridor", "flee the dungeon in terror"]
while response not in knife_opt_7:
    what_do()
    response = input("walk into the corridor/flee the dungeon in terror\n").lower()
    if response == "walk into the corridor":
        sleep(1)
        print("\nLighting another torch you journey onwards, deeper into the dungeon...\n")
        sleep(2)
    elif response == "flee the dungeon in terror":
        sleep(1)
        print("\nYou came so far but fear got the best of you\n")
        sleep(2)
        print("Game Over!")
        sleep(2)
        quit()
    else:
        choose_option()
for i in range(40):
    spin()
    sleep(0.1)
Spinner()
print("")

# Room 3 - The Flirtatious Wall
print("\nYou walk on through the corridor until it eventually opens out into a circular\nchamber. Carved onto the east wall is a face.")
sleep(6)
response = ""
flirt_opt_1 = ["pack in and leave the dungeon", "examine the face"]
while response not in flirt_opt_1:
    what_do()
    response = input("pack in and leave/examine the face\n> ").lower()
    if response == "pack in and leave":
        sleep(1)
        print("\nIn the end you just couldn't ... face it.\n")
        sleep(2)
        print("Game Over!")
        sleep(2)
        quit()
    elif response == "examine the face":
        sleep(1)
        print("\nYou walk over to the east wall to get a closer look at the face.")
        sleep(4)
    else:
        choose_option()
print("\nThe face is intricately carved and well detailed; the eyebrows are furrowed;\nage and experience are suggested by multiple wrinkles and scars; a great big\nbushy beard covers the lower half.")
sleep(8)
print("\nIt's eyes are tightly shut and its mouth is open a fraction on the left as if\nit were asleep.")
sleep(5)
response = ""
flirt_opt_2 = ["shout at the face", "poke its eye", "caress its cheek"]
door_rage = 0
while response not in flirt_opt_2:
    what_do()
    response = input("shout at the face/poke its eye/caress its cheek\n> ").lower()
    if response == "shout at the face":
        door_rage += 2
        sleep(1)
        print("\nBreathing in to achieve maximum volume you you unleash a bellowing cry of:\n")
        sleep(4)
        print("'WAKEY WAKEY EGGS AND BAKEY GOOD MORNING MR. WALL-FACE!'\n")
        sleep(3)
        print("Your scream shakes the very foundations of the chamber. The eyes of the face\nopen blinkingly accompanied by the sound of grinding stone.\n")
        sleep(6)
        print("The face speaks in a gravelly voice, saying: 'Three things: first - rude!\nSecond - do I look like I need eggs or bacon to you? Third - real fucking rude!'")
        sleep(6)
        shout_response = ""
        while shout_response not in wall_opt:
            what_do()
            shout_response = input("apologise/deflect/double down\n> ").lower()
            if shout_response == "apologise":
                door_rage -= 1
                sleep(1)
                print("\nYou see the rage on the door's face and say: 'I'm so sorry, to be honest I\ndidn't think anything would happen'\n")
                sleep(4)
                print("The door looks you over and says: 'Yes, well something did, but you strike me\nas having not encountered many talking walls before, so apology accepted'")
            elif shout_response == "deflect":
                door_rage += 1
                sleep(1)
                print("\nYou look at the face and with a grin say: 'Well if not eggs an bacon, could I\ninterest you in some pebbles?'\n")
                sleep(4)
                print("The face narrows its eyes and says 'I don't care for pebbles, or your attempts\nat humour'\n")
            elif shout_response == "double down":
                door_rage += 2
                sleep(1)
                print("\nYou look at the face and say: 'You're a wall carving, I don't owe you jack'\n")
                sleep(4)
                print("The face looks you up and down and says: 'You're a bag of bones - right back\nat you pal'")
            else:
                choose_option()
    elif response == "poke its eye":
        door_rage += 1
        sleep(1)
        print("\nYou jab at the solid rock with your index finger and it is surpisingly squishy.\nThe mouth opens screaming 'Owww!',the eyes roll around before resting on you.\n")
        sleep(6)
        print("The face speaks in a gravelly voice, saying: 'What the hell did you do that\nfor?'")
        sleep(4)
        poke_response = ""
        while poke_response not in wall_opt:
            what_do()
            poke_response = input("apologise/deflect/double down\n> ").lower()
            if poke_response == "apologise":
                door_rage -= 1
                sleep(1)
                print("\nYou see the rage on the door's face and say: 'I'm so sorry, to be honest I\nthought you were just an inanimate carving'\n")
                sleep(4)
                print("The door looks you over and says: 'Well I am animate, as you can tell by me\nmoving and talking, but you didn't know any better so apology accepted'")
            elif poke_response == "deflect":
                door_rage += 1
                sleep(1)
                print("\nYou look at the face and with a grin say: 'Ahh you know, just poking around'\n")
                sleep(4)
                print("The face narrows its eyes and says 'Now is not the time for puns, especially of such low calibre'")
            elif poke_response == "double down":
                door_rage += 2
                sleep(1)
                print("\nYou look at the face and say: 'You're a wall - not like you should react to a\npoking anyway!'\n")
                sleep(4)
                print("The face looks you up and down and says: 'Well maybe you've learnt not to just\npoke evertything you encounter.'")
            else:
                choose_option()
    elif response == "caress its cheek":
        sleep(1)
        print("\nYou run your hand gently across the beared cheek of the carving. It moves benath\nyour fingers and you see the eyes flutter open, fixing on you.\n")
        sleep(4)
        print("The face speaks in a gravelly voice, saying: 'Why hello there handsome'\n")
        sleep(3)
        if profession == "wizard":
            print("It looks you over and says: 'Is that a wand in your robes or are you just\npleased to see me?'")
        elif profession == "rogue":
            print("It looks you over and says: 'Are those two daggers in your breeches or are you\njust pleased to see me?'")
        else:
            print("It looks you over and says: 'Is that a sword in your sheath or are you just\npleased to see me?'")
        sleep(3)
        caress_response = ""
        come_on_opt_1 = ["be literal", "play along"]
        while caress_response not in come_on_opt_1:
            what_do()
            caress_response = input("be literal/play along\n> ").lower()
            if caress_response == "be literal":
                door_rage += 1
                sleep(1)
                if profession == "wizard":
                    print("\nYou look from the face to your wand and say: 'Affirmative. I use it to cast\nspells of a rad nature'")
                elif profession == "rogue":
                    print("\nYou look from the face to your daggers and say: 'I prefer the term stiletto,\nbut same difference'")
                else:
                    print("\nYou look from the face to your sword and say: 'Yeah. I swing it and it chops\nstuff'")
                sleep(3)
                print("\nThe face looks at you blankly and says: 'Oh. Cool.'")
            elif caress_response == "play along":
                sleep(1)
                print("\nYou look the face right in the saying 'Can't it be both?' and then wink.")
                sleep(3)
                print("\nA hint of red splashes across the grey stone of the face's cheeks and it says\n'Oh my!'")
    else:
        choose_option()
sleep(4)
print("\nThe face says: 'Well you've woken me up. What can I do you for?'")
sleep(3)
response = ""
flirt_opt_3 = ["state your business", "ask about face"]
while response not in flirt_opt_3:
    what_do()
    response = input("state your business/ask about face\n> ").lower()
    if response == "state your business":
        sleep(1)
        print("\nYou say to the face: 'I am here to fight monsters, solve puzzles and claim\ntreasure'")
        sleep(3)
        if door_rage >= 2:
            print("\nThe face rolls its eyes and says: 'Great, another one'")
            sleep(3)
        def get_intentions(door_rage):
            print("\nThe face looks to you and asks: 'Should you escape the dungeon what do you plan\nto do with the spoils of your quest?'")
            sleep(5)
            intentions = ["help others", "go on a bender", "don't know"]
            intentions_response = ""
            while intentions_response not in intentions:
                what_do()
                intentions_response = input("help others/go on a bender/don't know\n> ").lower()
                if intentions_response == "help others":
                    door_rage -= 1
                    sleep(1)
                    print("\nYou tell the face: 'I plan to use the treasure to help out my village'")
                    sleep(3)
                    print("\nThe face sizes you up and says: 'A most noble endeavour'")
                elif intentions_response == "go on a bender":
                    door_rage += 1
                    sleep(1)
                    print("\nYou tell the face: 'Get some me some shiny rings, few barrels of mead and hit\nthe brothels!'")
                    sleep(4)
                    print("\nThe face sizes you up and says: 'I see'")
                elif intentions_response == "don't know":
                    sleep(1)
                    print("\nYou tell the face: 'Tell the truth, not thought that far ahead'")
                    sleep(3)
                    print("\nThe face sizes you up and says: 'I can believe that'")
                else:
                    choose_options()
            sleep(3)
            if door_rage >= 4:
                print("\nThe door tells you flatly: 'You are, without a doubt, one of the nastiest shits\nto have ever entered this dungeon'")
                sleep(4)
                print("\nThe ground starts to shake beneath and the face continues to speak: 'I cannot in\ngood faith allow you to progress any further'")
                sleep(4)
                print("\nStones start falling from the ceiling, you turn to the door but it has gone:\nreplaced with more wall.")
                sleep(4)
                print("\nThe face closes its eyes and says: 'I'm going back to sleep. I don't like\nwatchingthem get crushed'")
                sleep(4)
                print("\nHelpless you claw at the wall as a rock falls on to your head, crushing you to\ndeath.")
                sleep(3)
                print("\nGame Over!")
                sleep(2)
                quit()
            elif door_rage <=3 and door_rage >= 2:
                print("\nThe wall sighs and says: 'You're a bit of a knob, but I've seen worse'")
                sleep(3)
                print("\nYou hear the scraping of stone and turning around you see the west wall opens\nup revealing another corridor.")
                sleep(4)
                print("\nBehind you the wall says: 'The rest of the dungeon lies onward. Now off you\nfuck, I need my beauty sleep'")
            else:
                print("\nThe walls says: 'You seem a mostly honourable sort. I shall open up the next\nroom to you'")
                sleep(4)
                print("\nYou hear the scraping of stone and turning around you see the west wall opens\nup revealing another corridor.")
                sleep(4)
                print("\nBehind you the wall says 'I need to catch some shut-eye, you be careful now'")
        get_intentions(door_rage)
    elif response == "ask about face":
        door_rage -= 1
        sleep(1)
        print("\nYou say to the wall: 'I'm just exploring, but what about you - what's your\nstory?'")
        sleep(3)
        print("\nThe wall looks bashful and replies: 'Why, no one ever asks about me. Oh my!'")
        sleep(3)
        print("\n'I was constructed by the mage who built this dungeon to test the morality of\nthose who enter in'")
        sleep(4)
        if door_rage >= 2:
            print("\n'Speaking of which, I have a job to do'")
            sleep(3)
            get_intentions(door_rage)
        else:
            print("\n'His skeletal remains are in the room beyond. I can see you are a sweetheart so\nI'm going to skip the morality test and open it up for you'")
            sleep(4)
            print("\nYou hear the scraping of stone and turning around you see the west wall opens\nup revealing another corridor.")
            sleep(4)
            print("\nBehind you the wall says 'If you survive maybe come back and say hi?'")
    else:
        choose_option()
sleep(3)
flirt_opt_4 = ["sally forth", "go back home"]
response = ""
while response not in flirt_opt_4:
    what_do()
    response = input("sally forth/go back home\n> ")
    if response == "sally forth":
        sleep(1)
        print("\nHaving spoken to the wall you push on deeper into the dungeon...\n")
        sleep(2)
    elif response == "go back home":
        sleep(1)
        print("\nThoroughly weirded out after speaking to a wall, you decide to give up and go home.")
        sleep(3)
        print("\nGame Over!")
        sleep(2)
        quit()
for i in range(40):
    spin()
    sleep(0.1)
Spinner()
print("")

# Room 4 - The Skeletal Boss Fight
print("The passageway opens up revealing a large chamber in the centre of which is a\nstone sarcophagus.")
sleep(3)
print("\nOn the east wall is a door that reflects the light of your torch in a warm\ngold.")
sleep(4)
boss_door_opt_1 = ["examine the sarcophagus", "look at the door"]
response = ""
while response not in boss_door_opt_1:
    what_do()
    response = input("examine the sarcophagus/look at the door\n> ").lower()
    if response == "look at the door":
        sleep(1)
        print("\nYou walk over to the door and see it is made of solid gold. A lock and handle\nare half way down the right side of it.")
        sleep(4)
        boss_door_opt_2 = ["try handle", "inspect the sarcophagus"]
        boss_door_response = ""
        while boss_door_response not in boss_door_opt_2:
            what_do()
            boss_door_response = input("try the handle/inspect the sarcophagus\n> ").lower()
            if boss_door_response == "try the handle":
                sleep(1)
                print("\nThe door is locked, and you currently have no means of changing that.")
                sleep(3)
            elif boss_door_response == "inspect the sarcophagus":
                break
            else:
                choose_option()
    elif response == "examine the sarcophagus":
        break
    else:
        choose_option()
sleep(1)
print("\nYou move over to the centre of the room and see that the sarcophagus is covered\nin sigils and runes.")
sleep(4)
if profession == "wizard":
    print("\nFrom your years of study you know these symbols pertain to necromancy and chronomancy.")
    sleep(3)
sarc_opt = ["knock on the lid", "look at the door", "flee the dungeon"]
sarc_response =""
while sarc_response not in sarc_opt:
    what_do()
    sarc_response = input("knock on the lid/look at the door/flee the dungeon\n> ").lower()
    if sarc_response == "look at the door":
        sleep(1)
        print("\nYou walk over to the door and see it is made of solid gold. A lock and handle\nare half way down the right side of it.")
        sleep(4)
        print("\nYou try the handle but it is locked, and you currently have no means of\nchanging that.")
        sleep(3)
        sarc_response = ""
    elif sarc_response == "knock on the lid":
        sleep(1)
        print("\nYou knock on the lid of the coffin. A few moments pass and with nothing\nhappening. Then, stone screeches against stone as the lid starts to move to the\nside")
        sleep(5)
        print("\nOut of the sarcophagus steps a skeleton with a golden key hung around its\nneck and a sword in hand. It's jaw starts to move, and despite its lack of\nlungs sighs, then speaks to you in a wispy voice.")
        sleep(7)
        print("\nIt says: 'So you are the latest challenger, eh? I was once a just like you.\nIt took all my power to get to here.'")
        sleep(4)
        print("\n'Don't be thinking this will be easy, mind. This sword isn't just for show' it\nscreams as it lunges towards you.\n")
        sleep(4)
        combat(player, skeleton)
    elif sarc_response == "flee the dungeon":
        sleep(1)
        print("\nHaving made it to the boss fight you tactically decided to chicken out before\nyour arese could be handed to you.")
        sleep(4)
        print("\nGame Over!")
        sleep(2)
        quit()
    else:
        choose_option()
print("\nShrieking 'NOOOOOOOOOO!' the skeleton crumples to the ground finally dead\nrather than undead.")
sleep(4)
print("\nGrabbing the key from its neck you go over to the golden door, which now opens\nfor you, revealing a tunnel beyond.")
sleep(4)
boss_opt_2 = ["go forth", "back out"]
response = ""
while response not in boss_opt_2:
    what_do()
    response = input("go forth/back out\n> ").lower()
    if response == "go forth":
        sleep(1)
        print("\nLooking back at the skeletal remains heaped on the floor fully confidant you have\nbested the challenges of this dungeon you progress into the corridor.")
        sleep(4)
    elif response == "back out":
        sleep(1)
        print("\nHaving defeated the boss you decided to give up rather than claim your prize.")
        sleep(3)
        print("\nGame Over!")
        sleep(2)
        quit()
    else:
        choose_option()
for i in range(40):
    spin()
    sleep(0.1)
Spinner()
print("")

# Room 5 - Pyrrhic Reward
print("You come to to the end of the passage and dazzled by the reflections given off\nby your torchlight in the chamber you enter.")
sleep(5)
print("\nAll around you are heaps of gold, gems, artworks and other such treasures.\nFinally, you have made it to the prize you have sought for so long.")
sleep(5)
reward_opt = ["grab some treasure", "leave the dungeon"]
response = ""
while response not in reward_opt:
    what_do()
    response = input("grab some treasure/leave the dungeon\n> ").lower()
    if response == "grab some treasure":
        print("\nYou reach out your hand and start loading jewels and coins into your backpack.")
        sleep(3)
        print("\nYou keep looting until you notice a tingle in your hands. Looking down you see\nthat the flesh starts to peel away from them.")
        sleep(5)
        print("\nYou start to scream, but soon even your breath is taken from you and all becomes\ndarkness ...")
        sleep(5)
        print("")
        for i in range(40):
            spin()
            sleep(0.1)
        Spinner()
        print("")
        sleep(1)
        print("\nEventually you come back to consciousness to the sound of stone scraping against\nstone. A smidgen of light slowly eeks out above your head revealing an opening.")
        sleep(5)
        print("\nLifting your head up you see your are in a large chamber with a golden door to\nthe side and the face of plucky adventurer infornt of you.")
        sleep(5)
        print("\nWith a sigh you step out of the sarcophagus, and finally understand why no one\never comes back from the five room dungeon.")
    elif response == "leave the dungeon":
        sleep(1)
        print("\nLooking over the the treasures you realise that no matter how many you take,\nthey will never fill the void in your life. You turn back, and walk through the\ndungeon.")
        sleep(6)
        if door_rage <=1:
            print("\nYou come to the room of the talking wall, and talk for what seems an age.You\nfind you two have a lot in common.")
            sleep(5)
            print("\nYou decide to make something of it together, supporting one another in a dark,\ncruel world.")
            sleep(5)
            print("\nThe wall informs you that the treasure was cursed, and should you have claimed\nany of it, you have become the new skeleton in the sarcophagus.")
            sleep(5)
            print("\nThe years pass. occasionally you have to hide when some would-be adventurer\ncomes to claim the cursed treasure. Whenever you do you smile, knowing you have\nthe greatest treasure of them all ...")
            sleep(6) 
        else:
            print("\nYou return to the village, and while most of the inhabitants think you a fool\nfor leaving so much treasure behind in this economy, some find the tale of\nyour exploits amusing.")
            sleep(6)
            print(f"\nForevermore you are known as {name} the {profession}: the only person to ever\ncome back from the five room dungeon.")
            sleep(5)
    else:
        choose_option()
print("\nThe End")
sleep(3)
print("\nCoded by\nDaniel Kiernan.\n\nBeta tested by\nJack Ashley\nJay Greenwood\nJames Watson")
