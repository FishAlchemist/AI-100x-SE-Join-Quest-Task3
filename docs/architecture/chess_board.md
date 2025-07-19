Class: ChessBoard
  // 描述：代表中國象棋棋盤，管理所有棋子的位置。
  // 座標系統：
  //   - 使用 (row, column) 表示位置。
  //   - 棋盤大小：10 行 x 9 列。
  //   - 第 1 行是紅方的底線；第 10 行是黑方的頂線。
  //   - 第 1 列是從紅方視角看最左邊的列。

  - Attributes:
    - dimensions: (int, int) // (rows, columns)
    - board_state: array of arrays of Piece or None // 一個 10x9 的二維網格，
    // 其中第一維代表行（0-9），第二維代表列（0-8）。
    // 每個元素可以存放一個 Piece 物件或為 None（空）。

  - Methods:
    - initialize_board(): void
    // 為新遊戲設置所有棋子的初始位置。
    - get_piece_at(position: (row, column)): Piece or None
    // 檢索指定位置的 Piece 物件。
    // 如果位置為空，則返回 None。
    // 內部使用 is_position_on_board 並在位置超出棋盤邊界時拋出 IndexError。
    - place_piece(piece: Piece, position: (row, column)): void
    // 將給定的 Piece 物件放置在棋盤上的指定位置。
    // 內部使用 is_position_on_board 並在位置超出棋盤邊界時拋出 IndexError。
    // 如果位置已被佔用，則拋出 ValueError。
    - remove_piece(position: (row, column)): Piece or None
    // 從指定位置移除 Piece 物件並返回它。
    // 如果位置為空，則返回 None。
    // 內部使用 is_position_on_board 並在位置超出棋盤邊界時拋出 IndexError。
    - move_piece(start_position: (row, column), end_position: (row, column)): boolean
    // 嘗試將棋子從 start_position 移動到 end_position。
    // 調用棋子的 is_valid_move 並處理吃子。
    // 如果成功則返回 true，否則返回 false。
    // 內部使用 is_position_on_board 並在 start_position 或 end_position 超出棋盤邊界時拋出 IndexError。
    // 對於基於遊戲規則的非法移動（例如，無效的棋子移動、路徑被阻擋、將軍），考慮返回更詳細的結果物件或枚舉，而不是簡單的布林值。
    - is_position_on_board(position: (row, column)): boolean
    // 檢查給定的 (row, column) 位置是否在棋盤的有效邊界內。