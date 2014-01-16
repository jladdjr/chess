#!/usr/bin/python

import constants

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
    #(Replace this with a real test)
    return False

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

def isCheckByHorizontal(location, board, player):
    """
    Helper method to determine if king under attack by rook or queen horizontally.
    """
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
                        """
    pass
                    
def isCheckByVertical(location, board, player):
    """
    Helper method to determine if king under attack by rook or queen vertically
    """
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
                        """
    pass
                    
def isCheckByKing(location, board, player):
    """
    Helper method to determine if king under attack by knight.
    """
    """
    if player == constants.WHITE_PLAYER:
        #Checks locations where black kings could attack white king
        if board[location[0] + 1][location[1] + 1] == constants.BLACK_KING_SYMBOL or \
        board[location[0] - 1][location[1] - 1] == constants.BLACK_KING_SYMBOL or \
        board[location[0] + 1][location[1] - 1] == constants.BLACK_KING_SYMBOL or \
        board[location[0] - 1][location[1] + 1] == constants.BLACK_KING_SYMBOL or \
        board[location[0] + 1][location[1]] == constants.BLACK_KING_SYMBOL or \
        board[location[0]][location[1] + 1] == constants.BLACK_KING_SYMBOL or \
        board[location[0] - 1][location[1]] == constants.BLACK_KING_SYMBOL or \
        board[location[0]][location[1] - 1] == constants.BLACK_KING_SYMBOL:
            return True
        
    if player == constants.BLACK_PLAYER:
        #Checks locations where white kings could attack black king
        if board[location[0] + 1][location[1] + 1] == constants.KING_SYMBOL or \
        board[location[0] - 1][location[1] - 1] == constants.KING_SYMBOL or \
        board[location[0] + 1][location[1] - 1] == constants.KING_SYMBOL or \
        board[location[0] - 1][location[1] + 1] == constants.KING_SYMBOL or \
        board[location[0] + 1][location[1]] == constants.KING_SYMBOL or \
        board[location[0]][location[1] + 1] == constants.KING_SYMBOL or \
        board[location[0] - 1][location[1]] == constants.KING_SYMBOL or \
        board[location[0]][location[1] - 1] == constants.KING_SYMBOL:
            return True
            """
    pass

def isCheckByPawn(location, board, player):
    """
    Helper method to determine if king under attack by pawn.
    """
    if player == constants.WHITE_PLAYER:
        #Checks if white king is under attack by black pawn
        if 1 <= location[0] and location[1] <= 6:
            if board[location[0] - 1][location[1] + 1] == constants.BLACK_PAWN_SYMBOL:
                return True
            else:
                return False
        if location[0] <= 6 and location[1] <= 6:
            if board[location[0] + 1][location[1] + 1] == constants.BLACK_PAWN_SYMBOL:
                return True
            else:
                return False

    else:
        #Checks if black king under attack by white pawn
        if 1 <= location[0] and 1 <= location[1]:
            if board[location[0] - 1][location[1] - 1] == constants.PAWN_SYMBOL:
                return True
            else:
                return False
        if location[0] <= 6 and 1 <= location[1]:
            if board[location[0] + 1][location[1] - 1] == constants.PAWN_SYMBOL:
                return True
            else:
                return False

def isCheckByKnight(location, board, player):
    """
    Helper method to determine if king under attack by knight.
    """
    """
    if player == constants.WHITE_PLAYER:
        #Checks locations where black knight would put white king in check
        if board[location[0] + 2][location[1] + 1] == constants.BLACK_KNIGHT or \
        board[location[0] + 1][location[1] + 2] == constants.BLACK_KNIGHT or \
        board[location[0] - 2][location[1] - 1] == constants.BLACK_KNIGHT or \
        board[location[0] - 1][location[1] - 2] == constants.BLACK_KNIGHT or \
        board[location[0] + 2][location[1] - 1] == constants.BLACK_KNIGHT or \
        board[location[0] + 1][location[1] - 2] == constants.BLACK_KNIGHT or \
        board[location[0] - 2][location[1] + 1] == constants.BLACK_KNIGHT or \
        board[location[0] - 1][location[1] + 2] == constants.BLACK_KNIGHT:
            return True
        
    else:
        #Checks locations where white knight would put black king in check
        if board[location[0] + 2][location[1] + 1] == constants.KNIGHT or \
        board[location[0] + 1][location[1] + 2] == constants.KNIGHT or \
        board[location[0] - 2][location[1] - 1] == constants.KNIGHT or \
        board[location[0] - 1][location[1] - 2] == constants.KNIGHT or \
        board[location[0] + 2][location[1] - 1] == constants.KNIGHT or \
        board[location[0] + 1][location[1] - 2] == constants.KNIGHT or \
        board[location[0] - 2][location[1] + 1] == constants.KNIGHT or \
        board[location[0] - 1][location[1] + 2] == constants.KNIGHT:
            return True
            """
    pass

                    

        
