#!/usr/bin/python

from operator import xor

import constants
import board_analyzer

import pdb

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
        #Checks for owner of a given piece
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
            print "Doesn't work because no piece moved."
            return False
        else:
            validity = True
        
        #b)Tests if there is a piece in the targeted space
        if self._board[move[0]][move[1]] == constants.EMPTY_SYMBOL:
            print "No piece there."
            return False
        else:
            validity = True
            
        #c)Tests if the game piece is not owned by the current player
        if currentPlayer != self.pieceOwner([move[0], move[1]]):
            print "Piece not owned by player"
            return False
        else:
            validity = True
       
        #d)Tests if game piece owned by the current player occupies end destination
        if currentPlayer == self.pieceOwner([move[2], move[3]]):
            print "Endpoint space has piece currently owned by player"
            return False
        else:
            validity = True
        
        #e)Tests whether the move is legal for a specific piece
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
        if constants.PAWN_SYMBOL in self._board[move[0]][move[1]]:
            if self._isLegalMoveForPawn(move, currentPlayer) == True:
                validity = True
            else:
                return False
        
        #f)Tests whether current player's move will move current player in check
        self._testBoard = self._board
        testPiece = self._board[move[0]][move[1]]
        self._testBoard[move[2]][move[3]] = testPiece
        
        if board_analyzer.isCheck(self._testBoard, currentPlayer) == True:
            print "Cannot move into check."
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
                blocked_space += 1
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
        A move for a queen is legal is the Queen i) stays in the same column, or ii)stays in the same row, or iii)changes the row and column by the same amount (as in up 3 over 3 or down 4 over 4)
        """
        
        #if queen stays in same column
        if move[0]==move[2]:
            i=1
            validity = True
            #check if there are any pieces in the way
            if move[3]>move[1]:
                while i<(abs(move[3]-move[1])):
                    if constants.EMPTY_SYMBOL==self._board[move[0]][(move[3]-i)]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
            else:
                while i<(abs(move[1]-move[3])):
                    if constants.EMPTY_SYMBOL==self._board[move[0]][(move[1]-i)]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
        #if queen stays in same row
        elif move[1]==move[3]:
            #check if there are any pieces in the way
            i=1
            validity = True
            if move[3]>move[1]:
                while i<(abs(move[2]-move[0])):
                    if constants.EMPTY_SYMBOL==self._board[(move[2]-i)][move[1]]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
            else:
                while i<(abs(move[0]-move[2])):
                    if constants.EMPTY_SYMBOL==self._board[(move[0]-i)][move[1]]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
        #if change of row and column is the same
        elif abs(move[2] - move[0]) == abs(move[3] - move[1]):
            #check if there are any pieces in the way
            i=1
            #if move is up and right
            if (move[2]>move[0] and move[3]>move[1]):
                while i<(abs(move[2]-move[0])):
                    if constants.EMPTY_SYMBOL==self._board[(move[0]+i)][(move[1]+i)]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
            #if move is down and right
            if (move[2]>move[0] and move[1]>move[3]):
                while i<(abs(move[2]-move[0])):
                    if constants.EMPTY_SYMBOL==self._board[(move[0]+i)][(move[1]-i)]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
            #if move is up and left
            if (move[0]>move[2] and move[3]>move[1]):
                while i<(abs(move[0]-move[2])):
                    if constants.EMPTY_SYMBOL==self._board[(move[0]-i)][(move[1]+i)]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
            #if move is down and left
            if (move[0]>move[2] and move[1]>move[3]):
                while i<(abs(move[0]-move[2])):
                    if constants.EMPTY_SYMBOL==self._board[(move[0]-i)][(move[1]-i)]:
                        validity=True
                        i+=1
                    else:
                        print "There is a piece in the way!"
                        return False
            
            validity=True
            
        else: 
            print "Our Queen would not do that; it is not a valid move for a queen!"
            validity = False
        return validity
        
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
        #white pieces can only move up, black pices can only move down
        if ((currentPlayer==constants.WHITE_PLAYER and move[3]<move[1]) or (currentPlayer==constants.BLACK_PLAYER and move[1]<move[3])):
            print "You can't move backwards"
            return False
        else:
            #staying in the same column
            if move[0]==move[2]:
                #this only works if the pawn is being moved into an empty spot
                if self._board[move[2]][move[3]]!=constants.EMPTY_SYMBOL:
                    print "That spot has a piece in it!"
                    return False
                else:
                    #moving ahead 2 spaces (for white piece or for black piece)
                    if (move[1] + 2 == move[3] or move[1] - 2 == move[3]):
                        #this should only work if the piece is in row 2 or row 7
                        if (move[1]==1 or move [1]==6):
                            #should only work if there is no piece in the way
                            i=1
                            while i<(abs(move[3]-move[1])):
                                if constants.EMPTY_SYMBOL==self._board[move[0]][(move[3]-i)]:
                                    validity=True
                                    i+=1
                            validity=True
                        else:
                            print "You can't move 2 spaces from row ", move[1]+1
                            validity=False
                    #moving ahead 1 space (for white piece or black piece)
                    elif (move[1] + 1 == move[3] or move[1] - 1 == move[3]):
                        #pawn promotion
                        if move[3]==7 or move[3]==0:
                            print "Your pawn has reached the other side. Which piece would you like to promote your pawn to? \n"
                            newpiece = raw_input("Type q for queen, b for bishop, n for knight or r for rook")
                            while newpiece not in 'qbnr':
                                newpiece = raw_input("Try again. Type q for queen, b for bishop, n for knight or r for rook")
                            else:
                                if currentPlayer == constants.WHITE_PLAYER:
                                    if newpiece == 'q':
                                        newpiece = constants.QUEEN_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        a = self._board[move[0]][move[1]]
                                        b = constants.QUEEN_SYMBOL
                                        print a
                                        print b
                                        if a==b:
                                            print 'yes'
                                        else:
                                            print 'no'    
                                    elif newpiece == 'b':
                                        newpiece = constants.BISHOP_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        print self._board[move[0]][move[1]]
                                    elif newpiece == 'n':
                                        newpiece = constants.KNIGHT_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        print self._board[move[0]][move[1]]
                                    else:
                                        newpiece = constants.ROOK_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        print self._board[move[0]][move[1]]
                                else:
                                    if newpiece == 'q':
                                        newpiece = constants.BLACK_PLAYER_SYMBOL+constants.QUEEN_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        a = self._board[move[0]][move[1]]
                                        b = constants.QUEEN_SYMBOL
                                        print a
                                        print b
                                        if a==b:
                                            print 'yes'
                                        else:
                                            print 'no'    
                                    elif newpiece == 'b':
                                        newpiece = constants.BLACK_PLAYER_SYMBOL+constants.BISHOP_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        print self._board[move[0]][move[1]]
                                    elif newpiece == 'n':
                                        newpiece = constants.BLACK_PLAYER_SYMBOL+constants.KNIGHT_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        print self._board[move[0]][move[1]]
                                    else:
                                        newpiece = constants.BLACK_PLAYER_SYMBOL+constants.ROOK_SYMBOL
                                        self._board[move[0]][move[1]]=newpiece
                                        print self._board[move[0]][move[1]]
                        validity = True
                    else:
                        print "A pawn can only move ahead 1 or 2 spaces, not ", abs(move[3]-move[1])
                        return False
                    
            #taking another piece for white piece
            elif ((abs(move[0]-move[2])==1) and move[1]+1==move[3]):
                if self._board[move[2]][move[3]] == constants.EMPTY_SYMBOL:
                    print "A pawn can not move diagonally to an empty space"
                    return False
                else:
                    validity=True
            #taking another piece for black piece
            elif ((abs(move[0]-move[2])==1) and move[1]-1==move[3]):
                if self._board[move[2]][move[3]] == constants.EMPTY_SYMBOL:
                    print "A pawn can not move diagonally to an empty space"
                    validity=False
                else:
                    validity=True
            else:
                validity = False

        return validity

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
