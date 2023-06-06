import tkinter as tk
from tkinter import filedialog

def select_path(is_folder=False):
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを非表示にする

    try:
        if is_folder:
            path = filedialog.askdirectory()  # フォルダを選択するダイアログを表示する
        else:
            path = filedialog.askopenfilename()  # ファイルを選択するダイアログを表示する
        
        # 選択がキャンセルされた場合は空の文字列を返す
        if not path:
            return ""
        
        # 選択されたパスを返す
        return path

    except Exception as e:
        # エラーメッセージを表示してから例外を再スローする
        error_message = f"Error: {e}"
        raise ValueError(error_message)