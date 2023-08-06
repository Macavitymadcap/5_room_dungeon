from dataclasses import dataclass, field
from random import randint
from typing import List, Optional

from Dice.parser import Parser


@dataclass
class Roller:
    dice_string: str
    valid_roll: bool = field(init=False)
    dice: Optional[int] = field(init=False)
    faces: Optional[int] = field(init=False)
    operator: Optional[str] = field(init=False)
    modifier: Optional[int] = field(init=False)

    def __post_init__(self) -> None:
        parsed_roll = Parser(self.dice_string)
        self.valid_roll = parsed_roll.is_valid_roll()
        self.dice = parsed_roll.dice
        self.faces = parsed_roll.faces
        self.operator = parsed_roll.operator
        self.modifier = parsed_roll.modifier

    def roll_die(self) -> int:
        if not self.valid_roll:
            raise ValueError(f"'{self.dice_string}' is not a valid roll")
        result = randint(1, self.faces)
        return result

    def roll_dice(self) -> int:
        if not self.valid_roll:
            raise ValueError(f"'{self.dice_string}' is not a valid roll")
        results = [self.roll_die() for _ in range(self.dice)]
        result = sum(results)
        return result

    def roll_standard(self) -> int:
        if not self.valid_roll:
            raise ValueError(f"'{self.dice_string}' is not a valid roll")
        result = 0
        if self.dice is not None:
            result += self.roll_dice()
        else:
            result += self.roll_die()
        if self.operator is not None and self.modifier is not None:
            result = eval(f"{result}{self.operator}{self.modifier}")
        return result

    def roll_advantage(self) -> List[int]:
        results = [self.roll_standard() for _ in range(2)]
        results.sort(reverse=True)
        return results

    def roll_disadvantage(self) -> List[int]:
        results = [self.roll_standard() for _ in range(2)]
        results.sort()
        return results

    def roll_critical(self) -> int:
        result = self.roll_standard()
        if self.dice is not None:
            result += self.roll_dice()
        else:
            result += self.roll_die()
        return result

    @staticmethod
    def roll_ability_scores():
        results = []
        for _ in range(6):
            rolls = [randint(1, 6) for _ in range(4)]
            rolls.sort()
            rolls.pop(0)
            results.append(sum(rolls))
        results.sort(reverse=True)
        return results
