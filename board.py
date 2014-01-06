#!/usr/bin/python

import constants

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
        self._currentPlayer = constants.WHITE_PLAYER

    def getBoard(self):
        """
        Returns a copy of the current board's
        state.

        @return:    Copy of board (as list of lists)
        """
        return self._board
    
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
        
    def isLegalMove(self, move):
        """
        Determines if a move is legal or not.
        A move is not legal if any of the following is true:
         a) piece is not actually moved (e.g. 'a5a5')
         b) move refers to empty space
         c) the game piece is not owned by the current player
         d) a game piece owned by the same player is at the destination
         e) the move is not legal for the game piece
         f) a game piece is blocking the path of the move 
         g) not moving into check 

        @precondition: Method presumes that move is well-formed.
        (e.g. row and column values are correct)

        @param move:        Four letter combination representing move. (e.g. "b3c4") 
        @return:            True if move is legal, False otherwise.
        """
        validity = True
        
        #a) piece is not actually moved (e.g. 'a5a5') 
        if move[0:2]==move[2:4]:
            print "Doesn't work because no piece moved."
            return False
        else:
            validity = True
        
        #converts move to new syntax
        move = self._moveConverter(move)
        
        #b) move refers to empty space
        if self._board[move[0]][move[1]] == "":
            print "No piece there."
            return False

        """
        #CW - Code in progress..
    
        #JDL Hint: Create a method that helps you determine which player 
        #          owns a piece (at a given spot). Call that method here.
        #          This should make this method considerably smaller
        #          (and also easier to read).

        #JDL Hint2: Replace '*' with constants.BLACK_PLAYER_SYMBOL
        #           '*' is a 'magic value'. It's not obvious to
        #           the reader what it represents.

        #c) the game piece is not owned by the current player
        print self._currentPlayer
        print self._board[move[0]][move[1]]
        
        if self._currentPlayer == constants.WHITE_PLAYER:
            if "*" in self._board[move[0]][move[1]]:
                print "Piece not owned by player"
                return False
            else:
                validity = True
        if self._currentPlayer == constants.BLACK_PLAYER:
            if "*" not in self._board[move[0]][move[1]]:
                print "Piece not owned by player"
                return False
            else: 
                validity = True
       
        #d) a game piece owned by the same player is at the destination
        if self._currentPlayer == constants.WHITE_PLAYER:
            if "*" not in self._board[move[2]][move[3]] and not self._board[move[2]][move[3]] == "":
                print "Can't capture own piece"
                return False
            else:
                validity = True
        if self._currentPlayer == constants.BLACK_PLAYER:
            if "*" in self._board[move[2]][move[3]] and not self._board[move[2]][move[3]] == "":
                print "Can't capture own piece"
                return False
            else:
                validity = True
            
        #JDL Hint: Replace 'p' with constants.PAWN_SYMBOL, 
        #                  'r' with constants.ROOK_SYMBOL, etc.
        #          When someone reads 'p', they won't know what it means.
        #          (It's a 'magic value' like we were talking about)
        #          constants.PAWN_SYMBOL makes it much more obvious. 

        #e) the move is not legal for the game piece
        if 'p' in self._board[move[0]][move[1]]:
            if self._isLegalMoveForPawn(move) == True:
                validity = True
            else:
                return False
        if 'r' in self._board[move[0]][move[1]]:
            if self._isLegalMoveForRook(move) == True:
                validity = True
            else:
                return False
        if 'n' in self._board[move[0]][move[1]]:
            if self._isLegalMoveForKnight(move) == True:
                validity = True
            else:
                return False
        if 'b' in self._board[move[0]][move[1]]:
            if self._isLegalMoveForBishop(move) == True:
                validity = True
            else:
                return False
        if 'q' in self._board[move[0]][move[1]]:
            if self._isLegalMoveForQueen(move) == True:
                validity = True
            else:
                return False
        if 'k' in self._board[move[0]][move[1]]:
            if self._isLegalMoveForKing(move) == True:
                validity = True
            else:
                return False
        """
        #f) a game piece is blocking the path of the move 
        
        #g) not moving into check
         
        return validity

    def pieceOwner(self, loc):
        """
        Determines which player owns a given piece.

        @param loc:         Location on game board (e.g. "b5")
        @return:            Player (e.g. constants.WHITE_PLAYER)
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
        A move for a queen is legal is the Queen i) stays in the same column, or ii)stays in the same row, or iii)changes the row and column by the same amount (as in up 3 over 3 or up 4 over 4)
        """

        #if queen stays in same column
        if move[0]==move[2]:
            validity=True
        #if queen stays in same row
        elif move[1]==move[3]:
            validity==True
        #if change of row and column is the same
        elif abs(move[2] - move[0]) == abs(move[3] - move[1]):
            validity==True
        else: 
            print "Not a valid move for a Queen"
            validity = False
        return validity

    def _isLegalMoveForKing(self, move):
        """
        Helper method for determining if move is legal for king.
        """
        #(Replace this with a real test)
        return True

    def _isLegalMoveForPawn(self, move):
        #checks different situations, then returns either True or False
        """
        Helper method for determining if move is legal for pawn.
        """
        #moving ahead 2 spaces (for white piece or for black piece)
        if (move[1] + 2 == move[3] and move [0]==move[2] or move[1] - 2 == move[3] and move [0]==move[2]):
            #this should only work if the piece is in row 2 or row 7
            if (move[1]==1 or move [1]==6):
                validity=True
            else:
                print "You can't move 2 spaces from row ", move[1]
                validity=False
        #moving ahead 1 space (for white piece or black piece)
        elif (move[1] + 1 == move[3] and move[0]==move[2] or move[1] - 1 == move[3] and move[0]==move[2]):
            validity = True
        #taking another piece for white piece
        elif (move[1] + 1 == move[3] and move[0] + 1 == move[2] or move[1] + 1 ==move[3] and move[0] - 1 == move[2]):
            if self._board[move[2]][move[3]] == "":
                print "A pawn can not move diagonally to an empty space"
                validity=False
            else:
                validity=True
        #taking another piece for black piece
        elif ((move[1] - 1 == move[3] and move[0] + 1 == move[2]) or (move[1] - 1 ==move[3] and move[0] - 1 == move[2])):
            if self._board[move[2]][move[3]] == "":
                print "A pawn can not move diagonally to an empty space"
                validity=False
            else:
                validity=True
        else:
            validity = False

        return validity

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
