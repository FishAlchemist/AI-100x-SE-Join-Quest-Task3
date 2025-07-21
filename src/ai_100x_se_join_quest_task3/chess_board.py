from .chess_piece import Piece


class ChessBoard:
    def __init__(self):
        self.board_state = [[None for _ in range(9)] for _ in range(10)]
        self.move_result = False

    def place_piece(self, piece: Piece, position):
        row, col = position
        self.board_state[row - 1][col - 1] = piece

    def move_piece(self, start_position, end_position):
        row, col = start_position
        piece = self.board_state[row - 1][col - 1]
        if piece:
            return piece.is_valid_move(start_position, end_position, self.board_state)
        return False
