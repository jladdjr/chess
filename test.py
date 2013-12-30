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

    """
    Board1:

                      +----+----+----+----+----+----+----+----+
                    8 | *r |    | *b |    | *k | *b | *n | *r |
                      +----+----+----+----+----+----+----+----+
                    7 |    | *p | *p | *p |    | *p |    | *p |
                      +----+----+----+----+----+----+----+----+
                    6 | *p |    | *n |    | *p |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    5 |    |    |    |  p |    |    | *p |    |
                      +----+----+----+----+----+----+----+----+
                    4 |    |  p |    |  q |    | *q |  p |    |
                      +----+----+----+----+----+----+----+----+
                    3 |  n |    |    |    |    |  n |    |    |
                      +----+----+----+----+----+----+----+----+
                    2 |  p |    |  p |    |  p |  p |    |  p |
                      +----+----+----+----+----+----+----+----+
                    1 |  r |    |  b |    |  k |  b |    |  r |
                      +----+----+----+----+----+----+----+----+

                         a    b    c    d    e    f    g    h
    """

    board1         = [ ['r','p','n',''  ,''  ,'*p',''  ,'*r'],
                       ['' ,'' ,'' ,'p' ,''  ,''  ,'*p',''  ],
                       ['b','p','' ,''  ,''  ,'*n','*p','*b'],
                       ['' ,'' ,'' ,'q' ,'p' ,''  ,'*p',''  ],
                       ['k','p','' ,''  ,''  ,'*p',''  ,'*k'],
                       ['b','p','n','*q',''  ,''  ,'*p','*b'],
                       ['' ,'' ,'' ,'p' ,'*p',''  ,''  ,'*n'],
                       ['r','p','' ,''  ,''  ,''  ,'*p','*r'] ]



    """
    Board2:

                      +----+----+----+----+----+----+----+----+
                    8 |    | *n |    |    |    |    |    | *r |
                      +----+----+----+----+----+----+----+----+
                    7 | *p |    |    |    | *k |    | *p |    |
                      +----+----+----+----+----+----+----+----+
                    6 |    |    | *b |    |    | *p |    |    |
                      +----+----+----+----+----+----+----+----+
                    5 |    |    |    |    |    |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    4 |    |    |    |  q |    |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    3 |    |  r |    |    |  n |    |    |    |
                      +----+----+----+----+----+----+----+----+
                    2 |    |    |    |  p |    |    |    |  p |
                      +----+----+----+----+----+----+----+----+
                    1 |    |    |  b |    |    |    |    |    |
                      +----+----+----+----+----+----+----+----+

                         a    b    c    d    e    f    g    h
    """

    board2         = [ ['' ,'' ,'' ,''  ,'',''  ,'*p',''  ],
                       ['' ,'' ,'r',''  ,'',''  ,''  ,'*n'],
                       ['b','' ,'' ,''  ,'','*b',''  ,''  ],
                       ['' ,'p','' ,'q' ,'',''  ,''  ,''  ],
                       ['' ,'' ,'n',''  ,'',''  ,'*k',''  ],
                       ['' ,'' ,'' ,''  ,'','*p',''  ,''  ],
                       ['' ,'' ,'' ,''  ,'',''  ,'*p',''  ],
                       ['' ,'p','' ,''  ,'',''  ,''  ,'*r'] ]


    #More boards (no illustrations given)
    board3        =  [ ['r','p','',''  ,'','','*p',''  ],
                       ['n','p','',''  ,'','','*p','*n'],
                       ['b','p','',''  ,'','','*p','*b'],
                       ['q','p','','*r','','','*p','*q'],
                       ['' ,'p','','k' ,'','','*p','*k'],
                       ['b','p','',''  ,'','','*p','*b'],
                       ['n','p','',''  ,'','','*p','*n'],
                       ['r','p','',''  ,'','','*p','*r'] ]


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
        b._isLegalMoveForPawn = MagicMock(return_value=True)
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
        b._isLegalMoveForPawn = MagicMock(return_value=True)
        b.isCheck      = MagicMock(return_value=False)
        b.isCheckMate  = MagicMock(return_value=False)

        self.assertFalse(b._isLegalMoveForPawn.called)
        self.assertFalse(b.isCheck.called)
        self.assertFalse(b.isCheckMate.called)
        self.assertEqual(g._currentPlayer, 1)

        g._nextTurn()

        b._isLegalMoveForPawn.assert_called_with("b1c3")
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
        b._isLegalMoveForKnight = MagicMock(return_value=True)
       
        self.assertEqual(b._board[1][0], "n")
        b.movePiece("b1","c3") 
        self.assertEqual(b._board[1][0], "")
        self.assertEqual(b._board[2][2], "n")
        b._isLegalMoveForKnight.assert_called_with("b1","c3")

    def test_move_piece_black_pawn(self):
        from board import Board
        b = Board()
        b._isLegalMoveForPawn = MagicMock(return_value=True)
       
        self.assertEqual(b._board[4][6], "*p")
        b.movePiece("e7","e6") 
        self.assertEqual(b._board[4][6], "")
        self.assertEqual(b._board[4][5], "*p")
        b._isLegalMoveForPawn.assert_called_with("e7","e6")

    def test_move_piece_queen_overtakes_queen(self):
        from board import Board
        b = Board()
        b._board      = ChessTest.board1
        b._isLegalMoveForQueen = MagicMock(return_value=True)
       
        self.assertEqual(b._board[3][3], "q")
        self.assertEqual(b._board[5][3], "*q")
        b.movePiece("d4","f4") 
        self.assertEqual(b._board[3][3], "")
        self.assertEqual(b._board[5][3], "q")
        b._isLegalMoveForQueen.assert_called_with("d4","f4")
    """

    #Tests for isLegalMove()
    
    """
    def test_is_legal_move(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Pawn - move forward one space
        self.assertTrue(b.isLegalMove("d2","d3"))
        
        #Rook - move forward several spaces
        self.assertTrue(b.isLegalMove("h8","h4"))

        #Rook - move across several spaces
        self.assertTrue(b.isLegalMove("h8","d8"))

        #Knight - move forward and right
        self.assertTrue(b.isLegalMove("e3","f5"))

        #Knight - move left and up
        self.assertTrue(b.isLegalMove("b8","d7"))

        #Bishop - move diagnoally left
        self.assertTrue(b.isLegalMove("c1","a3"))

        #Bishop - move back and right
        self.assertTrue(b.isLegalMove("c6","b7"))

        #Queen - move right one space
        self.assertTrue(b.isLegalMove("d4","e4"))

        #Queen - move left several spaces
        self.assertTrue(b.isLegalMove("d4","b4"))

        #Queen - move left diagonally
        self.assertTrue(b.isLegalMove("d4","b6"))

        #King - move forward
        self.assertTrue(b.isLegalMove("e7","e6"))

        #King - move backward 
        self.assertTrue(b.isLegalMove("e7","e8"))

        #King - move left 
        self.assertTrue(b.isLegalMove("e7","f7"))

        #King - move right 
        self.assertTrue(b.isLegalMove("e7","d7"))

        #King - move right diagonally 
        self.assertTrue(b.isLegalMove("e7","d6"))

    def test_is_legal_move_improper_movement(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Pawn - move forward three
        self.assertFalse(b.isLegalMove("h2","h5"))

        #Pawn - move left
        self.assertFalse(b.isLegalMove("g7","h7"))

        #Pawn - move backwards
        self.assertFalse(b.isLegalMove("d2","d1"))

        #Rook - move diagonally
        self.assertFalse(b.isLegalMove("b3","b4"))

        #Knight - move forward two
        self.assertFalse(b.isLegalMove("e3","e5"))

        #Bishop - move forward one
        self.assertFalse(b.isLegalMove("c1","c2"))

        #Queen - move like knight
        self.assertFalse(b.isLegalMove("d4","b5"))

        #King - move forward two
        self.assertFalse(b.isLegalMove("e7","e5"))

    def test_is_legal_move_moving_into_occupied_space(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #White rook moves into white pawn
        self.assertFalse(b.isLegalMove("a1","a2"))

        #Black king moves into black bishop
        self.assertFalse(b.isLegalMove("e8","f8"))

    def test_is_legal_move_legal_kills(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #White knight kills black pawn
        self.assertTrue(b.isLegalMove("f3","g5"))

        #Black queen kills white bishop
        self.assertTrue(b.isLegalMove("f4","c1"))

        #White bishop kills black pawn
        self.assertTrue(b.isLegalMove("c1","h7"))

    def test_is_legal_move_blocked_move(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Pawn tries to move forward two spaces, is blocked by knight
        self.assertFalse(b.isLegalMove("a2","a4"))

        #Rook tries to move forward, is blocked by pawn
        self.assertFalse(b.isLegalMove("h8","h5"))

        #Rook tries to move across, is blocked by several pieces
        self.assertFalse(b.isLegalMove("h8","d8"))

        #Knight 'jumps' - can't be blocked by any pieces

        #Bishop tries to move left diagonally, is blocked by pawn
        self.assertFalse(b.isLegalMove("f1","c4"))

        #Queen tries to move across, is blocked by other queen
        self.assertFalse(b.isLegalMove("f4","c4"))

        #King can only move one space at a time

    def test_is_legal_move_illegal_kills(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Black pawn moves forward to kill white pawn
        self.assertFalse(b.isLegalMove("g5","g4"))

        #Knight moves forward three spaces to kill black pawn
        self.assertFalse(b.isLegalmove("a3","a6"))
    """

    #Tests for _isLegalMoveForPawn()

    """
    def test_is_legal_move_for_pawn(self):
        from board import Board

        b = Board()
        b._board = ChessTest.board2

        #White pawn, forward one space from default position
        self.assertTrue(b._isLegalMoveForPawn("h2", "h3"))
        
        #White pawn, forward two spaces from default position
        self.assertTrue(b._isLegalMoveForPawn("h2", "h4"))

        #Black pawn, forward one space from default position
        self.assertTrue(b._isLegalMoveForPawn("g7", "g6"))
        
        #Black pawn, forward two spaces from default position
        self.assertTrue(b._isLegalMoveForPawn("g7", "g5"))

        #Black pawn, forward one space from non-default position
        self.assertTrue(b._isLegalMoveForPawn("f6", "f5"))

        b._board = ChessTest.board1
    
        #Legal move to kill
        self.assertTrue(b._isLegalMoveForPawn("d5", "e6"))

        #Legal move to kill 2
        self.assertTrue(b._isLegalMoveForPawn("d5", "c6"))

    def test_is_legal_move_for_pawn_negative_test(self):
        from board import Board

        b = Board()
        b._board = ChessTest.board2

        #White pawn, forward three spaces from default position
        self.assertFalse(b._isLegalMoveForPawn("h2", "h5"))
        
        #White pawn, backward one space 
        self.assertFalse(b._isLegalMoveForPawn("h2", "h1"))

        #Black pawn, move to left 
        self.assertFalse(b._isLegalMoveForPawn("f6", "g6"))
        
        #Black pawn, move to right 
        self.assertFalse(b._isLegalMoveForPawn("f6", "e6"))
        
        #Black pawn, forward diagonally
        self.assertFalse(b._isLegalMoveForPawn("f6", "e5"))

        #Black pawn, forward diagonally
        self.assertFalse(b._isLegalMoveForPawn("f6", "g5"))

        #White pawn, backward diagonally
        self.assertFalse(b._isLegalMoveForPawn("h2", "g1"))

        #White pawn, backward diagonally
        self.assertFalse(b._isLegalMoveForPawn("d2", "e1"))

        #White pawn, far across board 
        self.assertFalse(b._isLegalMoveForPawn("d2", "f8"))

        #Cannot kill your own piece 
        self.assertFalse(b._isLegalMoveForPawn("d2", "e3"))

        b._board = ChessTest.board1

        #Cannot kill piece by moving forward (must move diagnoally)
        self.assertFalse(b._isLegalMoveForPawn("g4", "g5"))
        
    """

    # Tests for isLegalMoveForRook()

    """
    def test_is_legal_move_for_rook(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Left
        self.assertTrue(b._isLegalMoveForRook("b3","a3"))
        
        #Right
        self.assertTrue(b._isLegalMoveForRook("b3","d3"))

        #Up
        self.assertTrue(b._isLegalMoveForRook("b3","b7"))

        #Down
        self.assertTrue(b._isLegalMoveForRook("h8","h4"))

        #Legal kill
        self.assertTrue(b._isLegalMoveForRook("b3","b8"))

    def test_is_legal_move_for_rook_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Diagnoal
        self.assertFalse(b._isLegalMoveForRook("b3","a4"))

        #Move to occupied space
        self.assertFalse(b._isLegalMoveForRook("b3","e3"))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForRook("h8","a8"))

        #Path blocked by enemy piece
        self.assertFalse(b._isLegalMoveForRook("h8","h1"))
    """

    # Tests for isLegalMoveForKnight()
    
    """
    def test_is_legal_move_for_knight(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Forward and right
        self.assertTrue(b._isLegalMoveForKnight("e3","f5"))
        
        #Forward and left
        self.assertTrue(b._isLegalMoveForKnight("e3","d5"))

        #Right and up
        self.assertTrue(b._isLegalMoveForKnight("e3","g4"))

        #Left and down
        self.assertTrue(b._isLegalMoveForKnight("e3","c2"))

        b._board = ChessTest.board1

        #Legal kill
        self.assertTrue(b._isLegalMoveForKnight("f3","g5"))

    def test_is_legal_move_for_knight_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left two
        self.assertFalse(b._isLegalMoveForKnight("f3","d3"))

        #Move to occupied space
        self.assertFalse(b._isLegalMoveForKnight("f3","e1"))
    """

    # Tests for isLegalMoveForBishop()

    """
    def test_is_legal_move_for_bishop(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Move up and to the left
        self.assertTrue(b._isLegalMoveForBishop("c1","a3"))
        
        #Move down and to the right
        self.assertTrue(b._isLegalMoveForBishop("c6","e8"))

        b._board = ChessTest.board1

        #Legal kill
        self.assertTrue(b._isLegalMoveForBishop("f8","b4"))

    def test_is_legal_move_for_bishop_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertFalse(b._isLegalMoveForBishop("c8","b8"))

        #Move to occupied space
        self.assertFalse(b._isLegalMoveForBishop("c8","b7"))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForBishop("f1","d3"))

        #Path blocked by enemy piece
        #(Even though this would otherwise be a legitimate kill)
        self.assertFalse(b._isLegalMoveForBishop("f8","a3"))
    """

    # Tests for isLegalMoveForQueen()
    
    """
    def test_is_legal_move_for_queen(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertTrue(b._isLegalMoveForQueen("f4","e4"))

        #Move right
        self.assertTrue(b._isLegalMoveForQueen("d4","e4"))

        #Move up and left
        self.assertTrue(b._isLegalMoveForQueen("d4","a7"))

        #Move down and right
        self.assertTrue(b._isLegalMoveForQueen("f4","g3"))

        #Legal kill
        self.assertTrue(b._isLegalMoveForQueen("f4","h2"))

        #Legal kill2
        self.assertTrue(b._isLegalMoveForQueen("d4","f4"))

        #Legal kill3
        self.assertTrue(b._isLegalMoveForQueen("f4","c1"))

    def test_is_legal_move_for_queen_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move like horse
        self.assertFalse(b._isLegalMoveForQueen("d4","f5"))

        #Move to occupied space
        self.assertFalse(b._isLegalMoveForQueen("f4","g5"))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForQueen("f4","g6"))

        #Path blocked by enemy piece
        #(Even though this would otherwise be a legitimate kill)
        self.assertFalse(b._isLegalMoveForQueen("f4","b4"))
    """

    # Tests for isLegalMoveForKing()

    """
    def test_is_legal_move_for_king(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertTrue(b._isLegalMoveForKing("e8","d8"))

        #Move up and left 
        self.assertTrue(b._isLegalMoveForKing("e1","d2"))

        #Move down 
        self.assertTrue(b._isLegalMoveForKing("e8","e7"))

        b._board = ChessTest.board3

        #Legal kill
        self.assertTrue(b._isLegalMoveForKing("e4","d4"))

    def test_is_legal_move_for_king_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move diagnoally two spaces
        self.assertFalse(b._isLegalMoveForKing("e1","c3"))

        #Move to occupied space
        self.assertFalse(b._isLegalMoveForKing("e8","f8"))
    """

    #################################
    # Tests for BoardAnalyzer class #
    #################################

    #Coming soon..         

if __name__ == '__main__':
    unittest.main(buffer=True)      #User buffer option to supress output
                                    #from program
