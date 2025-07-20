# 架構資料夾指南

本文件概述了 `architecture` 資料夾內文件編寫的要求，以確保所有架構描述的一致性和清晰度。

## 1. 描述要求 (註釋/標註)

`architecture` 資料夾內所有 `.md` 檔案中的描述和註釋應遵循以下格式和內容指南：

*   **註釋風格**：所有註釋都使用 `//` 開頭，其後內容**必須**使用 Markdown 語法進行格式化。
*   **行長度**：每行註釋的理想長度不應超過 80 個字元，以提高可讀性。將長註釋分成多行。
*   **目的**：註釋應清楚解釋所描述組件（`class`、`enum`、`attribute`、`method`）的 *目的* 和 *介面*。
*   **語言**：註釋應使用繁體中文編寫。程式碼相關的名稱（例如 `class` 名稱、`attribute` 名稱、`method` 名稱）應保留其原始英文形式。對於可能有多種中文翻譯的技術術語，應在中文翻譯後括號內附上英文原文，例如 `(rows, columns)`。
*   **Class/Enum 描述**：
    *   提供 `class`/`enum` 所代表內容的簡潔、高層次概述。
    *   範例：`// 代表中國象棋棋盤，管理棋子位置。`
*   **Attribute 描述**：
    *   簡要解釋 `attribute` 的作用及其預期類型。
    *   範例：`// (rows, columns)`
*   **Method 描述**：
    *   **第一行**：對 `method` 主要功能的簡潔摘要。
    *   **後續行（如果需要）**：
        *   解釋 `parameter` 及其作用。
        *   描述返回值。
        *   明確列出 `method` 可能引發的任何異常（例如，`如果...則引發 IndexError`，`如果...則引發 ValueError`）。
        *   提及任何內部依賴或關鍵行為（例如，`內部使用 is_position_on_board`）。
        *   對於棋子的移動方法，應明確區分「移動規則」和「吃子規則」，並將其分開描述。
        *   對於具有複雜返回邏輯的 `method`（例如 `move_piece` 返回詳細結果），簡要解釋不同的結果。

## 2. 內容結構要求

`architecture` 資料夾內的 `.md` 檔案應遵循一致的 Markdown 結構來描述系統的組件。

### Class/Enum 的一般結構：

```markdown
Class: [ClassName] // [可選的簡要描述/別名]
  // [符合描述要求的 Class 級別描述]
  // [額外的 Class 級別詳細資訊，例如 ChessBoard 的座標系統]

  - Attributes:
    - [attribute_name]: [type] 
	// [Attribute 描述]
    - ...

  - Methods:
    - [method_name]([param1]: [type], [param2]: [type]): [ReturnType]
    // [符合描述要求的 Method 描述]
    - ...

## 3. Commit Message Guidelines

`architecture` 資料夾相關的提交訊息應遵循以下規範：

*   **標題格式**：對於新增或修改架構文件的新功能，提交訊息標題應使用 `feat(architecture):` 前綴。
    *   範例：`feat(architecture): Add soldier/pawn movement rules`
*   **其他類型**：對於非功能性變更（例如修正錯字、格式調整），請使用適當的前綴（例如 `fix(architecture):`、`refactor(architecture):` 等）。
```
