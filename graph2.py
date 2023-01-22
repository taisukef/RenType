# import tkinter as tk
import matplotlib.pyplot as plt


class Graphmenu2():
    def __init__(self):
        with open('./test_data.dat') as f:
            lines = f.readlines()
            try:
                a = 0
                min = 100
                X = []
                Y = []
                fig, ax = plt.subplots()
                fig.autofmt_xdate()

                for line in lines[1:]:
                    a = (int(line.split(' ')[5].replace('\n', '')))
                    if a < min:
                        min = a

                    if line.split(' ')[3].replace('\n', '') in X:
                        X.pop(-1)
                        Y.pop(-1)
                    if line.split(' ')[5].replace('\n', '') in Y:
                        X.pop(-1)
                        Y.pop(-1)
                    X.append(line.split(' ')[0].replace('\n', ''))  # 日付
                    plt.xticks(rotation=90)
                    Y.append(min)

                ax.set_xlabel('date')
                ax.set_ylabel('sec')
                ax.plot(X, Y)
                ax.grid(which='major', axis='both',
                        color='#999999', linestyle='-.')

                plt.show()
            finally:
                f.close()
