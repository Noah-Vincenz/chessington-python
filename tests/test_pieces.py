from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, King, Knight, Queen, Rook, Bishop

class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(4, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

         # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves

class TestKings:

    @staticmethod
    def test_white_kings_can_move_to_all_neighbouring_squares():

        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(1,5),
            Square.at(1,3),
            Square.at(2,5),
            Square.at(2,3),
            Square.at(2,4),
            Square.at(0,5),
            Square.at(0,3),
            Square.at(0,4)
        ])

    @staticmethod
    def test_white_kings_can_move_to_all_neighbouring_squares_inside_board():

        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(7, 0)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(6,0),
            Square.at(6,1),
            Square.at(7,1)
        ])

    @staticmethod
    def test_white_kings_can_move_to_unoccupied_neighbouring_squares_inside_board():

        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(7, 0)
        board.set_piece(square, king)
        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(6, 0)
        board.set_piece(enemy1_square, enemy1)
        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(6, 1)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(6,0),
            Square.at(7,1)
        ])


class TestKnights:

    @staticmethod
    def test_white_knights_can_move_to_all_possible_squares():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(0, 6),
            Square.at(0, 2),
            Square.at(2, 6),
            Square.at(2, 2),
            Square.at(3, 3),
            Square.at(3, 5)
        ])
    
    @staticmethod
    def test_white_knights_can_move_to_all_unoccupied_squares():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, knight)
        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(0, 6)
        board.set_piece(enemy1_square, enemy1)
        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 6)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(0, 6),
            Square.at(0, 2),
            Square.at(2, 2),
            Square.at(3, 3),
            Square.at(3, 5)
        ])

class TestQueens:

    @staticmethod
    def test_white_queens_can_move_to_all_possible_squares():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(0, 3),
            Square.at(0, 4),
            Square.at(0, 5),
            Square.at(1, 0),
            Square.at(1, 1),
            Square.at(1, 2),
            Square.at(1, 3),
            Square.at(1, 5),
            Square.at(1, 6),
            Square.at(1, 7),
            Square.at(2, 3),
            Square.at(2, 4),
            Square.at(2, 5),
            Square.at(3, 2),
            Square.at(3, 4),       
            Square.at(3, 6),
            Square.at(4, 1),
            Square.at(4, 4),
            Square.at(4, 7),
            Square.at(5, 0),
            Square.at(5, 4),
            Square.at(6, 4),
            Square.at(7, 4)
        ])

    @staticmethod
    def test_white_queens_can_move_to_all_unoccupied_squares():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, queen)
        team1 = Pawn(Player.WHITE)
        team1_square = Square.at(2, 5)
        board.set_piece(team1_square, team1)
        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(3, 4)
        board.set_piece(enemy1_square, enemy1)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert set(moves) == set([
            Square.at(0, 3),
            Square.at(0, 4),
            Square.at(0, 5),
            Square.at(1, 0),
            Square.at(1, 1),
            Square.at(1, 2),
            Square.at(1, 3),
            Square.at(1, 5),
            Square.at(1, 6),
            Square.at(1, 7),
            Square.at(2, 3),
            Square.at(2, 4),
            Square.at(3, 2),
            Square.at(3, 4),       
            Square.at(4, 1),
            Square.at(5, 0)
        ])