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


class Board():

    """
    A :class:`Board` object which contains a magic square
    for finding a win and a values list.
    """

    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.magic_square = [8, 1, 6, 3, 5, 7, 4, 9, 2]

    def add_move(self, move, x_or_o):
        """Add a :class:`Board[move]` object to the list"""
        self.values[move] = x_or_o

    def remove_value(self, move):
        self.magic_square[move] = -1000

    def print_board(self):
        i = 0
        print '\n\n'
        for t in range(0, 3):
            for y in range(0, 3):
                print ' ' + str(self.values[i]),
                if y == 0 or y == 1:
                    print ' |',
                else:
                    print ''
                i += 1
            if t != 2:
                print '________________'
        print '\n\n'

    def assign_player_input(self):
        is_valid = 0
        count = 0
        while not is_valid or count == 5:
            player = raw_input("Player x moves first.\
                \nEnter x if you would like to move first,\
                \notherwise enter o:\n")
            ret = self.check_player_input(player)
            count += 1
            if ret is not None:
                is_valid = 1
        return ret

    def check_player_input(self, player):
        if player == "x" or player == 'o':
            return player
        else:
            print "Error: please enter x or o.\n"
            return None

    def move_input(self):
        is_valid = 0
        count = 0
        while not is_valid or count == 5:
            move = raw_input("Enter the number of space to move:\n")
            is_valid = self.move_type(move)
            count += 1

        return int(move) - 1

    def move_type(self, move):
        try:
            move = int(move) - 1
        except ValueError:
            print "Error\n"
            return False

        if move > 8 or move < 0:
            print "Error\n"
            return False
        elif type(self.values[move]) is str:
            print "Error\n"
            return False
        else:
            return True

    def print_winner(self, player):
        print player + " Wins"
