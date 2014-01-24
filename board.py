#!/usr/bin/python

from operator import xor

import constants
import board_analyzer

class Board(object):

    def __init__(self):
        """
        Initializes a new chess board.
        """
        #Board is a list of lists
        #To access element, write
        # self._board[<col#>][<row#>]
        #
        #See http://i.stack.imgur.com/7KSiN.png
        #for picture of board layout

        ################################################
        self._board = [ ['r','p','','','','','*p','*r'],
                        ['n','p','','','','','*p','*n'],
                        ['b','p','','','','','*p','*b'],
                        ['q','p','','','','','*p','*q'],
                        ['k','p','','','','','*p','*k'],
                        ['b','p','','','','','*p','*b'],
                        ['n','p','','','','','*p','*n'],
                        ['r','p','','','','','*p','*r'] ]

    def getBoard(self):
        """
        Returns a copy of the current board's
        state.

        @return:    Copy of board (as list of lists)
        """
        return self._board
    
    def pieceOwner(self, specific_move):
        """
        Returns the owner of a given piece
        
        @param move    The space you are trying to check (e.g. [a2])
        @return:       Either constants.WHITE_PLAYER or constants.BLACK_PLAYER
        """
        if constants.BLACK_PLAYER_SYMBOL in self._board[specific_move[0]][specific_move[1]]:
            return constants.BLACK_PLAYER
        elif constants.EMPTY_SYMBOL == self._board[specific_move[0]][specific_move[1]]:
            return constants.EMPTY_SYMBOL
        else:
            return constants.WHITE_PLAYER
    
    def _moveConverter(self, move):
        """
        Converts move from original string input to a list of integers 
        (e.g. "a2a3" => [0,1,0,2])

        @param move:    Player's move (e.g. "a2a3")
        @return:        List containing indices for board data structure.
                        (e.g. [0,1,0,2])
        """
        converter = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
        new_move = []
        for string in move:
            if string in converter:
                new_move.append(converter[string])
            else:
                new_move.append(int(string)-1)
        move = new_move
        return move
        
    def isLegalMove(self, currentPlayer, move):
        """
        Determines if a move is legal or not.
        A move is not legal if any of the following is true:
         a) piece is not actually moved (e.g. 'a5a5')
         b) move refers to empty space
         c) the game piece is not owned by the current player
         d) a game piece owned by the same player is at the destination
         e) the move is not legal for the game piece
         f) not moving into check 

        @precondition: Method presumes that move is well-formed.
        (e.g. row and column values are correct)

        @param move:        Four letter combination representing move. (e.g. "b3c4") 
        @return:            True if move is legal, False otherwise.
        """
        #a)Tests for whether a piece is not actually moved (e.g. 'a5a5') 
        if move[0:2] == move[2:4]:
            return False
        else:
            validity = True
        
        #b)Tests if there is a piece in the targeted space
        if self._board[move[0]][move[1]] == constants.EMPTY_SYMBOL:
            return False
        else:
            validity = True
            
        #c)Tests if the game piece is not owned by the current player
        if currentPlayer != self.pieceOwner([move[0], move[1]]):
            return False
        else:
            validity = True
       
        #d)Tests if game piece owned by the current player occupies end destination
        if currentPlayer == self.pieceOwner([move[2], move[3]]):
            return False
        else:
            validity = True
        
        #e)Tests whether the move is legal for a specific piece
        if constants.PAWN_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForPawn(move, currentPlayer) == True:
                validity = True
            else:
                return False
        if constants.ROOK_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForRook(move) == True:
                validity = True
            else:
                return False
        if constants.KNIGHT_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForKnight(move) == True:
                validity = True
            else:
                return False
        if constants.BISHOP_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForBishop(move) == True:
                validity = True
            else:
                return False
        if constants.QUEEN_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForQueen(move) == True:
                validity = True
            else:
                return False
        if constants.KING_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForKing(move) == True:
                validity = True
            else:
                return False
        
        #f)Tests whether current player's move will move current player in check
        if board_analyzer.isCheck(self._board, currentPlayer, move) == True:
            return False
        else:
            validity = True

        return validity

    def _isLegalMoveForRook(self, move):
        """
        Helper method for determining if move is legal for rook.
        """
        horizontal = None
        vertical = None
        horizontal_blocking = None
        vertical_blocking = None
            
        #Allows for horizontal movement
        if move[1] == move[3]:
            horizontal = True

        #Allows for vertical movement
        if move[0] == move[2]:
            vertical = True
        
        #Tests whether piece in path of horizontal movement
        blocked_spaces = 0
        for space in range(move[0] + 1, move[2]):
            if constants.EMPTY_SYMBOL != self._board[space][move[1]]:
                blocked_spaces += 1
        if blocked_spaces == 0:
            horizontal_blocking = True

        #Tests whether piece in path of vertical movement
        blocked_spaces = 0
        for space in range(move[1] + 1, move[3]):
            if constants.EMPTY_SYMBOL != self._board[move[0]][space]:
                blocked_spaces += 1
        if blocked_spaces == 0:
            vertical_blocking = True

        if xor((horizontal and horizontal_blocking) == True, \
            (vertical and vertical_blocking) == True):
            return True
        else:
            return False

    def _isLegalMoveForKnight(self, move):
        """
        Helper method for determining if move is legal for knight.
        """
        if (move[0] + 2 == move[2] and move[1] + 1 == move[3]) or \
        (move[0] + 2 == move[2] and move[1] - 1 == move[3]) or \
        (move[0] - 2 == move[2] and move[1] + 1 == move[3]) or \
        (move[0] - 2 == move[2] and move[1] - 1 == move[3]) or \
        (move[0] + 1 == move[2] and move[1] + 2 == move[3]) or \
        (move[0] + 1 == move[2] and move[1] - 2 == move[3]) or \
        (move[0] - 1 == move[2] and move[1] + 2 == move[3]) or \
        (move[0] - 1  == move[2] and move[1] - 2 == move[3]):
            return True
        else:
            return False

    def _isLegalMoveForBishop(self, move):
        """
        Helper method for determining if move is legal for bishop.
        """
        #Allows for diagonal movement
        if abs(move[2] - move[0]) != abs(move[3] - move[1]):
            return False

        #Test whether piece in path of upper-right diagonal movement
        if move[2] - move[0] > 0 and move[3] - move[1] > 0:
            for space in range(1, abs(move[2] - move[0])):
                if constants.EMPTY_SYMBOL != self._board[move[0] + space][move[1] + space]:
                    return False
                
        #Test whether piece in path of upper-left diagonal movement
        if move[2] - move[0] < 0 and move[3] - move[1] > 0:
            for space in range(1, abs(move[2] - move[0])):
                if constants.EMPTY_SYMBOL != self._board[move[0] - space][move[1] + space]:
                    return False
                
        #Test whether piece in path of lower-right diagonal movement
        if move[2] - move[0] > 0 and move[3] - move[1] < 0:
            for space in range(1, abs(move[2] - move[0])):
                if constants.EMPTY_SYMBOL != self._board[move[0] + space][move[1] - space]:
                    return False
                
        #Test whether piece in path of lower-left diagonal movement
        if move[2] - move[0] < 0 and move[3] - move[1] < 0:
            for space in range(1, abs(move[2] - move[0])):
                if constants.EMPTY_SYMBOL != self._board[move[0] - space][move[1] - space]:
                    return False

        return True

    def _isLegalMoveForQueen(self, move):
        """
        Helper method for determining if move is legal for queen.
        
        Calls isLegalMoveForRook and isLegalMoveForBishop since queen
        movements are either rook-like or bishop-like
        """
        if xor(self._isLegalMoveForRook(move), self._isLegalMoveForBishop(move)) == True:
            return True
        else:
            return False

    def _isLegalMoveForKing(self, move):
        """
        Helper method for determining if move is legal for king.
        """
        #Allows for horizontal movement
        if (move[0] + 1 == move[2] or move[0] - 1 == move[2]):
            return True
        else:
            validity = False
        
        #Allows for vertical movement
        if (move[1] + 1 == move[3] or move[1] - 1 == move[3]):
            return True
        else:
            validity = False
            
        #Allows for diagonal movement
        if (move[0] + 1 == move[2] and move[1] + 1 == move[3]) or \
        (move[0] - 1 == move[2] and move[1] - 1 == move[3]) or \
        (move[0] + 1 == move[2] and move[1] - 1 == move[3]) or \
        (move[0] - 1 == move[2] and move[1] + 1 == move[3]):
            return True
        else:
            validity = False
        
        return validity

    def _isLegalMoveForPawn(self, move, currentPlayer):
        """        
        Helper method for determining if move is legal for pawn.
        """
        if currentPlayer == constants.WHITE_PLAYER:
            #Pawns can move up one space at a time
            if self._board[move[0]][move[1] + 1] == constants.EMPTY_SYMBOL:
                if move[1] + 1 == move[3] and move[0] == move[2]:
                    return True
            #Pawns can move up two spaces at the start
            if move[1] == 1:
                if (move[1] + 2 == move[3]) and \
                   (self._board[move[0]][move[1] + 2] == constants.EMPTY_SYMBOL) and \
                    move[0] == move[2]:
                    return True
            #Allows for NE attack
            if self.pieceOwner([move[0] + 1, move[1] + 1]) == constants.BLACK_PLAYER:
                return True
            #Allows for NW attack
            if self.pieceOwner([move[0] - 1, move[1] + 1]) == constants.BLACK_PLAYER:
                return True
            
        elif currentPlayer == constants.BLACK_PLAYER:
            #Pawns can move up one space at a time
            if self._board[move[0]][move[1] - 1] == constants.EMPTY_SYMBOL:
                if move[1] - 1 == move[3] and move[0] == move[2]:
                    return True
            #Pawns can move up two spaces at the start
            if move[1] == 6:
                if (move[1] - 2 == move[3]) and \
                   (self._board[move[0]][move[1] - 2] == constants.EMPTY_SYMBOL) and \
                   move[0] == move[2]:
                    return True
            #Allows for NE attack
            if self.pieceOwner([move[0] + 1, move[1] - 1]) == constants.BLACK_PLAYER:
                return True            
            #Allows for NW attack
            if self.pieceOwner([move[0] - 1, move[1] - 1]) == constants.BLACK_PLAYER:
                return True

        return False

    ################################################################

    def movePiece(self, currentPlayer, move):
        """
        Moves chess piece.

        @precondition:      isLegalMove() must be True.
        @param move:        Four letter combination representing move. (e.g. "b3c4") 
        """
        targetPiece = self._board[move[0]][move[1]]
        self._board[move[2]][move[3]] = targetPiece
        self._board[move[0]][move[1]] = constants.EMPTY_SYMBOL
    
    ################################################################

    def printBoard(self):
        """
        Prints the board.
        """
        divider = "  +----+----+----+----+----+----+----+----+"

        #Print each row
        row = 7
        while row >= 0:
            print divider
            
            #Print each column
            col = 0
            text = "%s |" % str(row + 1)
            while col < 8:
                piece = self._board[col][row]
                text += " %2s |" % piece
                col = col + 1
            print text

            #Next row
            row = row - 1

        print divider

        print "\n     a    b    c    d    e    f    g    h"
