#!/usr/bin/python

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
        self._board = [ ['r','p','','','','','*p','*r'],
                        ['n','p','','','','','*p','*n'],
                        ['b','p','','','','','*p','*b'],
                        ['q','p','','','','','*p','*q'],
                        ['k','p','','','','','*p','*k'],
                        ['b','p','','','','','*p','*b'],
                        ['n','p','','','','','*p','*n'],
                        ['r','p','','','','','*p','*r'] ]

        #Current player
        self._currentPlayer = 1      # 1 => White, 2 => Black

    def getBoard(self):
        """
        Returns a copy of the current board's
        state.

        @return:    Copy of board (as list of lists)
        """
        return self._board

    def isLegalMove(self, move):
        """
        Determines if a move is legal or not.
        A move is not legal if any of the following is true:
         a) move refers to empty space
         b) the game piece is not owned by the current player
         c) a game piece owned by the same player is at the destination
         d) the move is not legal for the game piece
         e) a game piece is blocking the path of the move  

        @param move:        Four letter combination representing move. (e.g. "b3c4") 
        @return:            True if move is legal, False otherwise.
        """
        #(Replace this with a real test)
        return True

    def pieceOwnedBy(self, loc):
        """
        Determines which player owns a given piece.

        @param loc:         Location on game board (e.g. "b5")
        @return:            Player number (1 or 2).
        """
        pass

    def _isLegalMoveForRook(self, move):
        """
        Helper method for determining if move is legal for rook.
        """
        #(Replace this with a real test)
        return True

    def _isLegalMoveForKnight(self, move):
        """
        Helper method for determining if move is legal for knight.
        """
        #(Replace this with a real test)
        return True

    def _isLegalMoveForBishop(self, move):
        """
        Helper method for determining if move is legal for bishop.
        """
        #(Replace this with a real test)
        return True

    def _isLegalMoveForQueen(self, move):
        """
        Helper method for determining if move is legal for queen.
        """
        #(Replace this with a real test)
        return True

    def _isLegalMoveForKing(self, move):
        """
        Helper method for determining if move is legal for king.
        """
        #(Replace this with a real test)
        return True

    def _isLegalMoveForPawn(self, move):
        """
        Helper method for determining if move is legal for pawn.
        """
        #(Replace this with a real test)
        return True

    ################################################################

    def movePiece(self, move):
        """
        Moves chess piece.

        @precondition:      isLegalMove() must be True.
        @param move:        Four letter combination representing move. (e.g. "b3c4") 
        """

        #Note: You can write this method before writing all of the
        #isLegalMove methods (since they all return True right now)

        pass

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
