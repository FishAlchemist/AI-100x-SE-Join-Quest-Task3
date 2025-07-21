1. (R) `test_red_moves_the_general_within_the_palace_legal` 測試失敗，原因為 `NotImplementedError`，符合預期。
2. (R) `test_red_moves_the_general_outside_the_palace_illegal` 測試失敗，原因為 `StepDefinitionNotFoundError`，符合預期。
3. (G) 為了讓 `test_red_moves_the_general_outside_the_palace_illegal` 測試通過，在 `General.is_valid_move` 中加入了宮殿邊界檢查。測試通過，1 個測試通過，21 個測試被跳過。
4. (Refactor) `General.is_valid_move` 的程式碼已足夠清晰，無需重構。
5. (Format) 執行 `ruff format` 和 `ruff check`，程式碼被格式化。重新執行測試，所有測試依然通過。
6. (R) `test_generals_face_each_other_on_the_same_file_illegal` 測試失敗，原因為 `StepDefinitionNotFoundError`，符合預期。
7. (G) 經過多次嘗試，終於正確實作了處理 Gherkin data table 的 `given` 步驟。由於先前已完成 `General.is_valid_move` 的邏輯，測試直接通過。1 個測試通過，21 個測試被跳過。
8. (Refactor) 重構了 `General.is_valid_move` 方法，使用生成器表達式來簡化尋找對方將帥的邏輯。測試依然通過。
9. (Format) 執行 `ruff format` 和 `ruff check`，程式碼被格式化。重新執行測試，所有測試依然通過。
10. (R) `test_red_moves_the_guard_diagonally_in_the_palace_legal` 測試失敗，原因為 `StepDefinitionNotFoundError`，符合預期。
11. (G) 實作了 `Guard` 類別及相關的測試步驟，`test_red_moves_the_guard_diagonally_in_the_palace_legal` 測試通過。1 個測試通過，21 個測試被跳過。
12. (Refactor) `Guard.is_valid_move` 的程式碼已足夠清晰，無需重構。
13. (Format) 執行 `ruff format` 和 `ruff check`，程式碼被格式化。重新執行測試，所有測試依然通過。
14. (Plan) 修正開發計畫 workflows/dev_plan.md，使其與日誌 workflows/dev_log.md 的實際進度同步。計畫被錯誤地標示了過多已完成的項目。
