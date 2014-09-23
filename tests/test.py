import game
from game import Game
import unittest
"""
Tests for Tic-Tac-Toe game.
"""

__author__ = "Meg Ford"
__copyright__ = "Copyright 2014 Meg Ford"
__credits__ = []
__license__ = "GNU GPL v2+"
__version__ = "1.0"
__maintainer__ = "Meg Ford"
__email__ = ""

######################################################################

class Tests(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.game = Game()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        del self.game

    def test_move_string(self):
        result = self.game.board.move_type('L')
        self.assertFalse(result)
            
    def test_move_out_of_range(self):
        result = self.game.board.move_type(20)
        self.assertFalse(result)
        
    def test_move_in_range(self):
        result = self.game.board.move_type(2)
        self.assertTrue(result)
        
    def test_move_duplicate(self):
        self.game.move_playerX(5)
        result = self.game.move_playerX(5)
        self.assertFalse(result)
  
    def test_x_not_win(self):
        self.game.adjust_lists(self.game.playerX, 1)
        self.game.adjust_lists(self.game.playerX, 4)
        result = self.game.adjust_lists(self.game.playerX, 8)
        self.assertFalse(result)
        
    def test_o_not_win(self):
        self.game.adjust_lists(self.game.playerO, 1)
        self.game.adjust_lists(self.game.playerO, 4)
        self.game.adjust_lists(self.game.playerO, 8)
        result = self.game.playerO.check_game_over()
        self.assertFalse(result)
        
    def test_next_move_block(self):
        self.game.adjust_lists(self.game.playerX, 0)
        self.game.move_playerX(2)
        result = self.game.playerO.player[0]
        self.assertEquals(result, 1)
    
    def test_next_move_win(self):
        self.game.adjust_lists(self.game.playerO, 6)
        self.game.adjust_lists(self.game.playerO, 4)
        result, move = self.game.playerO.check_for_winning_move(self.game.board.magic_square)
        self.assertEquals(result, 1)
        self.assertEquals(move, 2)       
            
    def test_next_move_cats(self):
        self.game.adjust_lists(self.game.playerX, 0)
        self.game.adjust_lists(self.game.playerO, 1)
        self.game.adjust_lists(self.game.playerX, 2)
        self.game.adjust_lists(self.game.playerO, 3)
        self.game.adjust_lists(self.game.playerX, 4)
        self.game.adjust_lists(self.game.playerO, 6)
        self.game.adjust_lists(self.game.playerX, 7)
        self.game.adjust_lists(self.game.playerO, 8)
        result, move = self.game.playerX.check_for_winning_move(self.game.magic_square)
        self.assertEquals(result, 0)
        self.assertEquals(move, None)
            
if __name__ == "__main__":

    unittest.main()
