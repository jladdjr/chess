#!/usr/bin/python

import constants
import board
import pdb

def kingLocator(board, player):
    """
    Determines the location of the king of player
    
    @param board:   A list of lists representing the board state.
    @param player:  Player (e.g. constants.WHITE_PLAYER)
    @return:        returns list indicies of player's king
                    (e.g. [0, 4])
    """
    if player == constants.WHITE_PLAYER:
        piece = constants.KING_SYMBOL
    else:
        piece = constants.BLACK_KING_SYMBOL
        
    for line in board:
	if piece in line:
            location = [board.index(line), line.index(piece)]
                
    return location
def isCheckMate(board, player):
    """
    Determines if game has ended.

    @param board:   A list of lists representing the board state.
    @param player:  Player (e.g. constants.WHITE_PLAYER)
    @return True if game has ended, False otherwise.
    """
    
    """
    This method checks if a king can get out of check by:
    1.) running away to another spot on the board
    2.) having another piece block the path of check
    3.) having a piece kill and eat the piece that put king in check
    """   
    #1.) Can the king run away?
    location = kingLocator(board, player)
    #the king has 8 possible locations to move to. If king can move to any of them without being in check, this returns False, as in checkmate is False
    i=-1
    while i<2:
        j=-1
        while j<2:
            #if new spot is on the board, then we check it by putting the king in new spot and running isCheck on the new spot
            if (0<location[0]+i<len(board) and 0<location[1]+j<len(board)):
                #make a test board, makes king's spot blank, and puts king in test spot
                testBoard = board
                testPiece = constants.KING_SYMBOL
                testBoard[location[0]][location[1]] = constants.EMPTY_SYMBOL
                testBoard[location[0]+i][location[1]+j] = testPiece
                #tests new spot. If there is no check in the new spot, we make isCheckMate() return False
                if isCheck(testBoard,player)==False:
                    return False
            else:
                j+=1;
        i+=1
    else:
        #if the code gets here, then all of the king's possible moves would keep him in check
        pass
   
    #2.)Can another piece block the path of check?
    """
    We determine how many spots on the board are between the king and the piece that put it in check, and then determine if any piece of the king's color can move into any of these spots
    """
    #location of the piece that put the king in check 
    fromhere = checkmateLocation(board)
    
    #we go through horizontal, vertical, and diagonal scenarios. We don't need to check king, pawn, or knight checks, because those can't be blocked by moving in between that piece and the checked king
    pdb.set_trace()
    if isCheckByHorizontal(location, board, player) == True:
        #determine if check is from left or right. location is king's location
        #if check is from left
        if fromhere[0]<location[0]:
            i=1
            #while the king is to the right of the checking piece
            while location[0]-i>fromhere[0]:
                #the next spot is
                spot[0]=location[0]-i
                spot[1]=location[1]
                if CanPieceMoveToSpot(location,player,spot) == True:
                    return False
                i+=1
        #else check is from right
        else:
            i=1
            #while the king is to the left of the checking piece
            while location[0]+i<fromhere[0]:
                #the next spot is
                spot[0]=location[0]+i
                spot[1]=location[1]
                if CanPieceMoveToSpot(location,player,spot) == True:
                    return False
                i+=1

    if isCheckByVertical(location, board, player) == True:
        #determine if check is from up or down. location is king's location
        #if check is from up
        if fromhere[1]<location[1]:
            i=1
            #while the king is down from the checking piece
            while location[1]+i<fromhere[1]:
                #the next spot is
                spot[0]=location[0]
                spot[1]=location[1]+i
                if CanPieceMoveToSpot(location,player,spot) == True:
                    return False
                i+=1
        #if check is from down
        else:
            i=1
            #while the king is down from the checking piece
            while location[1]-i>fromhere[1]:
                #the next spot is
                spot[0]=location[0]
                spot[1]=location[1]-i
                if CanPieceMoveToSpot(location,player,spot) == True:
                    return False
                i+=1
    if isCheckByDiagonal(location, board, player) == True:
        #determine if check is from NW, NE, SE, or SW. location is king's location
        #if check is from NW (left and up)
        if (fromhere[0]<location[0] and fromhere[1]>location[1]):
        #if check is from NE (right and up)
        if (fromhere[0]>location[0] and fromhere[1]>location[1]):
        #if check is from SE (right and down)
        if (fromhere[0]>location[0] and fromhere[1]<location[1]):
        #if check is from SW (left and down)
        if (fromhere[0]<location[0] and fromhere[1]<location[1]):        
        
    #3.)Can another piece kill and eat the piece that put the king in check?
"""
    We look at all of the pieces of the same color as the king and determine if they can move into the spot that is being occupied by the piece that put the king in check
"""
    
    #(Replace this with a real test)
    #return False

def isCheck(board, player):
    """
    Determines if a king is in check.

    @param board:   A list of lists representing the board state.
    @param player:  Player (e.g. constants.WHITE_PLAYER)
    @return True if king is in check, False otherwise.
    """
    location = kingLocator(board, player)
    
    if isCheckByHorizontal(location, board, player) == True:
        return True
    if isCheckByVertical(location, board, player) == True:
        return True
    if isCheckByKing(location, board, player) == True:
        return True
    if isCheckByPawn(location, board, player) == True:
        return True
    if isCheckByKnight(location, board, player) == True:
        return True

    return False

def isCheckByDiagonal(location, board, player):
    """
    Helper method to determine if king under attack by rook or queen horizontally.
    """
    """
    if player == constants.WHITE_PLAYER:
    #For NE diagonal
        for space in range(location[0] + 1, len(board)):
            if board[location[0] + space, location[1] + space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] + space, location[1] + space] == constants.BLACK_QUEEN_SYMBOL:
                return True
    #For NW diagonal
        for space in range(location[0] + 1, len(board)):
            if board[location[0] - space, location[1] + space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] - space, location[1] + space] == constants.BLACK_QUEEN_SYMBOL:
                return True
    #For SE diagonal
        for space in range(location[0] + 1, len(board)):
            if board[location[0] + space, location[1] - space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] + space, location[1] - space] == constants.BLACK_QUEEN_SYMBOL:
                return True
    #For SW diagonal
        for space in range(location[0] + 1, len(board)):
            if board[location[0] - space, location[1] - space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] - space, location[1] - space] == constants.BLACK_QUEEN_SYMBOL:
                return True
        
    else:
    """
    pass

def isCheckByHorizontal(location, board, player):
    """
    Helper method to determine if king under attack by rook or queen horizontally.
    """
    if player == constants.WHITE_PLAYER:
        #Checks for rooks and queens in the same row as king
        for space in range(len(board)):
            if board[space][location[1]] == constants.BLACK_ROOK_SYMBOL or \
            board[space][location[1]] == constants.BLACK_QUEEN_SYMBOL:
                #Checks for blocking pieces if piece comes before the king horizontally
                if space < location[0]:
                    blocking = 0
                    for new_space in range(space + 1, location[0]):
                        if board[new_space][location[1]] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True
                #Checks for blocking pieces if piece comes after the king horizontally
                else:
                    blocking = 0
                    for new_space in range(location[0] + 1, space):
                        if board[new_space][location[1]] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True

        return False
                    
    else:
        #Checks for rooks and queens in the same row as king
        for space in range(len(board)):
            if board[space][location[1]] == constants.ROOK_SYMBOL or \
            board[space][location[1]] == constants.QUEEN_SYMBOL:
                #Checks for blocking pieces if piece comes before the king horizontally
                if space < location[0]:
                    blocking = 0
                    for new_space in range(space + 1, location[0]):
                        if board[new_space][location[1]] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True
                #Checks for blocking pieces if piece comes after the king horizontally
                else:
                    blocking = 0
                    for new_space in range(location[0] + 1, space):
                        if board[new_space][location[1]] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True

        return False
                    
def isCheckByVertical(location, board, player):
    """
    Helper method to determine if king under attack by rook or queen vertically
    """
    if player == constants.WHITE_PLAYER:
        #Checks for rooks and queens in same column as king
        for space in range(len(board)):
            if board[location[0]][space] == constants.BLACK_ROOK_SYMBOL or \
            board[location[0]][space] == constants.BLACK_QUEEN_SYMBOL:
                #Checks for blocking pieces if piece comes before the king vertically
                if space < location[1]:
                    blocking = 0
                    for new_space in range(space + 1, location[1]):
                        if board[location[0]][new_space] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True
                #Checks for blocking pieces if piece comes after the king horizontally
                else:
                    blocking = 0
                    for new_space in range(location[1] + 1, space):
                        if board[location[0]][new_space] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True
                    
        return False
                    
    else:
        #Checks for rooks and queens in same column as king
        for space in range(len(board)):
            if board[location[0]][space] == constants.ROOK_SYMBOL or \
            board[location[0]][space] == constants.QUEEN_SYMBOL:
                #Checks for blocking pieces if piece comes before the king vertically
                if space < location[1]:
                    blocking = 0
                    for new_space in range(space + 1, location[1]):
                        if board[location[0]][new_space] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True
                #Checks for blocking pieces if piece comes after the king vertically
                else:
                    blocking = 0
                    for new_space in range(location[1] + 1, space):
                        if board[location[0]][new_space] != constants.EMPTY_SYMBOL:
                            blocking += 1
                    if blocking == 0:
                        return True

        return False
                    
def isCheckByKing(location, board, player):
    """
    Helper method to determine if king under attack by knight.
    """
    if player == constants.WHITE_PLAYER:
        #Checks if white king is in check by black king
        if 1 <= location[0]:
            if board[location[0] - 1][location[1]] == constants.BLACK_KING_SYMBOL:
                return True
        if location[0] <= 6:
            if board[location[0] + 1][location[1]] == constants.BLACK_KING_SYMBOL:
                return True
        if 1 <= location[1]:
            if board[location[0]][location[1] - 1] == constants.BLACK_KING_SYMBOL:
                return True
        if location[1] <= 6:
            if board[location[0]][location[1] + 1] == constants.BLACK_KING_SYMBOL:
                return True
        if 1 <= location[0] and 1 <= location[1]:
            if board[location[0] - 1][location[1] - 1] == constants.BLACK_KING_SYMBOL:
                return True
        if location[0] <= 6 and 1 <= location[1]:
            if board[location[0] + 1][location[1] - 1] == constants.BLACK_KING_SYMBOL:
                return True
        if location[0] <= 1 and location[1] <= 6:
            if board[location[0] - 1][location[1] + 1] == constants.BLACK_KING_SYMBOL:
                return True
        if location[0] <= 6 and location[1] <= 6:
            if board[location[0] + 1][location[1] + 1] == constants.BLACK_KING_SYMBOL:
                return True
            
        return False

    else:
        #Checks if black king is in check by white king
        if 1 <= location[0]:
            if board[location[0] - 1][location[1]] == constants.KING_SYMBOL:
                return True
        if location[0] <= 6:
            if board[location[0] + 1][location[1]] == constants.KING_SYMBOL:
                return True
        if 1 <= location[1]:
            if board[location[0]][location[1] - 1] == constants.KING_SYMBOL:
                return True
        if location[1] <= 6:
            if board[location[0]][location[1] + 1] == constants.KING_SYMBOL:
                return True
        if 1 <= location[0] and 1 <= location[1]:
            if board[location[0] - 1][location[1] - 1] == constants.KING_SYMBOL:
                return True
        if location[0] <= 6 and 1 <= location[1]:
            if board[location[0] + 1][location[1] - 1] == constants.KING_SYMBOL:
                return True
        if location[0] <= 1 and location[1] <= 6:
            if board[location[0] - 1][location[1] + 1] == constants.KING_SYMBOL:
                return True
        if location[0] <= 6 and location[1] <= 6:
            if board[location[0] + 1][location[1] + 1] == constants.KING_SYMBOL:
                return True
            
        return False

def isCheckByPawn(location, board, player):
    """
    Helper method to determine if king under attack by pawn.
    """
    if player == constants.WHITE_PLAYER:
        #Checks if white king is under attack by black pawn
        if 1 <= location[0] and location[1] <= 6:
            if board[location[0] - 1][location[1] + 1] == constants.BLACK_PAWN_SYMBOL:
                return True
        if location[0] <= 6 and location[1] <= 6:
            if board[location[0] + 1][location[1] + 1] == constants.BLACK_PAWN_SYMBOL:
                return True

        return False

    else:
        #Checks if black king under attack by white pawn
        if 1 <= location[0] and 1 <= location[1]:
            if board[location[0] - 1][location[1] - 1] == constants.PAWN_SYMBOL:
                return True
        if location[0] <= 6 and 1 <= location[1]:
            if board[location[0] + 1][location[1] - 1] == constants.PAWN_SYMBOL:
                return True

        return False

def isCheckByKnight(location, board, player):
    """
    Helper method to determine if king under attack by knight.
    """
    if player == constants.WHITE_PLAYER:
        #Checks locations where black knight would put white king in check
        if 2 <= location[0] and 2 <= location[1]:
            if board[location[0] - 2][location[1] - 1] == constants.BLACK_KNIGHT_SYMBOL or \
               board[location[0] - 1][location[1] - 2] == constants.BLACK_KNIGHT_SYMBOL:
                return True
            
        if location[0] <= 5 and location[1] <= 5:
            if board[location[0] + 1][location[1] + 2] == constants.BLACK_KNIGHT_SYMBOL or \
               board[location[0] + 2][location[1] + 1] == constants.BLACK_KNIGHT_SYMBOL:
                return True
        
        if 2 <= location[0] and location[1] <= 5:
            if board[location[0] - 2][location[1] + 1] == constants.BLACK_KNIGHT_SYMBOL or \
            board[location[0] - 1][location[1] + 2] == constants.BLACK_KNIGHT_SYMBOL:
                return True

        if location[0] <= 5 and 2 <= location[1]:
            if board[location[0] + 2][location[1] - 1] == constants.BLACK_KNIGHT_SYMBOL or \
            board[location[0] + 1][location[1] - 2] == constants.BLACK_KNIGHT_SYMBOL:
                return True

        return False
        
    else:
        #Checks locations where white knight would put black king in check
        if 2 <= location[0] and 2 <= location[1]:
            if board[location[0] - 2][location[1] - 1] == constants.KNIGHT_SYMBOL or \
               board[location[0] - 1][location[1] - 2] == constants.KNIGHT_SYMBOL:
                return True
            
        if location[0] <= 5 and location[1] <= 5:
            if board[location[0] + 1][location[1] + 2] == constants.KNIGHT_SYMBOL or \
               board[location[0] + 2][location[1] + 1] == constants.KNIGHT_SYMBOL:
                return True
        
        if 2 <= location[0] and location[1] <= 5:
            if board[location[0] - 2][location[1] + 1] == constants.KNIGHT_SYMBOL or \
            board[location[0] - 1][location[1] + 2] == constants.KNIGHT_SYMBOL:
                return True

        if location[0] <= 5 and 2 <= location[1]:
            if board[location[0] + 2][location[1] - 1] == constants.KNIGHT_SYMBOL or \
            board[location[0] + 1][location[1] - 2] == constants.KNIGHT_SYMBOL:
                return True

        return False
        
def checkmateLocation(board):
    return [4,2]


#checks all of the spots on the board for a piece of same color as king
def canPieceMoveToSpot(location,player,spot):
    row=0
    column=0
    while row<8:
        while column<8:
            rowcol=[row,col]
            #if the piece is same color as the king
            if pieceOwner(rowcol)== pieceOwner(location):
                #if the piece can move there, then checkmate returns false
                if isLegalMove(player,spot) == True:
                    return False
                else:
                    validity=True
        column+=1
    row+=1
    return validity

"""
zzz                = [ ['r','p','','','','','*p','*r'],
                        ['n','p','','','','','*p','*n'],
                        ['b','p','','','','','*p',''],
                        ['','p','','','*b','','*p','*q'],
                        ['k','p','q','','*k','','*p',''],
                        ['b','p','','','','','*p','*b'],
                        ['n','p','','','','','*p','*n'],
                        ['r','p','','','','','*p','*r'] ]
isCheckMate(zzz,1)
"""
print "???"
