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

from board import Board
from players import Player


class Game(object):

    """
    A :class:`Game` object which instantiates
    the other objects and contains the business logic.
    """

    def __init__(self):
        """
        Initialize a :class:`Game` object.
        """
        self.board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9],
                           [8, 1, 6, 3, 5, 7, 4, 9, 2])
        self.magic_square = self.board.magic_square
        self.playerX = Player("Player X", "x")
        self.playerO = Player("Player O", "o")
        self._play = 0
        self._win = 1
        self._tie = 2

    def start(self):
        """
        Assign players based on user input.
        """
        player = self.board.assign_player_input()
        if player == 'x':
            player = self.playerX
            self.play(player)
        elif player == 'o':
            player = self.playerX
            self.adjust_lists(player, 4)
            self.board.print_board()
            player = self.playerO
            self.play(player)

    def play(self, player):
        """
        Start playing the game.
        """
        do = True
        while do is True:
            space = self.board.move_input()
            if type(space) == int:
                move = self.eval_move(player, space)
                self.board.print_board()
            do = True

    def eval_move(self, player, move):
        """
        Figure out which player moves first.
        """
        if player.name == "Player X":
            return self.move_playerX(move)
        else:
            return self.move_playerO(move)

    def move_playerX(self, move):
        """
        Move the person-controlled player.
        """
        self.adjust_lists(self.playerX, move)
        result = self.playerX.check_game_over()
        if result == self._play:
            return self.move_ai(self.playerO)
        else:
            self.print_result(self.playerX.name)

    def move_playerO(self, move):
        """
        Move the person-controlled player.
        """
        self.adjust_lists(self.playerO, move)
        result = self.playerO.check_game_over()
        if result == self._play:
            return self.move_ai(self.playerX)
        else:
            self.print_result(self.playerO.name)

    def move_ai(self, player):
        """
        Move the ai-controlled player.
        """
        opp_player = self.opp_player(player)
        # First check to see if the ai player has a winning move
        result, move = player.check_for_winning_move(self.magic_square)
        # If the ai player has a winning move, make it and print results
        if result == self._win and type(move) is int:
            self.adjust_lists(player, move)
            self.print_result(player.name)
        # If there are no winning moves for the ai player,
        # then check to see if there are any wins for the opponent.
        elif result == self._play and move is None:
            result, move =\
                opp_player.check_for_winning_move(self.magic_square)
            # If there are, then block the opponent's winning move
            if result == self._win and type(move) is int:
                self.adjust_lists(player, move)
                # If that was the last move on the board, end game
                if len(opp_player.player) + len(player.player) == 9:
                    self.print_result("Cat")
                # Else keep playing
                return self._play
            # Otherwise, hand the player off to the non-winning logic
            elif result == self._play and move is None:
                result = self.strategy(player)
                # If the ai player found  a move and made it...
                if result == self._play:
                    # Check to see if there are any more moves on the board...
                    if len(opp_player.player) + len(player.player) == 9:
                        self.print_result("Cat")
                    # If there are, keep playing
                    return self._play

                else:
                    self.print_result("Cat")
            else:
                print "Error\n"
                self.end_game()
        else:
            print "Error\n"
            self.end_game()

    def strategy(self, player):
        """
        Blocking strategies for the ai player.
        """
        # If the center square is empty, move there.
        if type(self.board.values[4]) is int:
            self.adjust_lists(player, 4)
            return self._play

        # Certain strategies are only relevent
        # if the opposing player
        # has made exactly two moves.
        if len(self.opp_player(player).player) == 2:
            # First check the diagonals.
            if not self.diagonal(player):
                return self._play

            # Next check for opposing player moves in opposite corners.
            if not self.check_opposite_corner(self.opp_player(player).player):
                return self._play

            # Next check for opposing player moves in checkerboard pattern
            # on the edge squares.
            if not self.check_edge(self.opp_player(player)):
                return self._play

        # Move to the first available even square.
        if not self.even_squares(player):
            return self._play
        # Move to the first available off square.
        if not self.odd_squares(player):
            return self._play

        # If we haven't found a move, then the cat won the game.
        return 2

    def even_squares(self, player):
        """
        Find the first free even-indexed square and
        add it to the ai player's list.
        """
        for idx, val in enumerate(self.board.values[::2]):
            if type(val) is int:
                self.adjust_lists(player, idx*2)
                return self._play
        return 1

    def odd_squares(self, player):
        """
        Find the first free odd-indexed square and
        add it to the ai player's list.
        """
        for idx, val in enumerate(self.board.values[1::2]):
            if type(val) is int:
                self.adjust_lists(player, idx*2+1)
                return self._play
        return 1

    def check_opposite_corner(self, player):
        """
        Next check for opposing player moves in opposite corners.
        """
        if player[0] % 2 == 0 and player[1] % 2 == 0:
            if player[0] + player[1] == 10:
                # If opposite corners are filled, then the ai player moves
                # to an odd-indexed square.
                return self.odd_squares(player)
        return 1

    def check_edge(self, player):
        """
        Check for a checkboard pattern.
        If that pattern is found, then the ai player moves
        to a corner square.
        """
        if player.player[0] % 2 != 0 and player.player[1] % 2 != 0:
            if abs(player.player[0] - player.player[1]) == 2 or\
                    abs(player.player[0] - player.player[1]) == 6:
                # If that pattern is found, then the ai player moves
                # to corner square.
                return self.corner_squares(player)
        return 1

    def diagonal(self, player):
        """
        Check for an occupied diagonal.
        """
        opp_player = self.opp_player(player).player
        if player.player[0] == 5:
            if player.player[0] + opp_player[0] + opp_player[1] == 15:
                # If a diagonal is filled, then the ai player moves
                # to an even-indexed square.
                return self.odd_squares(player)
        return 1

    def corner_squares(self, player):
        """
        Check for a checkboard pattern.
        If that pattern is found, then the ai player looks for
        the correct corner and moves there.
        """
        opp_player = self.opp_player(player)
        player = player.player
        if player[0] + player[1] == 4 and type(self.board.values[0]) is int:
            self.adjust_lists(opp_player, 0)
            return self._play
        elif player[0] + player[1] == 8 and type(self.board.values[2]) is int:
            self.adjust_lists(opp_player, 2)
            return self._play
        elif player[0] + player[1] == 12 and type(self.board.values[6]) is int:
            self.adjust_lists(opp_player, 6)
            return self._play
        elif player[0] + player[1] == 16 and type(self.board.values[8]) is int:
            self.adjust_lists(opp_player, 8)
            return self._play
        else:
            return 1

    def adjust_lists(self, player, move):
        """
        Add the values related to the square to the lists.
        """
        player.add_move(self.magic_square[move])
        self.board.add_move(move, player.move_type)
        self.board.remove_value(move)

    def print_result(self, name):
        """
        Print the board, winner, and exit the program.
        """
        self.board.print_board()
        self.board.print_winner(name)
        self.end_game()

    def end_game(self):
        """
        Exit the program.
        """
        sys.exit(0)

    def opp_player(self, player):
        """
        Return the other player based on the current player's name.
        """
        if player.name == "Player X":
            return self.playerO
        else:
            return self.playerX


if __name__ == '__main__':
    game = Game()
    game.board.print_board()
    game.start()
