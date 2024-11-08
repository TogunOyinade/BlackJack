from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.

  def test_print_card_name_example(self):
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 3), "Drew a 3\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")


  def draw_card(self):
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([6], draw_card), 6)


  def test_print_header(self):
    self.assertEqual(get_print(print_header, "YOUR TURN"),"-----------\nYOUR TURN\n-----------\n")
    self.assertEqual(get_print(print_header, "DEALER TURN"),"-----------\nDEALER TURN\n-----------\n")
  
  
  def test_draw_starting_hand(self):
    output = mock_random([3,5], draw_starting_hand, "DEALER")
    self.assertEqual(output, 8)
    output = mock_random([11,1], draw_starting_hand, "DEALER")
    self.assertEqual(output, 21)
    output = mock_random([12,8], draw_starting_hand, "DEALER")
    self.assertEqual(output, 18)
    output = mock_random([1,9], draw_starting_hand, "YOUR")
    self.assertEqual(output, 20)
  
  
  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 23), "Final hand: 23.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 20), "Final hand: 20.\n")
    self.assertEqual(get_print(print_end_turn_status, 0), "Final hand: 0.\n")
    self.assertEqual(get_print(print_end_turn_status, 10), "Final hand: 10.\n")
    self.assertEqual(get_print(print_end_turn_status, 15), "Final hand: 15.\n")
    self.assertEqual(get_print(print_end_turn_status, 26), "Final hand: 26.\nBUST.\n")

  def test_print_end_game_status(self):
    expected_output = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 18, 17), expected_output)
    self.assertEqual(get_print(print_end_game_status, 20, 25), expected_output)
    self.assertEqual(get_print(print_end_game_status, 5, 29), expected_output)
    self.assertEqual(get_print(print_end_game_status, 5, 4), expected_output)


    expected_output = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 23, 21), expected_output)
    self.assertEqual(get_print(print_end_game_status, 25, 19), expected_output)
    self.assertEqual(get_print(print_end_game_status, 30, 32), expected_output)
    self.assertEqual(get_print(print_end_game_status, 27, 29), expected_output)
    self.assertEqual(get_print(print_end_game_status, 19, 20), expected_output)
    self.assertEqual(get_print(print_end_game_status, 10, 14), expected_output)

    
    expected_output = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 21, 21), expected_output)
    self.assertEqual(get_print(print_end_game_status, 20, 20), expected_output)
    self.assertEqual(get_print(print_end_game_status, 15, 15), expected_output)
    self.assertEqual(get_print(print_end_game_status, 8, 8), expected_output)




if __name__ == '__main__':
    unittest.main()
