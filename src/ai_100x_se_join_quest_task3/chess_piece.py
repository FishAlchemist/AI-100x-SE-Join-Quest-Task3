from enum import Enum
from typing import Tuple

Position = Tuple[int, int]


class ChessSide(Enum):
    RED = 1
    BLACK = 2


class Piece:
    def __init__(self, color: ChessSide, position: Position):
        self.color = color
        self.position = position

    def is_valid_move(
        self, start_position: Position, end_position: Position, board_state
    ) -> bool:
        """Check if a move is valid for the piece.

        Args:
            start_position: The starting position (row, col)
            end_position: The ending position (row, col)
            board_state: The current state of the board

        Returns:
            bool: True if the move is valid, False otherwise
        """
        # Ensure positions are within board boundaries (1-10 for rows, 1-9 for columns)
        start_row, start_col = start_position
        end_row, end_col = end_position

        if not (1 <= start_row <= 10 and 1 <= start_col <= 9):
            return False
        if not (1 <= end_row <= 10 and 1 <= end_col <= 9):
            return False

        # Cannot move to a position occupied by a piece of the same color
        end_piece = board_state[end_row - 1][end_col - 1]
        if end_piece and end_piece.color == self.color:
            return False

        # Let subclass implement specific movement rules
        return self._check_piece_specific_rules(
            start_position, end_position, board_state
        )

    def _check_piece_specific_rules(
        self, start_position: Position, end_position: Position, board_state
    ) -> bool:
        """Check piece-specific movement rules.

        Args:
            start_position: The starting position (row, col)
            end_position: The ending position (row, col)
            board_state: The current state of the board

        Returns:
            bool: True if the piece-specific rules are satisfied, False otherwise
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def get_display_name(self):
        raise NotImplementedError


class General(Piece):
    def _check_piece_specific_rules(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # General can only move one step horizontally or vertically.
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
    def _check_piece_specific_rules(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # Guard must move one step diagonally.
        is_diagonal_move = (
            abs(row_start - row_end) == 1 and abs(col_start - col_end) == 1
        )
        if not is_diagonal_move:
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


class Rook(Piece):
    def _check_piece_specific_rules(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # Rook must move in a straight line, either horizontally or vertically.
        if row_start != row_end and col_start != col_end:
            return False

        # Check for any pieces blocking the path.
        if row_start == row_end:  # Horizontal move
            step = 1 if col_end > col_start else -1
            for col in range(col_start + step, col_end, step):
                if board_state[row_start - 1][col - 1] is not None:
                    return False
        else:  # Vertical move
            step = 1 if row_end > row_start else -1
            for row in range(row_start + step, row_end, step):
                if board_state[row - 1][col_start - 1] is not None:
                    return False

        return True

    def get_display_name(self):
        return "車" if self.color == ChessSide.RED else "俥"


class Horse(Piece):
    def _check_piece_specific_rules(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # Horse must move in an "L" shape (日).
        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)
        if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
            return False

        # Check if the Horse is blocked (馬腳) by an adjacent piece.
        # When moving vertically (2 rows), check the intermediate step horizontally.
        # When moving horizontally (2 cols), check the intermediate step vertically.
        if row_diff == 2:
            blocking_row = row_start + (1 if row_end > row_start else -1)
            blocking_col = col_start
        else:  # col_diff == 2
            blocking_row = row_start
            blocking_col = col_start + (1 if col_end > col_start else -1)

        if board_state[blocking_row - 1][blocking_col - 1] is not None:
            return False

        return True

    def get_display_name(self):
        return "傌" if self.color == ChessSide.RED else "馬"


class Cannon(Piece):
    def _check_piece_specific_rules(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # Cannon must move in a straight line, either horizontally or vertically.
        if row_start != row_end and col_start != col_end:
            return False

        # Count pieces in the path
        pieces_in_path = 0
        if row_start == row_end:  # Horizontal move
            step = 1 if col_end > col_start else -1
            for col in range(col_start + step, col_end, step):
                if board_state[row_start - 1][col - 1] is not None:
                    pieces_in_path += 1
        else:  # Vertical move
            step = 1 if row_end > row_start else -1
            for row in range(row_start + step, row_end, step):
                if board_state[row - 1][col_start - 1] is not None:
                    pieces_in_path += 1

        # Check if the target position has a piece
        target_piece = board_state[row_end - 1][col_end - 1]

        # When capturing (target position has an opponent's piece)
        if target_piece is not None:
            # Need exactly one piece in path to capture
            return pieces_in_path == 1
        else:
            # When moving to an empty position, path must be clear
            return pieces_in_path == 0

    def get_display_name(self):
        return "炮" if self.color == ChessSide.RED else "砲"


class Elephant(Piece):
    def _check_piece_specific_rules(self, start_position, end_position, board_state):
        row_start, col_start = start_position
        row_end, col_end = end_position

        # Elephant must move exactly 2 steps diagonally
        if abs(row_end - row_start) != 2 or abs(col_end - col_start) != 2:
            return False

        # Check if the Elephant is trying to cross the river
        if self.color == ChessSide.RED:
            if row_end > 5:  # Can't cross the river (middle line)
                return False
        else:  # Black Elephant
            if row_end < 6:  # Can't cross the river (middle line)
                return False

        # Check if the Elephant's eye is blocked
        # The eye is the middle point of the diagonal move
        eye_row = (row_start + row_end) // 2
        eye_col = (col_start + col_end) // 2

        if board_state[eye_row - 1][eye_col - 1] is not None:
            return False

        return True

    def get_display_name(self):
        return "相" if self.color == ChessSide.RED else "象"


class Soldier(Piece):
    """Represents a Soldier piece in Chinese chess."""

    def _check_piece_specific_rules(
        self, start_pos: Position, end_pos: Position, board_state
    ) -> bool:
        """Check Soldier-specific movement rules.

        Args:
            start_pos: The starting position (row, col)
            end_pos: The target position (row, col)
            board_state: The current state of the board

        Returns:
            bool: True if the move follows Soldier's rules, False otherwise
        """
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        row_diff = end_row - start_row
        col_diff = end_col - start_col

        # 判斷是否過河
        crossed_river = False
        if self.color == ChessSide.RED:
            # 紅方兵過河：第5行以上
            crossed_river = start_row >= 5
        else:
            # 黑方卒過河：第6行以下
            crossed_river = start_row <= 6

        # 過河前只能前進，過河後可以前進或橫走
        if not crossed_river:
            # 未過河：只能前進一格
            if self.color == ChessSide.RED:
                # 紅方兵往上走（行數增加）
                if row_diff != 1 or col_diff != 0:
                    return False
            else:
                # 黑方卒往下走（行數增加）
                if row_diff != 1 or col_diff != 0:
                    return False
        else:
            # 過河後：可以前進或橫走一格，但不能後退
            if self.color == ChessSide.RED:
                # 紅方不能後退（不能往下走）
                if row_diff < 0:
                    return False
            else:
                # 黑方不能後退（不能往上走）
                if row_diff < 0:
                    return False

            # 每次只能移動一格
            if abs(row_diff) + abs(col_diff) != 1:
                return False

        return True

    def get_display_name(self):
        return "兵" if self.color == ChessSide.RED else "卒"
