import tic_tac_toe 
from tic_tac_toe import Interface
import unittest
"""
Tests for tic_tac_toe.py
"""

__author__ = "Meg Ford"
__copyright__ = "Copyright 2014 Meg Ford"
__credits__ = []
__license__ = "GNU GPL v2+"
__version__ = "1.0"
__maintainer__ = "Meg Ford"
__email__ = "meg387@gmail.com"

######################################################################

class Tests(unittest.TestCase):
    def test_move_string(self):
        interface = Interface()

        result = interface.move_type('L')
        self.assertFalse(result)
            
    def test_move_out_of_range(self):
        interface = Interface()
        
        result = interface.move_type(20)
        self.assertFalse(result)
        
    def test_move_duplicate(self):
        interface = Interface()
        tic_tac_toe.input_list[0] = 'x'
        
        result = interface.move_type(0)
        self.assertFalse(result)
        
    def test_move_win(self):
        interface = Interface()
        tic_tac_toe.input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tic_tac_toe.board = [8, 1, 6, 3, 5, 7, 4, 9, 2]
        tic_tac_toe.player1 = []
        tic_tac_toe.input_list[0] = 'x'
        tic_tac_toe.input_list[1] = 'x'
        tic_tac_toe.player1.append(tic_tac_toe.board[0])
        tic_tac_toe.player1.append(tic_tac_toe.board[1]) 
        tic_tac_toe.board[0] = 0
        tic_tac_toe.board[1] = 0      
        result = interface.add_score('x', 2)
        self.assertTrue(result)
  
    def test_move_not_win(self):
        interface = Interface()
        tic_tac_toe.input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tic_tac_toe.board = [8, 1, 6, 3, 5, 7, 4, 9, 2]
        tic_tac_toe.player1 = []
        tic_tac_toe.input_list[0] = 'x'
        tic_tac_toe.player1.append(tic_tac_toe.board[0])
        tic_tac_toe.board[0] = 0  
        result = interface.add_score('x', 2)
        self.assertFalse(result)
        
    def test_next_move_block(self):
        interface = Interface()
        tic_tac_toe.input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tic_tac_toe.board = [8, 1, 6, 3, 5, 7, 4, 9, 2]
        tic_tac_toe.player1 = []
        tic_tac_toe.input_list[0] = 'x'
        tic_tac_toe.input_list[1] = 'x'
        tic_tac_toe.player1.append(tic_tac_toe.board[0])
        tic_tac_toe.player1.append(tic_tac_toe.board[1]) 
        tic_tac_toe.board[0] = 0
        tic_tac_toe.board[1] = 0      
        result = interface.next_move()
        self.assertEquals(result, 0)
        
    def test_next_move_strategy(self):
        interface = Interface()
        tic_tac_toe.input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tic_tac_toe.board = [8, 1, 6, 3, 5, 7, 4, 9, 2]
        tic_tac_toe.player1 = []
        tic_tac_toe.player2 = []
        tic_tac_toe.input_list[0] = 'x'
        tic_tac_toe.input_list[1] = 'o'
        tic_tac_toe.player1.append(tic_tac_toe.board[0])
        tic_tac_toe.player2.append(tic_tac_toe.board[1]) 
        tic_tac_toe.board[0] = 0
        tic_tac_toe.board[1] = 0      
        result = interface.next_move()
        self.assertEquals(result, 0)
    
    def test_next_move_win(self):
        interface = Interface()
        tic_tac_toe.input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tic_tac_toe.board = [8, 1, 6, 3, 5, 7, 4, 9, 2]
        tic_tac_toe.player2 = []
        tic_tac_toe.input_list[0] = 'o'
        tic_tac_toe.input_list[1] = 'o'
        tic_tac_toe.player2.append(tic_tac_toe.board[0])
        tic_tac_toe.player2.append(tic_tac_toe.board[1]) 
        tic_tac_toe.board[0] = 0
        tic_tac_toe.board[1] = 0      
        result = interface.next_move()
        self.assertEquals(result, 1)
        
            
    def test_next_move_cats(self):
        interface = Interface()
        tic_tac_toe.input_list = ['x', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'o']
        tic_tac_toe.board = [-100, -100, -100, -100, -100, -100, -100, -100, -100]
        tic_tac_toe.player1 = [8, 5, 7, 4, 9]
        tic_tac_toe.player2 = [1, 6, 3, 2]     
        result = interface.next_move()
        self.assertEquals(result, 2)
            
if __name__ == "__main__":

    unittest.main()
