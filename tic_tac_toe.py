#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tic-tac-toe game employing magic square win-checking algorithm
Include Unit tests
"""

__author__ = "Meg Ford"
__copyright__ = "Copyright 2014 Meg Ford"
__credits__ = []
__license__ = "GNU GPL v2+"
__version__ = "1.0"
__maintainer__ = "Meg Ford"
__email__ = ""

######################################################################

import sys

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [8, 1, 6, 3, 5, 7, 4, 9, 2]
player1 = []
player2 = []

class Interface:        
    def print_board(self):
        i = 0
        print '\n\n'
        for t in range(0, 3):
            for y in range(0, 3):
                print ' ' + str(input_list[i]),
                if y == 0 or y == 1:
                    print ' |',
                else:
                    print ''
                i += 1
            if t != 2:
                print '________________'      
        print '\n\n'

    def agent(self):
        self.print_board()
        move =  input("Enter the number of the space where you wish to move\n")
        return move - 1
        
    def check_move(self, move):
        if self.move_type(move):
            self.eval_move('x', move)
        else:
            print 'Error: please enter the number of the square'
            move = self.agent()
            self.check_move(move)       
    
    def move_type(self, move):
        if move > 8 or move < 0: 
            return False
        elif type(move) is not int:
            return False
        elif type(input_list[move]) is str:
            return False
        else:
            return True
   
    def eval_move(self, player, move):
        result = self.add_score(player, move)
        if result:
            self.print_board()
            print player + " Wins"
            sys.exit(0)
        else:   
            move = self.next_move() 
            if move == 2:
                self.print_board()
                print "Cat's Game"
                sys.exit(0)
            elif move == 0:
                move = self.agent()
                self.check_move(move)
            else:
                self.print_board()
                print "O Wins"
                sys.exit(0)                
                   
    def add_score(self, player, move):
        for i, val in enumerate(player1):
            for x in player1[i + 1:]:
                if val + x + board[move] == 15:
                    self.adjust_lists(player1, 'x', move)
                    return True
        self.adjust_lists(player1, 'x', move)
        return False             
            
    def next_move(self, player='o'):
        for i, x in enumerate(player2):
            for y in player2[i + 1:]:
                for l, f in enumerate(board):
                    if f + y + x == 15:
                        self.adjust_lists(player2, 'o', l)
                        return 1
                        
        for i, val in enumerate(player1):
            for x in player1[i + 1:]:
                for l, f in enumerate(board):
                    if f + val + x == 15:
                        self.adjust_lists(player2, 'o', l)
                        return 0
                        
        return self.strategy()
    
    def strategy(self):
        type_list = []
        if type(input_list[4]) is int:
           self.adjust_lists(player2, 'o', 4)
           return 0
        else:
            for idx, val in enumerate(input_list): 
                type_list += [self.check_list_elem_type(idx, val)]
            
            op = self.check_opposite_corner(idx, val)
            
            if  not op:
                odd = self.odd_squares(type_list)
                if not odd:
                    return odd
            else:
                even = self.even_squares(type_list)
                if not even:
                    return even
                
                odd = self.odd_squares(type_list)
                if not odd:
                    return odd                        
            return 2
   
    def even_squares(self, type_list):         
        for idx, val in enumerate(type_list):
            if type_list[idx][0]:
                self.adjust_lists(player2, 'o', type_list[idx][3])
                return 0
        return 1
        
    def odd_squares(self, type_list):
        for idx, val in enumerate(type_list):
            if val[1]:
                self.adjust_lists(player2, 'o', type_list[idx][3])
                return 0
        return 1
            
    def check_list_elem_type(self, idx, val):
        if type(val) is int and idx % 2 == 0:
            return [True, True, val, idx]
        elif type(val) is int and idx % 2 != 0:
            return [False, True, val, idx]
        else: 
            return [False, False, val, idx]
    
    def check_opposite_corner(self, idx, val):
        if player1[0] % 2 == 0:
            if player1[1] % 2 == 0:
                if player1[0] + player1[1] == 10:
                    return 0
        return 1 
   
    def adjust_lists(self, player, x_or_o, move):
        player.append(board[move])
        input_list[move] = x_or_o
        board[move] = -1000
        

                 
###############################################################################

if __name__ == '__main__':  
    i = Interface()  
    move = i.agent()
    i.check_move(move)
    
