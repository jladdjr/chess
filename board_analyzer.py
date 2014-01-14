#!/usr/bin/python

import constants

def kingLocator(board, player):
    """
    Determines the location of the king of the opposite player

    @return:     returns list indicies of opposing player's king
                 (e.g. [0, 4])
    """
    if player == constants.WHITE_PLAYER:
        piece = constants.BLACK_PLAYER_SYMBOL + constants.KING_SYMBOL
    else:
        piece = constants.KING_SYMBOL
        
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

        
        
