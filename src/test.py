import tkinter

# ==================================
# Applicationオブジェクトクラスの定義
# ==================================

class DesktopApp(tkinter.Frame):

    # ======================================
    # アプリケーションオブジェクト初期設定
    # ======================================
    def __init__(self, window=None):
        super().__init__(window,          # TKオブジェクト
                         width=380,       # フレームサイズ（幅）
                         height=290,      # フレームサイズ（高さ）
                         borderwidth=1,   # 境界線（太さ）
                         relief="groove"  # 境界線（種類）
                         )

        # TKオブジェクト
        self.window = window
        # 位置を指定
        self.pack()
        # サイズ調整
        self.pack_propagate(0)

    # ======================================
    # ウィジェット作成
    # ======================================

    # 後述

# ==================================
# アプリケーション起動
# ==================================

# Wndiow
window = tkinter.Tk()             # TKオブジェクト
window.title("Tkinterアプリ")      # アプリタイトル
window.geometry("400x300")        # 表示画面サイズ（幅x高さ)

# アプリケーションオブジェクト
App = DesktopApp(window=window)   # アプリケーションオブジェクトに指定のWindow設定を渡す
App.mainloop()                    # アプリケーション起動