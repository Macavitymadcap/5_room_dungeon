from dataclasses import dataclass

from Characters.attack import Attack

@dataclass
class Monster:
  name: str
  hit_points: int
  armour_class: int
  armour_name: str
  attack: Attack