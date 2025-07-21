from pytest_bdd import scenarios, given, when, then, parsers
from ai_100x_se_join_quest_task3.chess_board import ChessBoard
from ai_100x_se_join_quest_task3.chess_piece import (
    General,
    Guard,
    Horse,
    Rook,
    Cannon,
    Soldier,
    Elephant,
    ChessSide,
)
import re

scenarios("../chinese_chess.feature")

PIECE_MAPPING = {
    "Red General": (General, ChessSide.RED),
    "Black General": (General, ChessSide.BLACK),
    "Red Guard": (Guard, ChessSide.RED),
    "Black Guard": (Guard, ChessSide.BLACK),
    "Red Horse": (Horse, ChessSide.RED),
    "Red Rook": (Rook, ChessSide.RED),
    "Black Rook": (Rook, ChessSide.BLACK),
    "Red Cannon": (Cannon, ChessSide.RED),
    "Black Cannon": (Cannon, ChessSide.BLACK),
    "Red Soldier": (Soldier, ChessSide.RED),
    "Black Soldier": (Soldier, ChessSide.BLACK),
    "Red Elephant": (Elephant, ChessSide.RED),
}


def parse_position(position_str):
    match = re.match(r"\((\d+),\s*(\d+)\)", position_str)
    if match:
        return int(match.group(1)), int(match.group(2))
    raise ValueError(f"Invalid position format: {position_str}")


@given("the board has:", target_fixture="board")
def given_the_board_has(datatable):
    board = ChessBoard()
    # The datatable is a list of lists, where the first list is the header.
    header = datatable[0]
    for row_data in datatable[1:]:
        row_dict = dict(zip(header, row_data))
        piece_name = row_dict["Piece"]
        position_str = row_dict["Position"]
        position = parse_position(position_str)

        if piece_name in PIECE_MAPPING:
            piece_class, piece_side = PIECE_MAPPING[piece_name]
            piece = piece_class(piece_side, position)
            board.place_piece(piece, position)
        else:
            raise ValueError(f"Unknown piece: {piece_name}")
    return board


@given(
    parsers.parse("the board is empty except for a Red General at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_general(row, col):
    board = ChessBoard()
    general = General(ChessSide.RED, (row, col))
    board.place_piece(general, (row, col))
    return board


@given(
    parsers.parse("the board is empty except for a Red Guard at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_guard(row, col):
    board = ChessBoard()
    guard = Guard(ChessSide.RED, (row, col))
    board.place_piece(guard, (row, col))
    return board


@given(
    parsers.parse("the board is empty except for a Red Rook at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_rook(row, col):
    board = ChessBoard()
    rook = Rook(ChessSide.RED, (row, col))
    board.place_piece(rook, (row, col))
    return board


@given(
    parsers.parse("the board is empty except for a Red Horse at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_horse(row, col):
    board = ChessBoard()
    horse = Horse(ChessSide.RED, (row, col))
    board.place_piece(horse, (row, col))
    return board


@given(
    parsers.parse("the board is empty except for a Red Soldier at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_soldier(row, col):
    board = ChessBoard()
    soldier = Soldier(ChessSide.RED, (row, col))
    board.place_piece(soldier, (row, col))
    return board


@given(
    parsers.parse("the board is empty except for a Red Cannon at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_cannon(row, col):
    board = ChessBoard()
    cannon = Cannon(ChessSide.RED, (row, col))
    board.place_piece(cannon, (row, col))
    return board


@given(
    parsers.parse("the board is empty except for a Red Elephant at ({row:d}, {col:d})"),
    target_fixture="board",
)
def given_the_board_is_empty_except_for_a_red_elephant(row, col):
    board = ChessBoard()
    elephant = Elephant(ChessSide.RED, (row, col))
    board.place_piece(elephant, (row, col))
    return board


@when(
    parsers.parse(
        "Red moves the General from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_general(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Guard from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_guard(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Rook from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_rook(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Horse from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_horse(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Cannon from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_cannon(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Elephant from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_elephant(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Soldier from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_soldier(board, from_row, from_col, to_row, to_col):
    board.move_piece((from_row, from_col), (to_row, to_col))


@then("the move is legal")
def then_the_move_is_legal(board):
    assert board.move_result is True


@then("the move is illegal")
def then_the_move_is_illegal(board):
    assert board.move_result is False


@then("Red wins immediately")
def then_red_wins_immediately(board):
    # Give the board a chance to update after the move
    is_over, winner, reason = board.is_game_over()
    from ai_100x_se_join_quest_task3.chess_piece import ChessSide

    assert reason == "Black general captured", (
        f"Expected 'Black general captured' but got '{reason}'"
    )
    assert winner == ChessSide.RED, f"Expected RED winner but got {winner}"
    assert is_over is True


@then("the game is not over just from that capture")
def then_the_game_is_not_over(board):
    is_over, _, reason = board.is_game_over()
    assert reason is None, f"Expected no game over reason but got '{reason}'"
    assert is_over is False
