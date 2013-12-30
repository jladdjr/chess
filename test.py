#!/usr/bin/python

import unittest
from mock import MagicMock

class ChessTest(unittest.TestCase):
    """
    Unit tests for chess.
    """

    STARTING_BOARD = [ ['r','p','','','','','*p','*r'],
                       ['n','p','','','','','*p','*n'],
                       ['b','p','','','','','*p','*b'],
                       ['q','p','','','','','*p','*q'],
                       ['k','p','','','','','*p','*k'],
                       ['b','p','','','','','*p','*b'],
                       ['n','p','','','','','*p','*n'],
                       ['r','p','','','','','*p','*r'] ]

    board1         = [ ['r','p','n',''  ,''  ,'*p',''  ,'*r'],
                       ['' ,'' ,'' ,'p' ,''  ,''  ,'*p',''  ],
                       ['b','p','' ,''  ,''  ,'*n','*p','*b'],
                       ['' ,'' ,'' ,'q' ,'p' ,''  ,'*p',''  ],
                       ['k','p','' ,''  ,''  ,'*p',''  ,'*k'],
                       ['b','p','n','*q',''  ,''  ,'*p','*b'],
                       ['' ,'' ,'' ,'p' ,'*p',''  ,''  ,'*n'],
                       ['r','p','' ,''  ,''  ,''  ,'*p','*r'] ]

    def setUp(self):
        """
        Setup test fixture.
        """
        pass

    def tearDown(self):
        """
        Tear down test fixture.
        """
        pass

    ########################
    # Tests for Game class #
    ########################

    def test_game_initialization(self):
        from game import Game

        g = Game()
        self.assertEqual(g._currentPlayer, 1)

    #Tests for _nextTurn()

    """
    def test_next_turn_switching_players(self):
        from game import Game

        #Get game
        g = Game()
        g._getPlayersNextMove = MagicMock(return_value="b1c3")
       
        #Mock-up board functions
        b = g._board
        b._isLegalMove = MagicMock(return_value=True)
        b.isCheck      = MagicMock(return_value=False)
        b.isCheckMate  = MagicMock(return_value=False)

        self.assertEqual(g._currentPlayer, 1)
        g._nextTurn()
        self.assertEqual(g._currentPlayer, 2)

    def test_next_turn_process(self):
        from game import Game

        #Get game
        g = Game()
        g._getPlayersNextMove = MagicMock(return_value="b1c3")
       
        #Mock-up board functions
        b = g._board
        b._isLegalMove = MagicMock(return_value=True)
        b.isCheck      = MagicMock(return_value=False)
        b.isCheckMate  = MagicMock(return_value=False)

        self.assertFalse(b._isLegalMove.called)
        self.assertFalse(b.isCheck.called)
        self.assertFalse(b.isCheckMate.called)
        self.assertEqual(g._currentPlayer, 1)

        g._nextTurn()

        b._isLegalMove.assert_called_with("b1c3")
        self.assertTrue(b.isCheck.called)
        self.assertTrue(b.isCheckMate.called)
        self.assertEqual(g._currentPlayer, 2)
    """

    #########################
    # Tests for Board class #
    #########################

    def test_board_initialization(self):
        from board import Board
        b = Board()

        self.assertEqual(b._board, ChessTest.STARTING_BOARD)

    #Test for getBoard()

    def test_get_board(self):
        from board import Board 

        b = Board()
        self.assertEqual(b.getBoard(), ChessTest.STARTING_BOARD)

    #Tests for movePiece()
    """
    def test_move_piece_white_knight(self):
        from board import Board
        b = Board()
        b.isLegalMove           = MagicMock(return_value=True)
       
        self.assertEqual(b._board[1][0], "n")
        b.movePiece("b1","c3") 
        self.assertEqual(b._board[1][0], "")
        self.assertEqual(b._board[2][2], "n")
        b.isLegalMove.assert_called_with("b1","c3")

    def test_move_piece_black_pawn(self):
        from board import Board
        b = Board()
        b.isLegalMove           = MagicMock(return_value=True)
       
        self.assertEqual(b._board[4][6], "*p")
        b.movePiece("e7","e6") 
        self.assertEqual(b._board[4][6], "")
        self.assertEqual(b._board[4][5], "*p")
        b.isLegalMove.assert_called_with("e7","e6")

    def test_move_piece_queen_overtakes_queen(self):
        from board import Board
        b = Board()
        b._board      = ChessTest.board1
        b.isLegalMove = MagicMock(return_value=True)
       
        self.assertEqual(b._board[3][3], "q")
        self.assertEqual(b._board[5][3], "*q")
        b.movePiece("d4","f4") 
        self.assertEqual(b._board[3][3], "")
        self.assertEqual(b._board[5][3], "q")
        b.isLegalMove.assert_called_with("d4","f4")
    """

    #################################
    # Tests for BoardAnalyzer class #
    #################################

    #Coming soon..         

if __name__ == '__main__':
    unittest.main(buffer=True)      #User buffer option to supress output
                                    #from program
