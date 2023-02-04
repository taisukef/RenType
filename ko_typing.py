import tkinter as tk
import random

import datetime
import time
import ko_word

###### 単語練習用################################
# https://hajimete-program.com/blog/2018/07/10/python3tkinterでタイピングゲームを作ってみました%E3%80%82/
# https://zenn.dev/takahashi_m/articles/a272cea4c3c4d7bb29e5
# https://daeudaeu.com/typing-appli/
# https://github.com/Filbert-code/Typing-Test-Application/blob/main/MainFrame.py


# 打って欲しいキーと四角形を連動させるには

# 時間記録
# https://note.nkmk.me/python-datetime-now-today/ 参考
# https://magazine.techacademy.jp/magazine/18884 参考


class Practice4():
    def __init__(self):
        self.master = tk.Tk()
        # self.master = master
        self.master.title("rentype")
        self.master.geometry("1280x800")

        global canvas, text1, label1, label2, t_start, word, words, mojicount, count

        # メインフレームの作成と設置
        frame_app = tk.Frame(self.master)
        frame_app.pack()

        canvas = tk.Canvas(self.master, width=1280, height=800, bg="gray")
        canvas.pack()

        # list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        list2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        list3 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';']
        list4 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

        # ----------------1段目-----------------------------------------------------
        # x1 = 100
        # y1 = 160
        # x2 = 190
        # y2 = 250
        # i = 10

        # z = 145
        # w = 205
        # c = 0

        # canvas.create_rectangle(
        #    100, 160, 190, 250, outline="black", fill="gray", tag="1")
        # canvas.create_rectangle(
        #    200, 160, 290, 250, outline="black", fill="gray", tag="2")
        # canvas.create_rectangle(
        #    300, 160, 390, 250, outline="black", fill="gray", tag="3")
        # canvas.create_rectangle(
        #    400, 160, 490, 250, outline="black", fill="gray", tag="4")
        # canvas.create_rectangle(
        #    500, 160, 590, 250, outline="black", fill="gray", tag="5")
        # canvas.create_rectangle(
        #    600, 160, 690, 250, outline="black", fill="gray", tag="6")
        # canvas.create_rectangle(
        #    700, 160, 790, 250, outline="black", fill="gray", tag="7")
        # canvas.create_rectangle(
        #    800, 160, 890, 250, outline="black", fill="gray", tag="8")
        # canvas.create_rectangle(
        #    900, 160, 990, 250, outline="black", fill="gray", tag="9")
        # canvas.create_rectangle(
        #    1000, 160, 1090, 250, outline="black", fill="gray", tag="zero")
        # x1 += 100
        # x2 += 100

        # while i > 0:
        #    canvas.create_text(
        #        z, w, text=list1[c], fill="black", font=("Times", 35))
        #    z += 100
        #    c += 1
        #    i -= 1

        # -------------------------2段目---------------------------------------
        # x1 = 145
        # y1 = 260
        # x2 = 235
        # y2 = 350
        j = 10

        z = 190
        w = 305
        c = 0

        canvas.create_rectangle(
            145, 260, 235, 350, outline="black", fill="gray", tag="q")
        canvas.create_rectangle(
            245, 260, 335, 350, outline="black", fill="gray", tag="w")
        canvas.create_rectangle(
            345, 260, 435, 350, outline="black", fill="gray", tag="e")
        canvas.create_rectangle(
            445, 260, 535, 350, outline="black", fill="gray", tag="r")
        canvas.create_rectangle(
            545, 260, 635, 350, outline="black", fill="gray", tag="t")
        canvas.create_rectangle(
            645, 260, 735, 350, outline="black", fill="gray", tag="y")
        canvas.create_rectangle(
            745, 260, 835, 350, outline="black", fill="gray", tag="u")
        canvas.create_rectangle(
            845, 260, 935, 350, outline="black", fill="gray", tag="i")
        canvas.create_rectangle(
            945, 260, 1035, 350, outline="black", fill="gray", tag="o")
        canvas.create_rectangle(
            1045, 260, 1135, 350, outline="black", fill="gray", tag="p")
        # x1 += 100
        # x2 += 100
        while j > 0:
            canvas.create_text(
                z, w, text=list2[c], fill="black", font=("Times", 35))
            z += 100
            c += 1
            j -= 1

        # ------------3段目------------------------------------------------------
        # x1 = 170
        # y1 = 360
        # x2 = 260
        # y2 = 450
        k = 10

        z = 215
        w = 405
        c = 0

        canvas.create_rectangle(
            170, 360, 260, 450, outline="black", fill="gray", tag="a")
        canvas.create_rectangle(
            270, 360, 360, 450, outline="black", fill="gray", tag="s")
        canvas.create_rectangle(
            370, 360, 460, 450, outline="black", fill="gray", tag="d")
        canvas.create_rectangle(
            470, 360, 560, 450, outline="black", fill="gray", tag="f")
        canvas.create_rectangle(
            570, 360, 660, 450, outline="black", fill="gray", tag="g")
        canvas.create_rectangle(
            670, 360, 760, 450, outline="black", fill="gray", tag="h")
        canvas.create_rectangle(
            770, 360, 860, 450, outline="black", fill="gray", tag="j")
        canvas.create_rectangle(
            870, 360, 960, 450, outline="black", fill="gray", tag="k")
        canvas.create_rectangle(
            970, 360, 1060, 450, outline="black", fill="gray", tag="l")
        canvas.create_rectangle(
            1070, 360, 1160, 450, outline="black", fill="gray", tag=";")

        # x1 += 100
        # x2 += 100
        while k > 0:
            canvas.create_text(
                z, w, text=list3[c], fill="black", font=("Times", 35))
            z += 100
            c += 1
            k -= 1

        # -----------4段目---------------------------------------------------------
        x1 = 220
        y1 = 460
        x2 = 310
        y2 = 550
        l = 10

        z = 265
        w = 505
        c = 0

        canvas.create_rectangle(
            220, 460, 310, 550, outline="black", fill="gray", tag="z")
        canvas.create_rectangle(
            320, 460, 410, 550, outline="black", fill="gray", tag="x")
        canvas.create_rectangle(
            420, 460, 510, 550, outline="black", fill="gray", tag="c")
        canvas.create_rectangle(
            520, 460, 610, 550, outline="black", fill="gray", tag="v")
        canvas.create_rectangle(
            620, 460, 710, 550, outline="black", fill="gray", tag="b")
        canvas.create_rectangle(
            720, 460, 810, 550, outline="black", fill="gray", tag="n")
        canvas.create_rectangle(
            820, 460, 910, 550, outline="black", fill="gray", tag="m")
        canvas.create_rectangle(
            920, 460, 1010, 550, outline="black", fill="gray", tag=",")
        canvas.create_rectangle(
            1020, 460, 1110, 550, outline="black", fill="gray", tag=".")
        canvas.create_rectangle(
            1120, 460, 1210, 550, outline="black", fill="gray", tag="/")
        canvas.create_rectangle(
            430, 560, 900, 600, outline="black", fill="gray", tag="space")

        # x1 += 100
        # x2 += 100

        while l > 0:
            canvas.create_text(
                z, w, text=list4[c], fill="black", font=("Times", 35))
            z += 100
            c += 1
            l -= 1

        # ----------------------左手------------------------------------------------------

        # 指腹
        a1 = 230
        b1 = 670
        a2 = 300
        b2 = 800

        m = 4

        # 指先
        # c1 = 230
        # d1 = 620
        # c2 = 300
        # d2 = 670
        canvas.create_rectangle(
            230, 620, 300, 670, outline="white", fill="white", tag="Lko")
        canvas.create_rectangle(
            310, 620, 380, 670, outline="white", fill="white", tag="Lkusuri")
        canvas.create_rectangle(
            390, 620, 460, 670, outline="white", fill="white", tag="Lnaka")
        canvas.create_rectangle(
            470, 620, 540, 670, outline="white", fill="white", tag="Lhito")
        canvas.create_rectangle(
            550, 670, 620, 720, outline="white", fill="white", tag="Loya")
        canvas.create_rectangle(
            550, 720, 620, 800, outline="white", fill="white")
        while m > 0:
            canvas.create_rectangle(
                a1, b1, a2, b2, outline="white", fill="white")
            a1 += 80
            a2 += 80
            # c1 += 80
            # c2 += 80
            m -= 1

        # ----------------------右手------------------------------------------------------

        # 指腹
        a1 = 780
        b1 = 670
        a2 = 850
        b2 = 800

        n = 4

        # 指先
        # c1 = 700
        # d1 = 620
        # c2 = 770
        # d2 = 670

        canvas.create_rectangle(
            700, 720, 770, 800, outline="white", fill="white")
        canvas.create_rectangle(
            700, 670, 770, 720, outline="white", fill="white", tag="Roya")
        canvas.create_rectangle(
            780, 620, 850, 670, outline="white", fill="white", tag="Rhito")
        canvas.create_rectangle(
            860, 620, 930, 670, outline="white", fill="white", tag="Rnaka")
        canvas.create_rectangle(
            940, 620, 1010, 670, outline="white", fill="white", tag="Rkusuri")
        canvas.create_rectangle(
            1020, 620, 1090, 670, outline="white", fill="white", tag="Rko")

        while n > 0:
            canvas.create_rectangle(
                a1, b1, a2, b2, outline="white", fill="white")
            a1 += 80
            a2 += 80
            # c1 += 80
            # c2 += 80
            n -= 1

        words = ko_word.word1
        word = None
        count = 0
        mojicount = 0
        word = self.choise(words)

        # WPM / Words Per Minute

        self.back_button = tk.Button(self.master, text="終了", font=(
            "Times", 20), command=self.end)
        self.back_button.place(x=100, y=80)

        text1 = canvas.create_text(  # HajimeteProgramさんのプログラム
            640, 55,  # 座標 (0,0) から描画
            anchor=tk.N,  # 上寄せ
            # 描画する文字は "タイピング文字"
            text=f"{word}",
            font=("", 60, "bold"),
            fill="white",
        )

        # -------単語数-----------------------------------
        label = tk.Label(
            self.master,
            text="単語数:",
            font=("", 25),
            bg="gray"
        )
        label.place(x=1050, y=45)

        label2 = tk.Label(
            self.master,
            text=mojicount,
            font=("", 25),
            bg="gray"
        )
        label2.place(x=1200, y=45)
        # -------ミスカウント-----------------------------------
        self.label = tk.Label(
            self.master,
            text="ミスカウント:",
            font=("", 25),
            bg="gray"
        )
        self.label.place(x=1050, y=75)

        label1 = tk.Label(
            self.master,
            text=count,
            font=("", 25),
            bg="gray"
        )
        label1.place(x=1200, y=75)

        t_start = time.time()
        self.keybind()
        canvas.bind("<Key>", self.keypush)
        canvas.focus_set()  # HajimeteProgramさんのプログラム

        self.master.mainloop()

    def choise(self, words):  # HajimeteProgramさんのプログラム
        global mojicount
        mojicount += 1
        max = len(words) - 1
        rnd = random.randint(0, max)
        return words[rnd]

    def keypush(self, event):
        global word
        key = event.char
        if word[0] == key:  # 押した時の処理　## HajimeteProgramさんのプログラム
            word = word[1:]
            self.delete()
            if len(word) == 0:
                word = self.choise(words)
                label2.config(text=mojicount)

        else:
            self.colorwarning()

        self.kurikaesi()

    def keybind(self):
        global word

        if word[0] == "q":
            canvas.itemconfig("q", fill="pink")
            canvas.itemconfig("Lko", fill="pink")
        elif word[0] == "w":
            canvas.itemconfig("w", fill="pink")
            canvas.itemconfig("Lkusuri", fill="pink")
        elif word[0] == "e":
            canvas.itemconfig("e", fill="pink")
            canvas.itemconfig("Lnaka", fill="pink")
        elif word[0] == "r":
            canvas.itemconfig("r", fill="pink")
            canvas.itemconfig("Lhito", fill="pink")
        elif word[0] == "t":
            canvas.itemconfig("t", fill="pink")
            canvas.itemconfig("Lhito", fill="pink")
        elif word[0] == "y":
            canvas.itemconfig("y", fill="pink")
            canvas.itemconfig("Rhito", fill="pink")
        elif word[0] == "u":
            canvas.itemconfig("u", fill="pink")
            canvas.itemconfig("Rhito", fill="pink")
        elif word[0] == "i":
            canvas.itemconfig("i", fill="pink")
            canvas.itemconfig("Rnaka", fill="pink")
        elif word[0] == "o":
            canvas.itemconfig("o", fill="pink")
            canvas.itemconfig("Rkusuri", fill="pink")
        elif word[0] == "p":
            canvas.itemconfig("p", fill="pink")
            canvas.itemconfig("Rko", fill="pink")
        elif word[0] == "a":
            canvas.itemconfig("a", fill="pink")
            canvas.itemconfig("Lko", fill="pink")
        elif word[0] == "s":
            canvas.itemconfig("s", fill="pink")
            canvas.itemconfig("Lkusuri", fill="pink")
        elif word[0] == "d":
            canvas.itemconfig("d", fill="pink")
            canvas.itemconfig("Lnaka", fill="pink")
        elif word[0] == "f":
            canvas.itemconfig("f", fill="pink")
            canvas.itemconfig("Lhito", fill="pink")
        elif word[0] == "g":
            canvas.itemconfig("g", fill="pink")
            canvas.itemconfig("Lhito", fill="pink")
        elif word[0] == "h":
            canvas.itemconfig("h", fill="pink")
            canvas.itemconfig("Rhito", fill="pink")
        elif word[0] == "j":
            canvas.itemconfig("j", fill="pink")
            canvas.itemconfig("Rhito", fill="pink")
        elif word[0] == "k":
            canvas.itemconfig("k", fill="pink")
            canvas.itemconfig("Rnaka", fill="pink")
        elif word[0] == "l":
            canvas.itemconfig("l", fill="pink")
            canvas.itemconfig("Rkusuri", fill="pink")
        elif word[0] == ";":
            canvas.itemconfig(";", fill="pink")
            canvas.itemconfig("Rko", fill="pink")
        elif word[0] == "z":
            canvas.itemconfig("z", fill="pink")
            canvas.itemconfig("Lko", fill="pink")
        elif word[0] == "x":
            canvas.itemconfig("x", fill="pink")
            canvas.itemconfig("Lkusuri", fill="pink")
        elif word[0] == "c":
            canvas.itemconfig("c", fill="pink")
            canvas.itemconfig("Lnaka", fill="pink")
        elif word[0] == "v":
            canvas.itemconfig("v", fill="pink")
            canvas.itemconfig("Lhito", fill="pink")
        elif word[0] == "b":
            canvas.itemconfig("b", fill="pink")
            canvas.itemconfig("Lhito", fill="pink")
        elif word[0] == "n":
            canvas.itemconfig("n", fill="pink")
            canvas.itemconfig("Rhito", fill="pink")
        elif word[0] == "m":
            canvas.itemconfig("m", fill="pink")
            canvas.itemconfig("Rhito", fill="pink")
        elif word[0] == ",":
            canvas.itemconfig(",", fill="pink")
            canvas.itemconfig("Rnaka", fill="pink")
        elif word[0] == ".":
            canvas.itemconfig(".", fill="pink")
            canvas.itemconfig("Rkusuri", fill="pink")
        elif word[0] == "/":
            canvas.itemconfig("/", fill="pink")
            canvas.itemconfig("Rko", fill="pink")
        elif word[0] == " ":
            canvas.itemconfig("space", fill="pink")
            canvas.itemconfig("Loya", fill="pink")
            canvas.itemconfig("Roya", fill="pink")
        else:
            return

    def delete(self):
        canvas.itemconfig("1", fill="gray")
        canvas.itemconfig("2", fill="gray")
        canvas.itemconfig("3", fill="gray")
        canvas.itemconfig("4", fill="gray")
        canvas.itemconfig("5", fill="gray")
        canvas.itemconfig("6", fill="gray")
        canvas.itemconfig("7", fill="gray")
        canvas.itemconfig("8", fill="gray")
        canvas.itemconfig("9", fill="gray")
        canvas.itemconfig("zero", fill="gray")
        canvas.itemconfig("q", fill="gray")
        canvas.itemconfig("w", fill="gray")
        canvas.itemconfig("e", fill="gray")
        canvas.itemconfig("r", fill="gray")
        canvas.itemconfig("t", fill="gray")
        canvas.itemconfig("y", fill="gray")
        canvas.itemconfig("u", fill="gray")
        canvas.itemconfig("i", fill="gray")
        canvas.itemconfig("o", fill="gray")
        canvas.itemconfig("p", fill="gray")
        canvas.itemconfig("a", fill="gray")
        canvas.itemconfig("s", fill="gray")
        canvas.itemconfig("d", fill="gray")
        canvas.itemconfig("f", fill="gray")
        canvas.itemconfig("g", fill="gray")
        canvas.itemconfig("h", fill="gray")
        canvas.itemconfig("j", fill="gray")
        canvas.itemconfig("k", fill="gray")
        canvas.itemconfig("l", fill="gray")
        canvas.itemconfig(";", fill="gray")
        canvas.itemconfig("z", fill="gray")
        canvas.itemconfig("x", fill="gray")
        canvas.itemconfig("c", fill="gray")
        canvas.itemconfig("v", fill="gray")
        canvas.itemconfig("b", fill="gray")
        canvas.itemconfig("n", fill="gray")
        canvas.itemconfig("m", fill="gray")
        canvas.itemconfig(",", fill="gray")
        canvas.itemconfig(".", fill="gray")
        canvas.itemconfig("/", fill="gray")
        canvas.itemconfig("space", fill="gray")
        canvas.itemconfig("Lko", fill="white")
        canvas.itemconfig("Lkusuri", fill="white")
        canvas.itemconfig("Lnaka", fill="white")
        canvas.itemconfig("Lhito", fill="white")
        canvas.itemconfig("Loya", fill="white")
        canvas.itemconfig("Roya", fill="white")
        canvas.itemconfig("Rhito", fill="white")
        canvas.itemconfig("Rnaka", fill="white")
        canvas.itemconfig("Rkusuri", fill="white")
        canvas.itemconfig("Rko", fill="white")

    def colorwarning(self):  # daeuさんのプログラム
        global count
        count += 1
        label1.config(text=count)  # misstype カウント
        canvas.itemconfig(text1, fill="red")
        self.master.after(200, self.colorNormal)

    def colorNormal(self):  # daeuさんのプログラム
        canvas.itemconfig(text1, fill="white")

    def kurikaesi(self):  # HajimeteProgramさんのプログラムを参照
        self.keybind()
        canvas.itemconfig(text1, text=f"{word}")

    def end(self):
        # 時間記録
        # https://note.nkmk.me/python-datetime-now-today/ 参考
        # https://magazine.techacademy.jp/magazine/18884 参考
        nowtime = datetime.datetime.now()
        t_end = time.time()
        t_result = int(t_end - t_start)
        with open('training_data.dat', 'a')as f:
            print(nowtime, '', nowtime.day, '', mojicount,
                  '', count, '', t_result, file=f)

        self.master.destroy()


if __name__ == "__main__":
    # root = tk.Tk()
    Practice4()
    # root.mainloop()
