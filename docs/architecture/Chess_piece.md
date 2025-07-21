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
    // 將（帥）的移動規則：
    //   - 只能在九宮 (palace) 內移動。
    //   - 每次移動為橫向或縱向一格，即行 (row) 或列 (column) 改變 ±1。
    // 將（帥）的吃子規則：
    //   - 將（帥）可以直接吃掉其移動規則允許到達的敵方棋子。
    // 特殊規則 (明將)：
    //   - 將（帥）和對方的將（帥）不能在同一條豎線上直接面對面，中間沒有其他棋子阻擋。
    //   - 任何一方走棋造成將帥直接碰面（即明將），則該方立刻輸棋。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "帥"，如果顏色是 BLACK 則返回 "將"。

Class: Guard
  // 代表仕/士棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查仕/士的移動是否有效。
    // 仕（士）的移動規則：
    //   - 只能在九宮 (palace) 內移動。
    //   - 每次移動為斜向一格，即行 (row) 和列 (column) 同時改變 ±1。
    //   - 由於其移動限制，仕（士）最多只能到達九宮內的5個交叉點，是象棋中活動範圍最小的棋子。
    // 仕（士）的吃子規則：
    //   - 可以吃掉九宮內，斜線上相鄰一格的敵方棋子，即與自身位置行 (row) 和列 (column) 同時改變 ±1 的敵方棋子。
    //   - 這表示仕（士）可以吃掉其移動規則允許到達的敵方棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "仕"，如果顏色是 BLACK 則返回 "士"。

Class: Rook
  // 代表俥/車棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查俥/車的移動是否有效。
    // 車的移動規則：
    //   - 可以在棋盤上沿著直線（橫著或豎著）走任意格數。
    //   - 這表示移動時，棋子的行 (row) 或列 (column) 其中一個座標會保持不變，另一個座標則可以任意改變。
    // 車的吃子規則：
    //   - 吃子不需要配合，可以直接吃掉同一條直線上的棋子，但不能隔着吃子。
    //   - 這表示目標位置與起始位置在同一行 (row) 或同一列 (column) 上，且兩點之間沒有其他棋子。
    //   - 這表示車可以吃掉其移動規則允許到達的敵方棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "俥"，如果顏色是 BLACK 則返回 "車"。

Class: Horse
  // 代表傌/馬棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查傌/馬的移動是否有效。
    // 馬的移動規則：
    //   - 每次移動都呈現「日」字形。這意味著有兩種移動方式：
    //     1. 先橫向移動兩格，再縱向移動一格 (即列 (column) 改變 ±2 且行 (row) 改變 ±1)。
    //     2. 或者先縱向移動兩格，再橫向移動一格 (即行 (row) 改變 ±2 且列 (column) 改變 ±1)。
    // 絆馬腿：
    //   - 如果馬在移動時，其「日」字形路徑中，直線方向上的「中間點」（即馬要跨過的第一個格子）有其他棋子阻擋，則該次「日」字形移動無效。
    //   - 以座標表示，如果馬從起始位置 (r, c) 移動：
    //     - 若目標是 (r+1, c+2)，則中間阻擋點是 (r, c+1)。
    //     - 若目標是 (r+1, c-2)，則中間阻擋點是 (r, c-1)。
    //     - 若目標是 (r-1, c+2)，則中間阻擋點是 (r, c+1)。
    //     - 若目標是 (r-1, c-2)，則中間阻擋點是 (r, c-1)。
    //     - 若目標是 (r+2, c+1)，則中間阻擋點是 (r+1, c)。
    //     - 若目標是 (r+2, c-1)，則中間阻擋點是 (r+1, c)。
    //     - 若目標是 (r-2, c+1)，則中間阻擋點是 (r-1, c)。
    //     - 若目標是 (r-2, c-1)，則中間阻擋點是 (r-1, c)。
    //     - 如果這些中間阻擋點有棋子，則馬無法完成該方向的移動。
    // 馬的吃子規則：
    //   - 馬可以直接吃掉其「日」字形移動目標位置上的敵方棋子。
    //   - 這表示如果目標位置 (r±1, c±2) 或 (r±2, c±1) 上有敵方棋子，且沒有絆馬腿，馬就可以吃掉它。
    //   - 這表示馬可以吃掉其移動規則允許到達的敵方棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "傌"，如果顏色是 BLACK 則返回 "馬"。

Class: Cannon
  // 代表炮/砲棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查炮/砲的移動是否有效。
    // 炮的移動規則：
    //   - 可以在棋盤上沿著直線（橫著或豎著）走任意格數。
    //   - 這表示移動時，棋子的行 (row) 或列 (column) 其中一個座標會保持不變，另一個座標則可以任意改變。
    //   - 不吃子時，炮的移動路徑上不能有任何棋子阻擋。
    // 炮的吃子規則：
    //   - 吃子時，炮必須在移動路徑上跳過一個棋子（稱為「炮架」或「炮臺」），才能吃掉同一條直線上炮架後的敵方棋子。
    //   - 這表示在炮的起始位置與目標位置之間，必須且只能有一個棋子作為「炮架」。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "炮"，如果顏色是 BLACK 則返回 "砲"。

Class: Elephant
  // 代表相/象棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查相/象的移動是否有效。
    // 相（象）的移動規則：
    //   - 每次移動都斜向兩格，即俗稱的「田」字形。
    //   - 這表示移動時，行 (row) 和列 (column) 都必須同時改變 2 個單位，例如從 (r, c) 到 (r±2, c±2)。
    //   - 相（象）不能過河，即不能移動到對方的領地。
    // 絆象腿 (blocking elephant's leg)：
    //   - 如果相（象）在移動時，其「田」字形路徑的中心點有其他棋子阻擋，則該次移動無效。
    //   - 以座標表示，如果相（象）從起始位置 (r1, c1) 移動到目標位置 (r2, c2)，
    //     則中間阻擋點是 ((r1+r2)/2, (c1+c2)/2)。如果這個中間點有棋子，則相（象）無法完成該方向的移動。
    // 相（象）的吃子規則：
    //   - 相（象）可以直接吃掉其「田」字形移動目標位置上的敵方棋子。
    //   - 這表示如果目標位置 (r±2, c±2) 上有敵方棋子，且沒有絆象腿，相（象）就可以吃掉它。
    //   - 這表示相（象）可以吃掉其移動規則允許到達的敵方棋子。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "相"，如果顏色是 BLACK 則返回 "象"。

Class: Soldier
  // 代表兵/卒棋子。
  - Inherits from: Piece
  - Methods:
    - is_valid_move(start_position: (row, column), end_position: (row, column)): boolean
    // 檢查兵/卒的移動是否有效。
    // 兵/卒的移動規則：
    //   - 兵/卒不能後退。
    //   - **過楚河漢界 (river) 前**：
    //     - 只能向前移動一步 (即行 (row) 改變 ±1，列 (column) 不變)。
    //   - **過楚河漢界 (river) 後**：
    //     - 除了向前移動一步外，還可以橫向（左右）移動一步 (即行 (row) 不變，列 (column) 改變 ±1)。
    // 兵/卒的吃子規則：
    //   - **過楚河漢界 (river) 前**：
    //     - 只能吃掉前方一格的敵方棋子 (即目標位置的行 (row) 改變 ±1，列 (column) 不變)。
    //   - **過楚河漢界 (river) 後**：
    //     - 可以吃掉前方一格、左方一格或右方一格的敵方棋子。
    //     - 這表示目標位置的行 (row) 改變 ±1 且列 (column) 不變，或者行 (row) 不變且列 (column) 改變 ±1。
    //   - 這表示兵/卒可以吃掉其移動規則允許到達的敵方棋子。
    // 注意：此方法僅檢查棋子自身的移動模式，不考慮棋盤上的其他棋子或吃子行為。
    - get_display_name(): string
    // 如果顏色是 RED 則返回 "兵"，如果顏色是 BLACK 則返回 "卒"。