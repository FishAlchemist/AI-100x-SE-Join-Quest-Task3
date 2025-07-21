from pytest_bdd import scenarios, given, when, then, parsers
from ai_100x_se_join_quest_task3.chess_board import ChessBoard
from ai_100x_se_join_quest_task3.chess_piece import General, Guard, ChessSide
import re

scenarios("../chinese_chess.feature")

PIECE_MAPPING = {
    "Red General": (General, ChessSide.RED),
    "Black General": (General, ChessSide.BLACK),
    "Red Guard": (Guard, ChessSide.RED),
    # Add other piece types here as they are implemented
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


@when(
    parsers.parse(
        "Red moves the General from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_general(board, from_row, from_col, to_row, to_col):
    board.move_result = board.move_piece((from_row, from_col), (to_row, to_col))


@when(
    parsers.parse(
        "Red moves the Guard from ({from_row:d}, {from_col:d}) to ({to_row:d}, {to_col:d})"
    )
)
def when_red_moves_the_guard(board, from_row, from_col, to_row, to_col):
    board.move_result = board.move_piece((from_row, from_col), (to_row, to_col))


@then("the move is legal")
def then_the_move_is_legal(board):
    assert board.move_result is True


@then("the move is illegal")
def then_the_move_is_illegal(board):
    assert board.move_result is False
