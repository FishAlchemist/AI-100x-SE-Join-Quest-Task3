Class: ChessBoard
  // 描述：代表中國象棋棋盤，管理所有棋子的位置。
  // 座標系統：
  //   - 使用 (row, column) 表示位置。
  //   - 棋盤大小：10 行 (rows) x 9 列 (columns)。
  //   - 第 1 行 (row) 是紅方的底線；第 10 行 (row) 是黑方的頂線。
  //   - 第 1 列是從紅方視角看最左邊的列。

  - Attributes:
    - dimensions: (int, int) // (rows, columns)
    - board_state: array of arrays of Piece or None // 一個 10x9 的二維網格，
    // 其中第一維代表行（0-9），第二維代表列（0-8）。
    // 每個元素可以存放一個 Piece 物件或為 None（空）。
    - current_turn_color: ChessSide // 當前輪到哪一方下棋（紅方或黑方）。

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
    - is_in_opponent_territory(position: (row, column), player_color: Color): boolean
    // 檢查給定的 (row, column) 位置是否在指定玩家的對方領地內（即已過楚河漢界）。
    // 對於紅方 (Red)，對方領地是第 6 行 (row) 到第 10 行 (row)。
    // 對於黑方 (Black)，對方領地是第 1 行 (row) 到第 5 行 (row)。
    - is_in_palace(position: (row, column), player_color: Color): boolean
    // 檢查給定的 (row, column) 位置是否在指定玩家的九宮 (palace) 內。
    // 對於紅方 (Red)，九宮 (palace) 範圍是行 (row) 1-3，列 (column) 4-6。
    // 對於黑方 (Black)，九宮 (palace) 範圍是行 (row) 8-10，列 (column) 4-6。

  - Methods: // 遊戲狀態判斷
    - is_check(player_color: Color): boolean
    // 檢查指定顏色的將（帥）是否被將軍。
    - is_checkmate(player_color: Color): boolean
    // 檢查指定顏色的將（帥）是否被將死。
    // 內部使用 is_check 和檢查所有合法走法。
    - is_stalemate(player_color: Color): boolean
    // 檢查指定顏色的一方是否困斃（無子可動但將（帥）未被將軍）。
    // 內部檢查所有合法走法。
    - check_perpetual_check(): GameEndReason or None
    // 檢查是否發生長將。
    // 需要追蹤遊戲歷史中的重複將軍局面。
    - check_perpetual_chase(): GameEndReason or None
    // 檢查是否發生長捉。
    // 需要追蹤遊戲歷史中的重複捉子局面。
    - get_game_outcome(): (GameResult, GameEndReason) or None
    // 判斷並返回當前遊戲的結果和結束原因。
    // 返回值包含 GameResult (誰輸誰贏或平手) 和 GameEndReason (遊戲結束的具體原因)。
    // 依序檢查將死、困斃、將帥被吃、長將、長捉、和棋等條件。

Enum: GameResult
  // 代表中國象棋遊戲的最終結果。
  - RED_WINS // 紅方獲勝。
  - BLACK_WINS // 黑方獲勝。
  - DRAW // 遊戲平手。

Enum: GameEndReason
  // 代表中國象棋遊戲結束的具體原因。
  - CHECKMATE // 將死：一方的將（帥）被將軍且無法解除，被將死方輸棋。
  - STALEMATE // 困斃：當一方的將（帥）並未被將軍，但其所有合法走法都會導致將（帥）被將軍，則該方困斃，遊戲結束，困斃方輸棋。
  - PERPETUAL_CHECK_LOSS // 長將判負：一方連續不斷地將軍對方，且對方無法擺脫被將軍的狀態，若此情況持續發生，判長將方輸棋。
  - PERPETUAL_CHASE_LOSS // 長捉判負：一方連續不斷地捉（威脅吃掉）對方沒有保護的棋子，且對方無法擺脫被捉的狀態，若此情況持續發生，判長捉方輸棋。
  - AGREED_DRAW // 雙方同意和棋。
  - GENERAL_CAPTURED // 將（帥）被吃：一方的將（帥）被對方吃掉，被吃方立刻輸棋。
  // 補充說明：除了 AGREED_DRAW 和 STALEMATE，其他導致平手的條件（如重複局面、子力不足等）也屬於和棋範疇。