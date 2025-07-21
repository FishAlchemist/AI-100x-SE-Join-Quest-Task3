from .chess_piece import Piece, General, ChessSide


class ChessBoard:
    def __init__(self):
        self.board_state = [[None for _ in range(9)] for _ in range(10)]
        self.move_result = False
        self.last_captured_general = None  # Track if a general was just captured

    def place_piece(self, piece: Piece, position):
        row, col = position
        self.board_state[row - 1][col - 1] = piece

    def move_piece(self, start_position, end_position):
        start_row, start_col = start_position
        end_row, end_col = end_position
        
        # Get the moving piece
        piece = self.board_state[start_row - 1][start_col - 1]
        if not piece:
            self.move_result = False
            return False
        
        # Check if the move is valid
        if not piece.is_valid_move(start_position, end_position, self.board_state):
            self.move_result = False
            return False
            
        # Save captured piece (if any) for state check
        captured_piece = self.board_state[end_row - 1][end_col - 1]
            
        # Update board state
        self.board_state[start_row - 1][start_col - 1] = None
        self.board_state[end_row - 1][end_col - 1] = piece
        
        # Update piece's position
        piece.position = end_position
        
        # Check if we captured a general
        if isinstance(captured_piece, General):
            self.last_captured_general = captured_piece
            self.move_result = True
            return True
        
        # For non-general captures, game continues normally
        self.last_captured_general = None
        self.move_result = True
        return True
        
    def is_game_over(self):
        """Check if the game is over and determine the winner and reason.
        
        Returns:
            tuple: (is_over: bool, winner: ChessSide or None, reason: str or None)
            where reason describes why the game ended (e.g., "Black general captured",
            "Invalid state: multiple red generals", etc.)
        """
        # If a general was just captured
        if self.last_captured_general:
            if self.last_captured_general.color == ChessSide.BLACK:
                return True, ChessSide.RED, "Black general captured"
            else:
                return True, ChessSide.BLACK, "Red general captured"

        # Track the presence of generals
        red_general = False
        black_general = False
        red_general_count = 0
        black_general_count = 0
        
        for row in self.board_state:
            for piece in row:
                if isinstance(piece, General):
                    if piece.color == ChessSide.RED:
                        red_general_count += 1
                        red_general = True
                    else:
                        black_general_count += 1
                        black_general = True

        # Check for invalid states (multiple generals of same color)
        if red_general_count > 1:
            return True, None, "Invalid state: multiple red generals"
        if black_general_count > 1:
            return True, None, "Invalid state: multiple black generals"
            
        # Game continues if both generals are present
        if red_general and black_general:
            return False, None, None
            
        # If a side lost their general (and the other side has one), they lose
        if not black_general and red_general:
            return True, ChessSide.RED, "Black general captured"
        if not red_general and black_general:
            return True, ChessSide.BLACK, "Red general captured"
            
        # Game is over with no winner if no generals are present
        return True, None, "No generals present on the board"