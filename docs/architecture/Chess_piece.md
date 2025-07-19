Enum: ChessSide
  // 代表中國象棋遊戲中的兩方。
  - RED
  - BLACK

Abstract Class: Piece
  // 代表一個通用的中國象棋棋子。
  - Attributes:
    - color: ChessSide // 棋子所屬的顏色（紅方或黑方）。
    - position: (row, column) tuple // 棋子在棋盤上的當前位置。
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查從 start_position 到 end_position 的移動對於此特定棋子類型是否有效。
    - get_display_name(): string
    // 抽象方法：根據棋子類型和顏色返回其本地化的顯示名稱（例如，將/帥）。

Class: General
  // 代表將/帥棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查將/帥的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "帥"，如果顏色是 BLACK 則返回 "將"。

Class: Guard
  // 代表仕/士棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查仕/士的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "仕"，如果顏色是 BLACK 則返回 "士"。

Class: Rook
  // 代表俥/車棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查俥/車的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "俥"，如果顏色是 BLACK 則返回 "車"。

Class: Horse
  // 代表傌/馬棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查傌/馬的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "傌"，如果顏色是 BLACK 則返回 "馬"。

Class: Cannon
  // 代表炮/砲棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查炮/砲的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "炮"，如果顏色是 BLACK 則返回 "砲"。

Class: Elephant
  // 代表相/象棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查相/象的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "相"，如果顏色是 BLACK 則返回 "象"。

Class: Soldier
  // 代表兵/卒棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查兵/卒的移動是否有效。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "兵"，如果顏色是 BLACK 則返回 "卒"。