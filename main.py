import tkinter as tk
from tkinter import *
import sys
from hito_typing import Practice1  # 練習
from naka_typing import Practice2  # 練習
from kusuri_typing import Practice3  # 練習
from ko_typing import Practice4  # 練習
from zen_typing import Practice5  # 練習
from eng_typing import Practice6  # 練習
from typingapp_test import Test_key  # テスト
from graph import Graphmenu  # グラフ
from graph2 import Graphmenu2  # グラフ(test)


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("rentype")
        self.master.geometry("500x600")
        self.main()

    def main(self):
        for i in self.master.winfo_children():  # ボタンが増殖するのを防ぐ処理
            i.destroy()
        self.frame1 = tk.Frame(self.master, width=500, height=600)
        self.frame1.pack()

        self.label1 = tk.Label(
            self.frame1, text="・・rentype・・", font=("Times", 30))
        self.label1.pack(pady=10)

        self.button1 = tk.Button(
            self.frame1, text="1: ポジション練習", command=self.next)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame1, text="2: 単語練習", command=self.next2)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame1, text="3: テスト", command=self.next3)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame1, text="4: 成績", command=self.next4)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame1, text="5: 終了", command=sys.exit)
        self.button1.pack(pady=20)  # ウィジェットの配置

    def next(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=500, height=600)
        self.frame2.pack()

        self.label1 = tk.Label(
            self.frame2, text="・・ポジション練習・・", font=("Times", 20))
        self.label1.pack(pady=10)

        self.button1 = tk.Button(
            self.frame2, text="1: 人さし指", command=Practice1)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame2, text="2: 中指", command=Practice2)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame2, text="3: 薬指", command=Practice3)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame2, text="4: 小指", command=Practice4)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame2, text="5: 全般", command=Practice5)
        self.button1.pack(pady=20)

        self.login_btn = tk.Button(
            self.frame2, text="6: 戻る", command=self.main)
        self.login_btn.pack(pady=20)  # ウィジェットの配置

    def next2(self):
        for i in self.master.winfo_children():  # ボタンが増殖するのを防ぐ処理
            i.destroy()
        self.frame4 = Frame(self.master, width=1280, height=800)
        self.frame4.pack()

        self.label1 = tk.Label(
            self.frame4, text="・・単語練習・・", font=("Times", 30))
        self.label1.pack(pady=10)

        self.button1 = tk.Button(
            self.frame4, text="1: 単語", command=Practice6)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame4, text="2: 戻る", command=self.main)
        self.button1.pack(pady=20)  # ウィジェットの配置

    def next3(self):
        for i in self.master.winfo_children():  # ボタンが増殖するのを防ぐ処理
            i.destroy()
        self.frame8 = Frame(self.master, width=500, height=600)
        self.frame8.pack()

        self.label1 = tk.Label(
            self.frame8, text="・・テスト・・", font=("Times", 20))
        self.label1.pack(pady=10)

        self.button1 = tk.Button(
            self.frame8, text="1: 英単語", command=Test_key)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame8, text="2: 戻る", command=self.main)
        self.button1.pack(pady=20)  # ウィジェットの配置

    def next4(self):
        for i in self.master.winfo_children():  # ボタンが増殖するのを防ぐ処理
            i.destroy()
        self.frame10 = Frame(self.master, width=500, height=600)
        self.frame10.pack()

        self.label1 = tk.Label(
            self.frame10, text="・・成績・・", font=("Times", 20))
        self.label1.pack(pady=10)

        self.button1 = tk.Button(
            self.frame10, text="1: グラフ(practice)", command=Graphmenu)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame10, text="2: グラフ(test)", command=Graphmenu2)
        self.button1.pack(pady=20)  # ウィジェットの配置

        self.button1 = tk.Button(
            self.frame10, text="3:戻る", command=self.main)
        self.button1.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
