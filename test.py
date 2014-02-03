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
                    1 |  k |    |  b |    |    |    |    |    |
                      +----+----+----+----+----+----+----+----+

                         a    b    c    d    e    f    g    h
    """

    board2         = [ ['k','' ,'' ,''  ,'',''  ,'*p',''  ],
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

    check1         = [ ['r','p','*r',''  ,''  ,''  ,'*p',''  ],
                       ['n','' ,''  ,''  ,''  ,''  ,'*p','*n'],
                       ['b','p',''  ,''  ,''  ,'*q','*p','*b'],
                       ['q','' ,''  ,'p' ,''  ,''  ,'*p',''  ],
                       ['' ,'' ,'p' ,'k' ,''  ,''  ,'*p','*k'],
                       ['b','p',''  ,''  ,''  ,''  ,'*p','*b'],
                       ['n','p',''  ,''  ,''  ,''  ,'*p','*n'],
                       ['r','p','*r',''  ,''  ,''  ,''  ,''  ] ]

    check2         = [ ['' ,'p',''  ,''  ,''  ,''  ,'*p',''  ],
                       ['n','' ,''  ,''  ,''  ,''  ,'*p','*n'],
                       ['b','p',''  ,''  ,''  ,''  ,'*p','*b'],
                       ['q','p','r' ,''  ,''  ,''  ,'*p','*q'],
                       ['k','p','r' ,''  ,'*k',''  ,'*p',''  ],
                       ['b','' ,''  ,'p' ,''  ,''  ,'*p','*b'],
                       ['n','p',''  ,''  ,''  ,''  ,'*p','*n'],
                       ['' ,'p',''  ,''  ,''  ,''  ,''  ,''  ] ]

    checkmate1     = [ ['r','p','*r',''  ,''  ,''  ,'*p',''  ],
                       ['n','' ,''  ,''  ,''  ,'*b','*p','*n'],
                       ['b','p',''  ,''  ,''  ,'*q','*p',''  ],
                       ['q','p' ,'' ,'k' ,''  ,''  ,'*p',''  ],
                       ['' ,'p',''  ,''  ,''  ,''  ,'*p','*k'],
                       ['b','p',''  ,''  ,''  ,''  ,'*p','*b'],
                       ['n','p',''  ,''  ,''  ,''  ,'*p','*n'],
                       ['r','p',''  ,''  ,'*r',''  ,''  ,''  ] ]

    checkmate2     = [ ['k','' ,'' ,'' ,''  ,''  ,'b' ,''],
                       ['' ,'' ,'' ,'' ,''  ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,'q' ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,''  ,'*k',''  ,''],
                       ['' ,'' ,'' ,'' ,'p' ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,''  ,''  ,''  ,''],
                       ['' ,'' ,'' ,'' ,''  ,''  ,'r' ,''],
                       ['' ,'' ,'' ,'' ,''  ,'r' ,''  ,''] ]

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
        import constants

        g = Game()
        self.assertEqual(g._currentPlayer, constants.WHITE_PLAYER)
    
    #Tests for _nextTurn()

    def test_next_turn_switching_players(self):
        from game import Game
        import constants

        #Get game
        g = Game()
        g._getPlayersNextMove = MagicMock(return_value="b1c3")
       
        #Mock-up board functions
        b = g._board
        b._isLegalMove = MagicMock(return_value=True)
        b.isCheck      = MagicMock(return_value=False)
        b.isCheckMate  = MagicMock(return_value=False)

        self.assertEqual(g._currentPlayer, constants.WHITE_PLAYER)
        g._nextTurn()
        self.assertEqual(g._currentPlayer, constants.BLACK_PLAYER)
    
    def test_next_turn_process(self):
        from game import Game
        import constants

        #Get game
        g = Game()
        g._getPlayersNextMove = MagicMock(return_value="b1c3")

        #Mock-up board functions
        b = g._board
        b.isLegalMove = MagicMock(return_value=True)

        self.assertFalse(b.isLegalMove.called)
        self.assertEqual(g._currentPlayer, constants.WHITE_PLAYER)

        g._nextTurn()

        b.isLegalMove.assert_called_with(constants.WHITE_PLAYER, [1, 0, 2, 2])
        self.assertEqual(g._currentPlayer, constants.BLACK_PLAYER)

    
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

    def test_move_piece_white_knight(self):
        from board import Board
        import constants
        b = Board()
       
        self.assertEqual(b._board[1][0], "n")
        b.movePiece(constants.WHITE_PLAYER, [1, 0, 2, 2])
        self.assertEqual(b._board[1][0], "")
        self.assertEqual(b._board[2][2], "n")
    
    def test_move_piece_black_pawn(self):
        from board import Board
        import constants
        b = Board()
       
        self.assertEqual(b._board[4][6], "*p")
        b.movePiece(constants.WHITE_PLAYER, [4, 6, 4, 5]) 
        self.assertEqual(b._board[4][6], "")
        self.assertEqual(b._board[4][5], "*p")
    
    def test_move_piece_queen_overtakes_queen(self):
        from board import Board
        import constants
        b = Board()
        b._board      = ChessTest.board1
       
        self.assertEqual(b._board[3][3], "q")
        self.assertEqual(b._board[5][3], "*q")
        b.movePiece(constants.WHITE_PLAYER, [3, 3, 5, 3]) 
        self.assertEqual(b._board[3][3], "")
        self.assertEqual(b._board[5][3], "q")
    """
    
    #Tests for isLegalMove()
    
    """
    def test_is_legal_move(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board2

        #Pawn - move forward one space
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER, [3, 1, 3, 2]))
        
        #Rook - move forward several spaces
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [7, 7, 7, 3]))

        #Rook - move across several spaces
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [7, 7, 3, 7]))

        #Knight - move forward and right
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER, [4, 2, 5, 4]))

        #Knight - move left and up
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [1, 7, 3, 6]))

        #Bishop - move diagnoally left
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER, [2, 0, 0, 2]))

        #Bishop - move back and right
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [2, 5, 1, 6]))

        #Queen - move right one space
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER, [3, 3, 4, 3]))

        #Queen - move left several spaces
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER, [3, 3, 2, 3]))

        #Queen - move left diagonally
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER, [3, 3, 1, 5]))

        #King - move forward
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [4, 6, 4, 5]))

        #King - move backward 
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [4, 6, 4, 7]))

        #King - move left 
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [4, 6, 5, 6]))

        #King - move right 
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [4, 6, 5, 6]))

        #King - move right diagonally 
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER, [4, 6, 5, 7]))
    
    def test_is_legal_move_improper_movement(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board2

        #Pawn - move forward three
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [7, 1, 7, 4]))

        #Pawn - move left
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [6, 6, 7, 6]))

        #Pawn - move backwards
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [3, 1, 3, 0]))

        #Rook - move diagonally
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [1, 2, 2, 3]))

        #Knight - move forward two
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [4, 2, 4, 4]))

        #Bishop - move forward one
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [2, 0, 2, 1]))

        #Queen - move like knight
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [3, 3, 1, 4]))

        #King - move forward two
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [4, 6, 4, 4]))
    
    def test_is_legal_move_piece_not_moved(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board2

        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [2, 0, 2, 0]))
    
    def test_is_legal_move_moving_into_occupied_space(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #White rook moves into white pawn
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [0, 0, 0, 1]))

        #Black king moves into black bishop
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [4, 7, 5, 7]))
    
    def test_is_legal_move_legal_kills(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #White knight kills black pawn
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER,[5, 2, 6, 4]))

        #Black queen kills white bishop
        self.assertTrue(b.isLegalMove(constants.BLACK_PLAYER,[5, 3, 2, 0]))

        #White bishop kills black queen
        self.assertTrue(b.isLegalMove(constants.WHITE_PLAYER,[2, 0, 5, 3]))
    
    def test_is_legal_move_blocked_move(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #Pawn tries to move forward two spaces, is blocked by knight
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [0, 1, 0, 3]))

        #Rook tries to move forward, is blocked by pawn
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [7, 7, 7, 4]))

        #Rook tries to move across, is blocked by several pieces
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [7, 7, 3, 7]))

        #Knight 'jumps' - can't be blocked by any pieces

        #Bishop tries to move left diagonally, is blocked by pawn
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [5, 0, 2, 3]))

        #Queen tries to move across, is blocked by other queen
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [5, 3, 2, 3]))

        #King can only move one space at a time

    def test_is_legal_move_illegal_kills(self):
        from board import Board
        import constants
        b = Board()
        b._board = ChessTest.board1

        #Black pawn moves forward to kill white pawn
        self.assertFalse(b.isLegalMove(constants.BLACK_PLAYER, [6, 4, 6, 3]))

        #Knight moves forward three spaces to kill black pawn
        self.assertFalse(b.isLegalMove(constants.WHITE_PLAYER, [0, 2, 0, 5]))
    """
    
    #Tests for _isLegalMoveForPawn()

    """
    def test_is_legal_move_for_pawn(self):
        from board import Board
        import constants

        b = Board()
        b._board = ChessTest.board2

        #White pawn, forward one space from default position
        self.assertTrue(b._isLegalMoveForPawn([7, 1, 7, 2], constants.WHITE_PLAYER))
        
        #White pawn, forward two spaces from default position
        self.assertTrue(b._isLegalMoveForPawn([7, 1, 7, 3], constants.WHITE_PLAYER))

        #Black pawn, forward one space from default position
        self.assertTrue(b._isLegalMoveForPawn([6, 6, 6, 5], constants.BLACK_PLAYER))
        
        #Black pawn, forward two spaces from default position
        self.assertTrue(b._isLegalMoveForPawn([6, 6, 6, 4], constants.BLACK_PLAYER))

        #Black pawn, forward one space from non-default position
        self.assertTrue(b._isLegalMoveForPawn([5, 5, 5, 4], constants.BLACK_PLAYER))

        b._board = ChessTest.board1
    
        #Legal move to kill
        self.assertTrue(b._isLegalMoveForPawn([3, 4, 4, 5], constants.WHITE_PLAYER))

        #Legal move to kill 2
        self.assertTrue(b._isLegalMoveForPawn([3, 4, 2, 5], constants.WHITE_PLAYER))
    
    def test_is_legal_move_for_pawn_negative_test(self):
        from board import Board
        import constants

        b = Board()
        b._board = ChessTest.board2

        #White pawn, forward three spaces from default position
        self.assertFalse(b._isLegalMoveForPawn([7, 1, 7, 4], constants.WHITE_PLAYER))
        
        #White pawn, backward one space 
        self.assertFalse(b._isLegalMoveForPawn([7, 1, 7, 0], constants.WHITE_PLAYER))

        #Black pawn, move to left 
        self.assertFalse(b._isLegalMoveForPawn([6, 5, 6, 5], constants.WHITE_PLAYER))
        
        #Black pawn, move to right 
        self.assertFalse(b._isLegalMoveForPawn([6, 5, 6, 5], constants.WHITE_PLAYER))
        
        #Black pawn, forward diagonally
        self.assertFalse(b._isLegalMoveForPawn([5, 5, 4, 4], constants.WHITE_PLAYER))

        #Black pawn, forward diagonally
        self.assertFalse(b._isLegalMoveForPawn([5, 5, 5, 4], constants.WHITE_PLAYER))

        #White pawn, backward diagonally
        self.assertFalse(b._isLegalMoveForPawn([5, 1, 6, 0], constants.WHITE_PLAYER))

        #White pawn, backward diagonally
        self.assertFalse(b._isLegalMoveForPawn([3, 1, 4, 0], constants.WHITE_PLAYER))

        #White pawn, far across board 
        self.assertFalse(b._isLegalMoveForPawn([3, 1, 5, 7], constants.WHITE_PLAYER))

        b._board = ChessTest.board1

        #Cannot kill piece by moving forward (must move diagnoally)
        self.assertFalse(b._isLegalMoveForPawn([6, 3, 6, 4], constants.WHITE_PLAYER))
        
    """
    
    # Tests for isLegalMoveForRook()

    """
    def test_is_legal_move_for_rook(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Left
        self.assertTrue(b._isLegalMoveForRook([1, 2, 0, 2]))
        
        #Right
        self.assertTrue(b._isLegalMoveForRook([1, 2, 3, 2]))

        #Up
        self.assertTrue(b._isLegalMoveForRook([1, 2, 1, 6]))

        #Down
        self.assertTrue(b._isLegalMoveForRook([7, 7, 7, 3]))

        #Legal kill
        self.assertTrue(b._isLegalMoveForRook([1, 2, 1, 7]))
    
    def test_is_legal_move_for_rook_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Diagnoal
        self.assertFalse(b._isLegalMoveForRook([1, 2, 0, 3]))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForRook([7, 7, 0, 7]))

        #Path blocked by enemy piece
        self.assertFalse(b._isLegalMoveForRook([7, 7, 7, 0]))
    """
    
    # Tests for isLegalMoveForKnight()
    
    """
    def test_is_legal_move_for_knight(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Forward and right
        self.assertTrue(b._isLegalMoveForKnight([4, 2, 5, 4]))
        
        #Forward and left
        self.assertTrue(b._isLegalMoveForKnight([4, 2, 3, 4]))

        #Right and up
        self.assertTrue(b._isLegalMoveForKnight([4, 2, 6, 3]))

        #Left and down
        self.assertTrue(b._isLegalMoveForKnight([4, 2, 2, 1]))

        b._board = ChessTest.board1

        #Legal kill
        self.assertTrue(b._isLegalMoveForKnight([5, 2, 6, 4]))
    
    def test_is_legal_move_for_knight_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left two
        self.assertFalse(b._isLegalMoveForKnight([5, 2, 3, 2]))
    """

    # Tests for isLegalMoveForBishop()

    """
    def test_is_legal_move_for_bishop(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board2

        #Move up and to the left
        self.assertTrue(b._isLegalMoveForBishop([2, 0, 0, 2]))
        
        #Move down and to the right
        self.assertTrue(b._isLegalMoveForBishop([2, 5, 4, 7]))

        b._board = ChessTest.board1

        #Legal kill
        self.assertTrue(b._isLegalMoveForBishop([5, 7, 1, 3]))
    
    def test_is_legal_move_for_bishop_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertFalse(b._isLegalMoveForBishop([2, 7, 1, 7]))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForBishop([5, 0, 3, 2]))

        #Path blocked by enemy piece
        #(Even though this would otherwise be a legitimate kill)
        self.assertFalse(b._isLegalMoveForBishop([5, 7, 0, 2]))
    """
    
    # Tests for isLegalMoveForQueen()
    
    """
    def test_is_legal_move_for_queen(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertTrue(b._isLegalMoveForQueen([5, 3, 4, 3]))

        #Move right
        self.assertTrue(b._isLegalMoveForQueen([3, 3, 4, 3]))

        #Move up and left
        self.assertTrue(b._isLegalMoveForQueen([3, 3, 0, 6]))

        #Move down and right
        self.assertTrue(b._isLegalMoveForQueen([5, 3, 6, 2]))

        #Legal kill
        self.assertTrue(b._isLegalMoveForQueen([5, 3, 7, 1]))

        #Legal kill2
        self.assertTrue(b._isLegalMoveForQueen([3, 3, 5, 3]))

        #Legal kill3
        self.assertTrue(b._isLegalMoveForQueen([5, 3, 2, 0]))
    
    def test_is_legal_move_for_queen_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move like horse
        self.assertFalse(b._isLegalMoveForQueen([3, 3, 5, 4]))

        #Path blocked by friendly piece
        self.assertFalse(b._isLegalMoveForQueen([5, 3, 6, 5]))

        #Path blocked by enemy piece
        #(Even though this would otherwise be a legitimate kill)
        self.assertFalse(b._isLegalMoveForQueen([5, 3, 1, 3]))
    """

    # Tests for isLegalMoveForKing()

    """
    def test_is_legal_move_for_king(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move left
        self.assertTrue(b._isLegalMoveForKing([4, 7, 3, 7]))

        #Move up and left 
        self.assertTrue(b._isLegalMoveForKing([4, 0, 3, 1]))

        #Move down 
        self.assertTrue(b._isLegalMoveForKing([4, 7, 4, 6]))

        b._board = ChessTest.board3

        #Legal kill
        self.assertTrue(b._isLegalMoveForKing([4, 3, 3, 3]))

    def test_is_legal_move_for_king_negative_test(self):
        from board import Board
        b = Board()
        b._board = ChessTest.board1

        #Move diagnoally two spaces
        self.assertFalse(b._isLegalMoveForKing([4, 0, 2, 2]))
    """
   
    #################################
    # Tests for BoardAnalyzer class #
    #################################

    #Tests for isCheckMate()

    """
    def test_is_check_mate(self):
        import board_analyzer
        import constants
        from board import Board

        board1 = Board()
        board1._board = ChessTest.checkmate1

        board2 = Board()
        board2._board = ChessTest.checkmate2
        
        self.assertTrue(board_analyzer.isCheckMate(board1, constants.WHITE_PLAYER))
        self.assertTrue(board_analyzer.isCheckMate(board2, constants.BLACK_PLAYER))

    def test_is_check_mate_negative(self):
        import board_analyzer
        import constants
        from board import Board

        board1 = Board()
        board1._board = ChessTest.board1

        board2 = Board()
        board2._board = ChessTest.board2
        
        self.assertFalse(board_analyzer.isCheckMate(board1, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board1, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board2, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board2, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board1, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board1, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board2, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckMate(board2, constants.BLACK_PLAYER))
    """

    #Tests for isCheck()

    """
    def test_is_check(self):
        import board_analyzer
        import constants
    
        self.assertTrue(board_analyzer.isCheckStatic(ChessTest.check1, constants.WHITE_PLAYER))
        self.assertTrue(board_analyzer.isCheckStatic(ChessTest.check2, constants.BLACK_PLAYER))
        
    def test_is_check_negative(self):
        import board_analyzer
        import constants

        self.assertFalse(board_analyzer.isCheckStatic(ChessTest.board1, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckStatic(ChessTest.board1, constants.BLACK_PLAYER))
        self.assertFalse(board_analyzer.isCheckStatic(ChessTest.board2, constants.WHITE_PLAYER))
        self.assertFalse(board_analyzer.isCheckStatic(ChessTest.board2, constants.BLACK_PLAYER))

if __name__ == '__main__':
    unittest.main()
