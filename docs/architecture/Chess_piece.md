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
    // 車的移動規則：
    //   - 沿直線（橫向或縱向）行棋，步數不限。
    // 車的吃子規則：
    //   - 吃子不需要配合，可以直接吃掉同一條直線上的棋子，但不能隔着吃子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "俥"，如果顏色是 BLACK 則返回 "車"。

Class: Horse
  // 代表傌/馬棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查傌/馬的移動是否有效。
    // 馬的移動規則：
    //   - 每次移動為「日」字形跳躍，即從起始點斜向跳躍到目標點，其路徑可分解為：
    //     - 橫向兩格後，再縱向一格。
    //     - 縱向兩格後，再橫向一格。
    // 絆馬腿：
    //   - 如果馬在移動路徑上，緊鄰起始點的直線方向（即「日」字形走法的第一步）有一棋子阻擋，則該方向的「日」字形走法無效。
    // 馬的吃子規則：
    //   - 可以直接吃掉日字格上的棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "傌"，如果顏色是 BLACK 則返回 "馬"。

Class: Cannon
  // 代表炮/砲棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查炮/砲的移動是否有效。
    // 炮的移動規則：
    //   - 沿直線（橫向或縱向）行棋，步數不限。
    //   - 不吃子時，路徑上不能有任何棋子阻擋。
    // 炮的吃子規則：
    //   - 吃子時，必須在移動路徑上跳過一個棋子（稱為「炮架」或「炮臺」），
    //     才能吃掉同一條直線上炮架後的對方棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "炮"，如果顏色是 BLACK 則返回 "砲"。

Class: Elephant
  // 代表相/象棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查相/象的移動是否有效。
    // 相（象）的移動規則：
    //   - 斜著飛過一個田字格 (diagonal move across a 'field' square)。
    //   - 移動時，行 (row) 和列 (column) 都必須改變 2 個單位，例如從 (r, c) 到 (r±2, c±2)。
    //   - 不能過河 (cannot cross the river)。
    // 絆象腿 (blocking elephant's leg)：
    //   - 如果從 start_position (r1, c1) 到 end_position (r2, c2) 的移動路徑上，
    //     位於田字格中心點 ((r1+r2)/2, (c1+c2)/2) 的位置有任何棋子阻擋，
    //     則該次移動無效。
    // 相（象）的吃子規則：
    //   - 可以直接吃掉田字格上的棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "相"，如果顏色是 BLACK 則返回 "象"。

Class: Soldier
  // 代表兵/卒棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查兵/卒的移動是否有效。
    // 兵/卒的移動規則：
    //   - 不能後退。
    //   - **過楚河漢界 (river) 前**：
    //     - 只能向前移動一步。
    //   - **過楚河漢界 (river) 後**：
    //     - 除了向前移動一步外，還可以橫向（左右）移動一步。
    // 兵/卒的吃子規則：
    //   - **過楚河漢界 (river) 前**：
    //     - 只能吃掉前方一格的敵方棋子。
    //   - **過楚河漢界 (river) 後**：
    //     - 可以吃掉前方一格、左方一格或右方一格的敵方棋子。
    // 注意：此方法僅檢查棋子自身的移動模式，不考慮棋盤上的其他棋子或吃子行為。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "兵"，如果顏色是 BLACK 則返回 "卒"。