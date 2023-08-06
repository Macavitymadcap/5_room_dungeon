from typing import List
from Characters import fighter, rogue, wizard

def get_option_from_list(options: List[str]) -> str:
    for index, option in enumerate(options):
        print(f"{[index]} {option}")
    option_index = int(input("[choice_index] >"))
   
    return options[option_index]

player_name = input("Well met adventurer! What is your name?\n> ").capitalize()

print(f"Ahh, {player_name}: a warrior's name!")
print("Or is it? Chhose your class from:")
character_classes = ["fighter", "wizard", "rogue"]
character_class = get_option_from_list(character_classes) 
if character_class == character_classes[0]:
    print("Stab things and ask questions later, I like your style.")

elif character_class == character_classes[1]:
    print("When in doubt, set it aflame: a noble strategy.")

else:
    print("Some say sneaking around lacks honour; I say it keeps you alive.")

print(f"{player_name} the {character_class}, are you ready to face ...")
print("THE FIVE ROOM DUNGEON!")

response = ""
while response not in ["y", "n", "yes", "no"]:
  print("Well, are you?")
  response = input("yes/no> ").lower()
  if response in ["no", "n"]:
    print("Well that was an anti-climax.")
    print("Game Over!")
    quit()
  if response in ["yes", "y"]:
    print("A wise choice! Behold your character sheet:")
  

player = None
if character_class == "fighter":
    player = fighter
elif character_class == "rogue":
    player = rogue
else:
    player = wizard

player.player_name = player_name
print(player.__str__())

print("And now your adventure begins ...")