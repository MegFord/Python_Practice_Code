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


class Player(object):
    """
    A :class:`Board` object which contains a magic square
    for finding a win and a values list.
    """
    def __init__(self, name, move_type):
        """
        Initialize a :class:`Board` object.
        """
        self.player = list()
        self.name = name
        self.move_type = move_type

    def add_move(self, move):
        """
        Add a move to the :class:`Player` object's values.
        """
        self.player.append(move)

    def check_game_over(self):
        """
        Check to see if adding any three elements
        from the player's moves gives you 15.
        """
        limits = 0, len(self.player) - 1
        for index in enumerate(sorted(self.player)):
            lower, upper = limits
            while lower < index < upper:
                value =\
                    sum(self.player[lower],
                        self.player[index],
                        self.player[upper])
                print value
                if value == 15:
                    return 1
                elif value < 15:
                    lower += 1
                else:
                    upper -= 1
        return 0

    def check_for_winning_move(self, MagicSquare):
        """
        Check to see if adding any two elements
        from the player's moves and any one move
        still left on the board gives you 15.
        """
        for i, val in enumerate(self.player):
            for val2 in self.player[i + 1:]:
                for l, val3 in enumerate(MagicSquare):
                    if val + val2 + val3 == 15:
                        return 1, l
        return 0, None
