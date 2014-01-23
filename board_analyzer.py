#!/usr/bin/python

import constants
from copy import deepcopy

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

def isCheckMate(board, boardObject, player):
    """
    Determines if game has ended.

    @param board:   A list of lists representing the board state.
    @param player:  Player (e.g. constants.WHITE_PLAYER)
    @return True if game has ended, False otherwise.
    """
    location = kingLocator(board, player)
    acceptable = [0, 1, 2, 3, 4, 5, 6, 7]

    #Tests if king is in check
    if isCheckStatic(board, player) == False:
        return False

    #Tests if king can move/attack out of check
    escapeRoutes = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for route in escapeRoutes:
        route[0] = route[0] + location[0]
        route[1] = route[1] + location[1]
        testMove = location + route
        if testMove[0] not in acceptable or testMove[1] not in acceptable:
            continue
        if boardObject.isLegalMove(player, testMove) == True:
            if isCheck(board, player, testMove) == False:
                return False

    #Tests if king can get blocked out of check - for NE/SW diagonal
    if isCheckByDiagonal(location, board, player) == True:
        for space in range(-len(board), len(board)):
            for horizontalSpace in range(len(board)):
                for verticalSpace in range(len(board)):
                    if location[0] + space not in acceptable or \
                       location[1] + space not in acceptable:
                        continue
                    move = [horizontalSpace, verticalSpace, location[0] + space, location[1] + space]
                    if boardObject.isLegalMove(player, move) == True:
                        if isCheck(board, player, move) == False:
                            return False
                   
    #Tests if king can get blocked out of check - for NW/SE diagonal
    if isCheckByDiagonal(location, board, player) == True:
        for space in range(-len(board), len(board)):
            for horizontalSpace in range(len(board)):
                for verticalSpace in range(len(board)):
                    if location[0] + space not in acceptable or \
                       location[1] + space not in acceptable:
                        continue
                    move = [horizontalSpace, verticalSpace, location[0] - space, location[1] + space]
                    if boardObject.isLegalMove(player, move) == True:
                        if isCheck(board, player, move) == False:
                            return False
    
    #Tests if king can get blocked out of check - for horizontal check
    if isCheckByHorizontal(location, board, player) == True:
        for space in range(len(board)):
            for horizontalSpace in range(len(board)):
                for verticalSpace in range(len(board)):
                    move = [horizontalSpace, verticalSpace, space, location[1]]
                    if boardObject.isLegalMove(player, move) == True:
                        print move
                        if isCheck(board, player, move) == False:
                            return False
                    
    #Tests if king can get blocked out of check - for vertical check
    if isCheckByVertical(location, board, player) == True:
        for space in range(len(board)):
            for horizontalSpace in range(len(board)):
                for verticalSpace in range(len(board)):
                    move = [horizontalSpace, verticalSpace, location[0], space]
                    if boardObject.isLegalMove(player, move) == True:
                        if isCheck(board, player, move) == False:
                            print move
                            return False
    
    return True

def isCheck(board, player, move):
    """
    Determines if king is in check after move.

    @param board:   A list of lists representing the board state.
    @param player:  Player (e.g. constants.WHITE_PLAYER)
    @return True if king is in check, False otherwise.
    """
    testBoard = deepcopy(board)
    testPiece = board[move[0]][move[1]]
    testBoard[move[2]][move[3]] = testPiece
    testBoard[move[0]][move[1]] = constants.EMPTY_SYMBOL

    location = kingLocator(testBoard, player)
    
    if isCheckByDiagonal(location, testBoard, player) == True:
        return True
    if isCheckByHorizontal(location, testBoard, player) == True:
        return True
    if isCheckByVertical(location, testBoard, player) == True:
        return True
    if isCheckByKing(location, testBoard, player) == True:
        return True
    if isCheckByPawn(location, testBoard, player) == True:
        return True
    if isCheckByKnight(location, testBoard, player) == True:
        return True

    return False

def isCheckStatic(board, player):
    """
    Determines if king is in check.
    
    @param board:   A list of lists representing the board state.
    @param player:  Player (e.g. constants.WHITE_PLAYER)
    @return True if king is in check, False otherwise.
    """
    location = kingLocator(board, player)
    
    if isCheckByDiagonal(location, board, player) == True:
        return True
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
    acceptable = [0, 1, 2, 3, 4, 5, 6, 7]

    if player == constants.WHITE_PLAYER:
        #Testing for check from NE diagonal
        space = 1
        while location[0] + space in acceptable and location[1] + space in acceptable:
            if board[location[0] + space][location[1] + space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] + space][location[1] + space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] + space][location[1] + space] == constants.BLACK_QUEEN_SYMBOL:
               return True
            else:
               break
                
        #Testing for check from NW diagonal
        space = 1
        while location[0] - space in acceptable and location[1] + space in acceptable:
            if board[location[0] - space][location[1] + space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] - space][location[1] + space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] - space][location[1] + space] == constants.BLACK_QUEEN_SYMBOL:
               return True
            else:
               break
        
        #Testing for check from SE diagonal        
        space = 1
        while location[0] + space in acceptable and location[1] - space in acceptable:
            if board[location[0] + space][location[1] - space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] + space][location[1] - space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] + space][location[1] - space] == constants.BLACK_QUEEN_SYMBOL:
               return True
            else:
               break
         
        #Testing for check from SW diagonal        
        space = 1
        while location[0] - space in acceptable and location[1] - space in acceptable:
            if board[location[0] - space][location[1] - space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] - space][location[1] - space] == constants.BLACK_BISHOP_SYMBOL or \
               board[location[0] - space][location[1] - space] == constants.BLACK_QUEEN_SYMBOL:
               return True
            else:
               break
         
        return False
         
    else:
        #Testing for check from NE diagonal
        space = 1
        while location[0] + space in acceptable and location[1] + space in acceptable:
            if board[location[0] + space][location[1] + space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] + space][location[1] + space] == constants.BISHOP_SYMBOL or \
               board[location[0] + space][location[1] + space] == constants.QUEEN_SYMBOL:
               return True
            else:
               break
                
        #Testing for check from NW diagonal
        space = 1
        while location[0] - space in acceptable and location[1] + space in acceptable:
            if board[location[0] - space][location[1] + space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] - space][location[1] + space] == constants.BISHOP_SYMBOL or \
               board[location[0] - space][location[1] + space] == constants.QUEEN_SYMBOL:
               return True
            else:
               break
        
        #Testing for check from SE diagonal        
        space = 1
        while location[0] + space in acceptable and location[1] - space in acceptable:
            if board[location[0] + space][location[1] - space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] + space][location[1] - space] == constants.BISHOP_SYMBOL or \
               board[location[0] + space][location[1] - space] == constants.QUEEN_SYMBOL:
               return True
            else:
               break
         
        #Testing for check from SW diagonal        
        space = 1
        while location[0] - space in acceptable and location[1] - space in acceptable:
            if board[location[0] - space][location[1] - space] == constants.EMPTY_SYMBOL:
                space += 1
                continue
            if board[location[0] - space][location[1] - space] == constants.BISHOP_SYMBOL or \
               board[location[0] - space][location[1] - space] == constants.QUEEN_SYMBOL:
               return True
            else:
               break
         
        return False

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
