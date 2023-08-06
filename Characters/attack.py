from dataclasses import dataclass
from Dice import Roller
from typing import Dict, Union

@dataclass
class Attack:
    name: str
    to_hit: int
    damage_dice: str
    damage_type: str

    def __post_init__(self):
        self.to_hit_roller = Roller(f"d20+{self.to_hit}")
        self.damage_roller = Roller(self.damage_dice)

    def __str__(self) -> str:
        string = f"{self.name.capitalize()}, +{self.to_hit} to hit, {self.damage_dice} {self.damage_type} damage"
        
        return string
    
    def roll_to_hit(self, armour_class: int) -> Dict[str, Union[str, int]]:
        roll = self.to_hit_roller.roll_standard()
        if roll < armour_class:
            return { "result": "miss", "roll": roll }
        
        if roll - 20 == self.to_hit:
            return { "result": "crit", "roll": roll, "damage": self.damage_roller.roll_critical() }
        
        return { "result": "hit", "roll": roll, "damage": self.damage_roller.roll_standard() }