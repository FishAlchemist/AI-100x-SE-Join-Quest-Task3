# 開發計畫

## 已完成的測試場景

### General 將

- [x] **Scenario: Red moves the General within the palace (Legal)** (日誌 #1-5)
- [x] **Scenario: Red moves the General outside the palace (Illegal)** (日誌 #2-5)
- [x] **Scenario: Generals face each other on the same file (Illegal)** (日誌 #6-9)

### Guard 士

- [x] **Scenario: Red moves the Guard diagonally in the palace (Legal)** (日誌 #10-13)
- [x] **Scenario: Red moves the Guard straight (Illegal)** (日誌 #17-23)

### Rook 車

- [x] **Scenario: Red moves the Rook along a clear rank (Legal)** (日誌 #26-29)
- [x] **Scenario: Red moves the Rook and attempts to jump over a piece (Illegal)** (日誌 #30-32)

### Horse 馬

- [x] **Scenario: Red moves the Horse in an "L" shape with no block (Legal)** (日誌 #33-38)
- [x] **Scenario: Red moves the Horse and it is blocked by an adjacent piece (Illegal)** (日誌 #36-38)

### Cannon 砲

- [x] **Scenario: Red moves the Cannon like a Rook with an empty path (Legal)** (日誌 #41-44)
- [x] **Scenario: Red moves the Cannon and jumps exactly one screen to capture (Legal)** (日誌 #41-44)
- [x] **Scenario: Red moves the Cannon and tries to jump with zero screens (Illegal)** (日誌 #41-44)
- [x] **Scenario: Red moves the Cannon and tries to jump with more than one screen (Illegal)** (日誌 #41-44)

### Elephant 象

- [x] **Scenario: Red moves the Elephant 2-step diagonal with a clear midpoint (Legal)** (日誌 #47-50)
- [x] **Scenario: Red moves the Elephant and tries to cross the river (Illegal)** (日誌 #51)
- [x] **Scenario: Red moves the Elephant and its midpoint is blocked (Illegal)** (日誌 #52)

### Soldier 兵

- [x] **Scenario: Red moves the Soldier forward before crossing the river (Legal)** (日誌 #54-55)
- [x] **Scenario: Red moves the Soldier and tries to move sideways before crossing (Illegal)** (日誌 #54-55)
- [x] **Scenario: Red moves the Soldier sideways after crossing the river (Legal)** (日誌 #54-56)
- [x] **Scenario: Red moves the Soldier and attempts to move backward after crossing (Illegal)** (日誌 #54-56)

### Game Rules 遊戲規則

- [x] **Scenario: Red captures opponent's General and wins immediately (Legal)** (日誌 #57-60)
- [x] **Scenario: Red captures a non-General piece and the game continues (Legal)** (日誌 #57-60)

## 所有測試場景都已完成
- [ ] **Scenario: Red captures a non-General piece and the game continues (Legal)** (日誌 #57)
