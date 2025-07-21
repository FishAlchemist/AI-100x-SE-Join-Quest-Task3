# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import os
import sys

def read_content_from_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"讀取檔案 {file_path} 時發生錯誤：{e}")
        sys.exit(1)

def append_log(log_file_path: str, log_content: str):
    # 將相對路徑轉換為絕對路徑
    absolute_log_file_path = os.path.abspath(log_file_path)
    
    # 確保 workflows 目錄存在
    os.makedirs(os.path.dirname(absolute_log_file_path), exist_ok=True)

    current_line_number = 0
    if os.path.exists(absolute_log_file_path):
        with open(absolute_log_file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():  # 檢查是否為空行
                    try:
                        # 嘗試從行首解析行號
                        parts = line.strip().split('.', 1)
                        if len(parts) > 1 and parts[0].isdigit():
                            current_line_number = int(parts[0])
                    except ValueError:
                        continue # 如果解析失敗，跳過此行

    new_line_number = current_line_number + 1
    
    with open(absolute_log_file_path, 'a', encoding='utf-8') as f:
        f.write(f"{new_line_number}. {log_content}\n")
    
    print(f"日誌已追加到 {log_file_path}，新行號為 {new_line_number}")

def main():
    if len(sys.argv) > 2:
        log_file_path = sys.argv[1]
        log_message_arg = sys.argv[2]
        
        if log_message_arg.startswith('@'):
            content_file_path = log_message_arg[1:]
            log_message = read_content_from_file(content_file_path)
        else:
            log_message = log_message_arg

        append_log(log_file_path, log_message)
    else:
        print("請提供日誌檔案路徑和日誌內容（或以@開頭的檔案路徑）作為參數。例如：")
        print("uv run --script script/append_log.py workflows/dev_log.md \"這是我的日誌內容\"")
        print("uv run --script script/append_log.py workflows/dev_log.md @temp_log.txt")

if __name__ == "__main__":
    main()
