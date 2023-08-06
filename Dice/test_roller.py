import unittest

from Dice.roller import Roller


class RollerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.d8 = "d8"
        self.one_to_eight = range(1, 9)
        self.two_d6 = "2d6"
        self.two_to_twelve = range(2, 13)
        self.standard_roll = "1d20+2"
        self.three_to_twenty_two = range(3, 23)
        self.invalid_roll = "blorgen"
        self.critical_roll = "3d4+2"
        self.eight_to_twenty_six = range(8, 27)
        self.three_to_eighteen = range(3, 19)

    def test_roll_die_returns_number_within_expected_range(self) -> None:
        roll = Roller(self.d8)
        result = roll.roll_die()
        self.assertIn(result, self.one_to_eight)

    def test_roll_dice_returns_number_within_expected_range(self) -> None:
        roll = Roller("2d6")
        result = roll.roll_dice()
        self.assertIn(result, self.two_to_twelve)

    def test_roll_standard_returns_number_within_expected_range(self) -> None:
        roll = Roller(self.standard_roll)
        result = roll.roll_standard()
        self.assertIn(result, self.three_to_twenty_two)

    def test_roll_standard_raises_error_given_invalid_dice_string(self) -> None:
        roll = Roller(self.invalid_roll)
        with self.assertRaises(ValueError):
            roll.roll_standard()

    def test_roll_advantage_returns_list_of_ints_in_expected_range_sorted_hightest_to_lowest(self) -> None:
        roll = Roller(self.standard_roll)
        results = roll.roll_advantage()
        self.assertGreaterEqual(results[0], results[1])
        for result in results:
            self.assertIn(result, self.three_to_twenty_two)

    def test_roll_disadvantage_returns_list_of_ints_in_expected_range_sorted_lowest_to_highest(self) -> None:
        roll = Roller(self.standard_roll)
        results = roll.roll_disadvantage()
        self.assertLessEqual(results[0], results[1])
        for result in results:
            self.assertIn(result, self.three_to_twenty_two)

    def test_roll_criticial_returns_int_within_expected_range(self) -> None:
        roll = Roller(self.critical_roll)
        result = roll.roll_critical()
        self.assertIn(result, self.eight_to_twenty_six)

    def test_roll_ability_scores_returns_list_of_ints_in_expected_ranges_sorted_highest_to_lowest(self) -> None:
        results = Roller.roll_ability_scores()
        self.assertGreaterEqual(results[0], results[5])
        for result in results:
            self.assertIn(result, self.three_to_eighteen)
