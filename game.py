#!/usr/bin/python

import os
import sys

import constants
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
        self._currentPlayer = constants.WHITE_PLAYER 

        #Print welcome text
        os.system('clear')
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

        #Print initial board
        self._board.printBoard()

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
        while self._board.isLegalMove(move,self._currentPlayer) != True:
            move = self._getPlayersNextMove()

        #Print board
        os.system('clear')
        self._board.printBoard()
    
        #Creates variable other_player
        if self._currentPlayer == constants.WHITE_PLAYER:
            self._otherPlayer = constants.BLACK_PLAYER
        else:
            self._otherPlayer = constants.WHITE_PLAYER

        #End game if king is in check-mate
        if self._boardAnalyzer.isCheckMate(self._board, self._otherPlayer)==True:
            #Game end conditions
            print "Congradulations! Player", self._currentPlayer, "has won!"
            choice = ""
            while choice != 'quit':
                choice = raw_input("Type 'quit' to quit. ")

        #Warn if king is in check
        if self._boardAnalyzer.isCheck(self._board, self._otherPlayer)==True:
            print "Player", self._otherPlayer,"is in check!"
        

        if self._currentPlayer == constants.WHITE_PLAYER:
            self._currentPlayer = constants.BLACK_PLAYER
        else: 
            self._currentPlayer = constants.WHITE_PLAYER
    def _getPlayersNextMove(self):
        """
        Retrieves player's next move. (e.g. "b1d4").
        Ensures that move is well-formed.

        @return: Player's next move (e.g. "b1d4")
        """
        while True:
            playerColor = ""
            if self._currentPlayer == constants.WHITE_PLAYER:
                playerColor = "White"
            else:
                playerColor = "Black"
            prompt = "%s> " % playerColor
            response = raw_input(prompt)

            #Check response length
            if len(response) != 4:
                self._printHelp()
                continue

            #Does user want to quit?
            if response.lower() == 'quit':
                sys.exit(0)

            #Check row/column values 
            validColumns = "abcdefgh"
            validRows    = "12345678"

            col1 = response[0]
            row1 = response[1]
            col2 = response[2]
            row2 = response[3]

            if (col1 not in validColumns) or   \
               (row1 not in validRows) or      \
               (col2 not in validColumns) or   \
               (row2 not in validRows):
                self._printHelp()
                continue

            return response

    def _printHelp(self):
        helpText = "\n Type the starting and ending coordinates.\n" \
                   " For example, 'b1c3'.\n\n" \
                   " Type quit to quit.\n"
        print helpText

