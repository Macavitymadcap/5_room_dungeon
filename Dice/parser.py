import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Parser:
    roll_string: str
    dice_regex = r"(?P<dice>\d*)?[d|D](?P<faces>\d+)?(?P<operator>[-|+|*|/])?(?P<modifier>\d*)?"
    dice: Optional[int] = None
    faces: Optional[int] = None
    operator: Optional[str] = None
    modifier: Optional[int] = None

    def __post_init__(self) -> None:
        if self.is_valid_roll():
            match = re.match(self.dice_regex, self.roll_string)
            self.dice = int(match.group('dice')) if match.group(
                'dice') else None
            self.faces = int(match.group('faces')) if match.group(
                'faces') else None
            self.operator = match.group(
                'operator') if match.group('operator') else None
            self.modifier = int(match.group('modifier')
                                ) if match.group('modifier') else None

    def is_valid_roll(self) -> bool:
        match = re.match(self.dice_regex, self.roll_string)
        if not match:
            return False
        if match.group('operator') and not match.group('modifier'):
            return False
        return True
