import unittest

from Dice.roll_parser import Parser


class ParserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.full_roll = "1d20+2"
        self.just_face = "d6"
        self.dice_and_faces = "2d8"
        self.face_and_operator = "d12-"
        self.dice_face_operator = "3d4*"
        self.invalid_string = "blorgen"

    def test_is_valid_roll_returns_true_given_a_full_roll_string(self) -> None:
        roll = Parser(self.full_roll)
        is_valid = roll.is_valid_roll()
        self.assertEquals(is_valid, True)

    def test_is_valid_returns_true_given_a_roll_with_just_face(self) -> None:
        roll = Parser(self.just_face)
        is_valid = roll.is_valid_roll()
        self.assertEquals(is_valid, True)

    def test_is_valid_returns_true_given_a_roll_with_dice_and_faces(self) -> None:
        roll = Parser(self.dice_and_faces)
        is_valid = roll.is_valid_roll()
        self.assertEquals(is_valid, True)

    def test_is_valid_returns_false_given_a_roll_with_face_and_operator(self) -> None:
        roll = Parser(self.face_and_operator)
        is_valid = roll.is_valid_roll()
        self.assertEquals(is_valid, False)

    def test_is_valid_returns_false_given_a_roll_with_dice_face_and_operator(self) -> None:
        roll = Parser(self.dice_face_operator)
        is_valid = roll.is_valid_roll()
        self.assertEquals(is_valid, False)

    def test_is_valid_returns_false_given_an_invalid_string(self) -> None:
        roll = Parser(self.invalid_string)
        is_valid = roll.is_valid_roll()
        self.assertEquals(is_valid, False)

    def test_Parser_assigns_constituents_correctly_given_full_roll(self) -> None:
        parsed_roll = Parser(self.full_roll)
        self.assertEquals(parsed_roll.dice, 1)
        self.assertEquals(parsed_roll.faces, 20)
        self.assertEquals(parsed_roll.operator, "+")
        self.assertEquals(parsed_roll.modifier, 2)

    def test_Parser_assigns_constituents_correctly_given_just_face(self) -> None:
        parsed_roll = Parser(self.just_face)
        self.assertIsNone(parsed_roll.dice)
        self.assertEquals(parsed_roll.faces, 6)
        self.assertIsNone(parsed_roll.operator)
        self.assertIsNone(parsed_roll.modifier)

    def test_Parser_assigns_constituents_correctly_given_dice_and_faces(self) -> None:
        parsed_roll = Parser(self.dice_and_faces)
        self.assertEquals(parsed_roll.dice, 2)
        self.assertEquals(parsed_roll.faces, 8)
        self.assertIsNone(parsed_roll.operator)
        self.assertIsNone(parsed_roll.modifier)

    def test_Parser_assigns_constituents_as_none_given_invalid_string(self) -> None:
        parsed_roll = Parser(self.invalid_string)
        self.assertIsNone(parsed_roll.dice)
        self.assertIsNone(parsed_roll.faces)
        self.assertIsNone(parsed_roll.operator)
        self.assertIsNone(parsed_roll.modifier)

if __name__ == "__main__":
    unittest.main()