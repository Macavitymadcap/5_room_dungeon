from io_functions import console, get_option_from_list, get_yes_no_bool, line_generator
from Characters import character_class_names, fighter, rogue, wizard, Player
from pathlib import Path
from rich.markdown import Markdown 

def get_player_character() -> Player:
    creation_text = line_generator(Path().cwd().joinpath("texts", "character_creation.txt"))
    game_over_text = line_generator(Path().cwd().joinpath("texts", "game_over.txt"))

    console.print(creation_text.__next__())
    player_name = input("> ")
    console.print(Markdown(creation_text.__next__().format(player_name)))
    console.print(creation_text.__next__())
    character_class = get_option_from_list(character_class_names) 
    
    if character_class == character_class_names[0]:
        console.print(creation_text.__next__())
        for _ in range(2):
            creation_text.__next__()
    elif character_class == character_class_names[1]:
        creation_text.__next__()
        console.print(creation_text.__next__())
        creation_text.__next__()
    else:
        for _ in range(2):
            creation_text.__next__()
        console.print(creation_text.__next__())
    console.print((creation_text.__next__().format(player_name, character_class)))

    for _ in range(3):
        console.print(creation_text.__next__())
    response = get_yes_no_bool()

    if not response:
        for _ in range(2):
            console.print((game_over_text.__next__()))
        quit()
    else:
        player = None
        if character_class == character_class_names[0]:
            player = fighter
        elif character_class == character_class_names[1]:
            player = rogue
        else:
            player = wizard
        player.player_name = player_name
        console.print(player.__str__())
        console.print(creation_text.__next__())
    return player