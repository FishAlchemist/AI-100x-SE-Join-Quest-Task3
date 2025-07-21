from enum import Enum


class ChessSide(Enum):
    RED = 1
    BLACK = 2


class Piece:
    def __init__(self, color: ChessSide, position):
        self.color = color
        self.position = position

    def is_valid_move(self, start_position, end_position):
        raise NotImplementedError

    def get_display_name(self):
        raise NotImplementedError


class General(Piece):
    def is_valid_move(self, start_position, end_position, board_state):
        # General can only move one step horizontally or vertically.
        row_start, col_start = start_position
        row_end, col_end = end_position

        if abs(row_start - row_end) + abs(col_start - col_end) != 1:
            return False

        # General must stay within the palace.
        # Red palace: rows 1-3, cols 4-6
        if self.color == ChessSide.RED:
            if not (1 <= row_end <= 3 and 4 <= col_end <= 6):
                return False
        # Black palace: rows 8-10, cols 4-6
        else:
            if not (8 <= row_end <= 10 and 4 <= col_end <= 6):
                return False

        # Generals cannot face each other on the same file without any pieces in between.
        opponent_general = next(
            (
                piece
                for row in board_state
                for piece in row
                if isinstance(piece, General) and piece.color != self.color
            ),
            None,
        )

        if opponent_general and col_end == opponent_general.position[1]:
            # Check if there are any pieces between them
            min_row = min(row_end, opponent_general.position[0])
            max_row = max(row_end, opponent_general.position[0])

            is_clear = all(
                board_state[r - 1][col_end - 1] is None
                or (r == row_start and col_end == col_start)
                for r in range(min_row + 1, max_row)
            )

            if is_clear:
                return False

        return True

    def get_display_name(self):
        return "帥" if self.color == ChessSide.RED else "將"


class Guard(Piece):
    def is_valid_move(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # Guard must move one step diagonally.
        if not (abs(row_start - row_end) == 1 and abs(col_start - col_end) == 1):
            return False

        # Guard must stay within the palace.
        if self.color == ChessSide.RED:
            if not (1 <= row_end <= 3 and 4 <= col_end <= 6):
                return False
        else:  # Black Guard
            if not (8 <= row_end <= 10 and 4 <= col_end <= 6):
                return False

        return True

    def get_display_name(self):
        return "仕" if self.color == ChessSide.RED else "士"
