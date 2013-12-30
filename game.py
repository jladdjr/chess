#!/usr/bin/python

import sys

from board import Board
from board_analyzer import BoardAnalyzer

class Game(object):

    def __init__(self):
        """
        Initialize new game.
        """
        #Create new game board
        self._board = Board() 
        self._boardAnalyzer = BoardAnalyzer()

        #Record whose turn it is
        self._currentPlayer = 1      # 1 => White, 2 => Black

        #Print welcome text
        welcome = "Welcome to Solidarity Bros. Chess!\n" \
          "by Chris Wang, Dmitriy Chukhin, and Jim Ladd\n" \
          "\n" \
          "To move a piece, give the starting and ending coordinates.\n" \
          "To move the white knight for example, type 'b1c3'.\n\n" \
          "Enjoy!\n\n"
 
        print welcome

    def play(self):
        """
        Main game loop.
        """
        while True:
            self._nextTurn()

    def _nextTurn(self):
        """
        Contains logic for executing a player's turn.
        Exits when game is finished.
        """
        #Get next move from player
        move = self._getPlayersNextMove()

        #If move is legal, make next move

        #Print board

        #End game if king is in check-mate

        #Warn if king is in check

        #Switch to next player

    def _getPlayersNextMove(self):
        while True:
            prompt = "Player %s> " % str(self._currentPlayer)
            response = raw_input(prompt)

            #Validate response
            if len(response) == 4:
                if response.lower() == 'quit':
                    sys.exit(0)
                return response
            else:
                helpText = "\n Type the starting and ending coordinates.\n" \
                           " For example, 'b1c3'.\n\n" \
                           " Type quit to quit.\n"
                print helpText
