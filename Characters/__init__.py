from Characters.attack import Attack
from Characters.monster import Monster
from Characters.player import Player

character_class_names = ["fighter", "wizard", "rogue"]

fighter = Player(
    class_name="fighter", 
    hit_points=12, 
    armour_class=17, 
    armour_name="chainmail and shield",
    attack = Attack(name="longsword", to_hit=5, damage_dice="d8+3", damage_type="slashing"),
    inventory = ["longsword", "chainmail", "shield", "bundle of torches"]
)

rogue = Player(
    class_name="rogue", 
    hit_points=10, 
    armour_class=14, 
    armour_name="leather", 
    attack=Attack(name="double daggers", to_hit=5, damage_dice="2d4+3", damage_type="piercing"), 
    inventory=["two daggers", "leather armour", "bundle of torches"]
)

wizard = Player(
    class_name="wizard", 
    hit_points=8, 
    armour_class=14, 
    armour_name="mage armour", 
    attack = Attack(name="firebolt", to_hit=5, damage_dice="d10", damage_type="fire"), 
    inventory=["spellbook", "wand", "bundle of torches"]
)

# Monsters
animated_knife = Monster(
    name="animated knife", 
    hit_points=12, 
    armour_class=17, 
    armour_name="natural armour", 
    attack=Attack(name="dagger", to_hit=4,  damage_dice="d4+1", damage_type="piercing")
)

skeleton = Monster(
    name="skeleton", 
    hit_points=13, 
    armour_class=13, 
    armour_name="armour scraps", 
    attack=Attack(name="shortsword", to_hit=4, damage_dice="d6+2", damage_type="slashing")
)