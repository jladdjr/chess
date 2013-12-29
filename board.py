#!/usr/bin/python

class Board(object):

    def __init__(self):
        """
        Initializes a new chess board.
        """
        #Board is a list of lists
        #To access element, write
        # self.board[<col#>][<row#>]
        #
        #See http://i.stack.imgur.com/7KSiN.png
        #for picture of board layout 
        self.board = [ ['r','p','','','','','*p','*r'],
                       ['n','p','','','','','*p','*n'],
                       ['b','p','','','','','*p','*b'],
                       ['q','p','','','','','*p','*q'],
                       ['k','p','','','','','*p','*k'],
                       ['b','p','','','','','*p','*b'],
                       ['n','p','','','','','*p','*n'],
                       ['r','p','','','','','*p','*r'] ]

        #Last player to move
        self.lastPlayer = None

        #Last move
        self.lastMove = None

    def isLegalMove(self, orig, dest):
        """
        Determines if a move is legal or not.
        A move is not legal if any of the following is true:
         a) move refers to empty space
         b) the game piece is not owned by the current player
         c) a game piece owned by the same player is at the destination
         d) the move is not legal for the game piece
         e) a game piece is blocking the path of the move  

        @param orig:        Origin. Starting location of game piece. (e.g. "b5")
        @param dest:        Destination. Final location of game piece. (e.g. "b6")
        @return:            True if move is legal, False otherwise.
        """
        pass

    def pieceOwnedBy(self, loc):
        """
        Determines which player owns a given piece.

        @param loc:         Location on game board (e.g. "b5")
        @return:            Player number (1 or 2).
        """
        pass

    def _isLegalMoveForRook(self, orig, dest):
        """
        Helper method for determining if move is legal for rook.
        """
        pass

    def _isLegalMoveForKnight(self, orig, dest):
        """
        Helper method for determining if move is legal for knight.
        """
        pass

    def _isLegalMoveForBishop(self, orig, dest):
        """
        Helper method for determining if move is legal for bishop.
        """
        pass

    def _isLegalMoveForQueen(self, orig, dest):
        """
        Helper method for determining if move is legal for queen.
        """
        pass

    def _isLegalMoveForKing(self, orig, dest):
        """
        Helper method for determining if move is legal for king.
        """
        pass

    def _isLegalMoveForPawn(self, orig, dest):
        """
        Helper method for determining if move is legal for pawn.
        """
        pass

    ################################################################

    def movePiece(self, orig, dest):
        """
        Moves chess piece.

        @precondition:      isLegalMove() must be True.
        @param orig:        Origin. Starting location of game piece. (e.g. "b5")
        @param dest:        Destination. Final location of game piece. (e.g. "b6")
        """
        pass

    ################################################################

    def isCheckMate(self):
        """
        Determines if game has ended.

        @return True if game has ended, False otherwise.
        """
        pass

    def isCheck(self):
        """
        Determines if a king is in check. 

        @return True if king is in check, False otherwise. 
        """
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
                piece = self.board[col][row]
                text += " %2s |" % piece
                col = col + 1
            print text

            #Next row
            row = row - 1

        print divider

        print "\n     a    b    c    d    e    f    g    h"
