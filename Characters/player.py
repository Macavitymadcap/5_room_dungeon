from dataclasses import dataclass, field
from typing import List

from copy import copy

from Characters.attack import Attack
from Dice import Roller

@dataclass
class Player:
    class_name: str
    hit_points:int
    armour_class: int
    armour_name: str
    attack: Attack
    inventory: List[str] = field(default_factory=list)
    player_name: str = field(default="Darren")

    def __post_init__(self):
        self.max_hit_points = copy(self.hit_points)


    def __str__(self):
        string = f"""
Name: {self.player_name}
Class: {self.class_name.capitalize()}
Hit Points: {self.hit_points}/{self.max_hit_points}
Armour Class: {self.armour_class} ({self.armour_name})
Attack: {self.attack.__str__()}
Inventory: {', '.join(self.inventory)}
"""        
        return string
    
    def heal(self):
        roll = Roller("2d4+2").roll_standard()
        self.hp = min(self.max_hp, self.hp + roll)