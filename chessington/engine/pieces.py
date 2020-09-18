"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player
        self.has_moved = False

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.has_moved = True

    def inside_board(self, square, board):
        col = square.col
        row = square.row
        size = board.board_size
        if row < size and row >= 0 and col < size and col >= 0:
            return True
        return False

    def is_enemy(self, square, board):
        if board.get_piece(square) != None and board.get_piece(square).player != self.player:
            return True
        return False

    def can_move(self, sq, board):
        if self.inside_board(sq, board) and (board.get_piece(sq) == None or self.is_enemy(sq, board)):
            return True
        return False

class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        row = current_square.row
        col = current_square.col
        available_moves = []
        row_dir = 1 if self.player == Player.WHITE else -1
        sq = Square.at(row + row_dir, col)
        if self.inside_board(sq, board) and board.get_piece(sq) == None:
            available_moves.append(sq)
            sq = Square.at(row + row_dir, col + 1)
            if self.inside_board(sq, board) and self.is_enemy(sq, board):
                available_moves.append(sq)
            sq = Square.at(row + row_dir, col - 1)
            if self.inside_board(sq, board) and self.is_enemy(sq, board):
                available_moves.append(sq)
            if self.has_moved == False:
                sq = Square.at(row + 2 * row_dir, col)
                if self.inside_board(sq, board) and board.get_piece(sq) == None:
                    available_moves.append(sq)
        return available_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        row = current_square.row
        col = current_square.col
        available_moves = []
        x = [-2, -2, -1, -1, 1, 1, 2, 2]
        y = [1, -1, 2, -2, 2, -2, -1, 1]
        for i in range(0, len(x)):
            sq = Square.at(row + x[i], col + y[i])
            if self.can_move(sq, board):
                available_moves.append(sq)
        return available_moves


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        row = current_square.row
        col = current_square.col
        available_moves = []
        for i in range(row + 1, board.board_size):
            sq = Square.at(i, col)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        i = row - 1
        while i >= 0:
            sq = Square.at(i, col)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
                i -= 1
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        for j in range(col + 1, board.board_size):
            sq = Square.at(row, j)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        j = col - 1
        while j >= 0:
            sq = Square.at(row, j)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
                j -= 1
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        i = row + 1
        j = col + 1
        while i < board.board_size and j < board.board_size:
            sq = Square.at(i, j)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
                i += 1
                j += 1
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        i = row + 1
        j = col - 1
        while i < board.board_size and j >= 0:
            sq = Square.at(i, j)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
                i += 1
                j -= 1
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        i = row - 1
        j = col + 1
        while i >= 0 and j < board.board_size:
            sq = Square.at(i, j)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
                i -= 1
                j += 1
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            sq = Square.at(i, j)
            if board.get_piece(sq) == None:
                available_moves.append(sq)
                i -= 1
                j -= 1
            else:
                if self.is_enemy(sq, board):
                    available_moves.append(sq)
                break
        return available_moves


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        row = current_square.row
        col = current_square.col
        available_moves = []
        change = [-1,0,1]
        for row_change in change:
            for col_change in change:
                sq = Square.at(row + row_change, col + col_change)
                if self.can_move(sq, board):
                    available_moves.append(sq)
        return available_moves