# GUI用のクラス
import tkinter as tk
from tkinter import ttk
from datetime import timedelta


# メイン画面 生成用のクラス
class Gui(tk.Frame):
    def __init__(self, master, m_title='雛形', size="300x200"):
        super().__init__()

        self.pack()
        master.title(m_title)
        master.geometry(size)


# タブ画面　生成用のクラス
class Gui_tab(tk.Frame):

    def __init__(self, master_notebook, tab_name):
        super().__init__()
        self.tab = ttk.Frame(master_notebook)
        master_notebook.add(self.tab, text=tab_name)
        master_notebook.pack(expand=True, fill='both', padx=0, pady=0)

        self.pack()

    def label_ttk(self, label_name, font):
        label = ttk.Label(self.tab, text=label_name, font=font)
        label.pack()

    def button_ttk(self, button_name, func, x, y, state="normal"):
        button = ttk.Button(self.tab, text=button_name, command=func, state=state)
        button.place(x=x, y=y)


# タブ画面　タイマー部分 生成用のクラス
class Gui_timer(Gui_tab):
    def __init__(self, master_notebook, tab_name):
        super().__init__(master_notebook, tab_name)

        self.label = None
        self.exit_btn = None
        self.reset_btn = None
        self.stop_btn = None
        self.start_btn = None
        self.pack()
        self.tmr = 0
        self.after_id = None

    # タイマー用のラベル
    def label_ttk_timer(self):
        # global label
        self.label = ttk.Label(self.tab, text=timedelta(seconds=0), font=("Times New Roman", 80))
        self.label.pack()

    # Startボタンクリック時の処理
    # クリック時にResetボタンを無効化
    # クリック時にStartボタンを無効化
    def start(self):

        self.start_btn["state"] = "disabled"
        self.stop_btn["state"] = "normal"
        self.reset_btn["state"] = "disabled"

        self.tmr = self.tmr + 1
        self.label["text"] = timedelta(seconds=self.tmr)
        self.after_id = self.tab.after(1000, self.start)


    # Stopボタンクリック時の処理
    # クリック時にResetボタンを有効化
    # クリック時にStartボタンを有効化
    def stop(self):

        self.start_btn["state"] = "normal"
        self.reset_btn["state"] = "normal"

        self.tab.after_cancel(self.after_id)
        self.start_btn["state"] = "normal"
        self.reset_btn["state"] = "normal"

    # Resetボタンクリック時の処理
    def reset(self):
        self.tmr = 0
        self.label["text"] = timedelta(seconds=self.tmr)

    # Startボタン生成のメソッド
    def start_button(self, func, state='normal'):
        self.start_btn = ttk.Button(self.tab, text='Start', command=func, state=state)
        self.start_btn.place(x=50, y=160)

    # Stopボタン生成のメソッド
    def stop_button(self, func, state='disabled'):
        self.stop_btn = ttk.Button(self.tab, text='Stop', command=func, state=state)
        self.stop_btn.place(x=150, y=160)

    # Resetボタン生成のメソッド
    def reset_button(self, func, state='disabled'):
        self.reset_btn = ttk.Button(self.tab, text='Reset', command=func, state=state)
        self.reset_btn.place(x=250, y=160)

    # Exitボタン生成のメソッド
    def exit_button(self, func, state='normal'):
        self.exit_btn = ttk.Button(self.tab, text='Exit', command=func, state=state)
        self.exit_btn.place(x=350, y=160)


def window1():
    # 　メイン画面の生成
    win1 = tk.Tk()
    app = Gui(master=win1, m_title='作業時間記録', size="550x300")

    notebook = ttk.Notebook(win1)

    # 空のタブの生成
    app_tab1 = Gui_timer(master_notebook=notebook, tab_name="作業1")
    app_tab2 = Gui_timer(master_notebook=notebook, tab_name="作業2")
    app_tab3 = Gui_timer(master_notebook=notebook, tab_name="作業3")
    app_tab4 = Gui_timer(master_notebook=notebook, tab_name="作業4")

    # タブ1の画面構成
    app_tab1.label_ttk(label_name="作業1", font=("MS明朝", 25))
    app_tab1.label_ttk_timer()
    app_tab1.start_button(func=app_tab1.start)
    app_tab1.stop_button(func=app_tab1.stop)
    app_tab1.reset_button(func=app_tab1.reset)
    app_tab1.exit_button(func=win1.quit)

    # タブ2の画面構成
    app_tab2.label_ttk(label_name="作業2", font=("MS明朝", 25))
    app_tab2.label_ttk_timer()
    app_tab2.start_button(func=app_tab2.start)
    app_tab2.stop_button(func=app_tab2.stop)
    app_tab2.reset_button(func=app_tab2.reset)
    app_tab2.exit_button(func=win1.quit)

    # タブ3の画面構成
    app_tab3.label_ttk(label_name="作業3", font=("MS明朝", 25))
    app_tab3.label_ttk_timer()
    app_tab3.start_button(func=app_tab3.start)
    app_tab3.stop_button(func=app_tab3.stop)
    app_tab3.reset_button(func=app_tab3.reset)
    app_tab3.exit_button(func=win1.quit)

    # タブ4の画面構成
    app_tab4.label_ttk(label_name="作業4", font=("MS明朝", 25))
    app_tab4.label_ttk_timer()
    app_tab4.start_button(func=app_tab4.start)
    app_tab4.stop_button(func=app_tab4.stop)
    app_tab4.reset_button(func=app_tab4.reset)
    app_tab4.exit_button(func=win1.quit)

    app.mainloop()
