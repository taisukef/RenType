#import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class Graphmenu():
    def __init__(self):
        with open('./training_data.dat') as f:
            lines = f.readlines()
            try:
                sum = 0
                X = []
                Y = []
                fig, ax = plt.subplots()
                fig.autofmt_xdate()

                for line in lines[1:]:
                    sum += (int(line.split(' ')[9].replace('\n', '')))
                    if line.split(' ')[3].replace('\n', '') in X:
                        X.pop(-1)
                        Y.pop(-1)
                    X.append(line.split(' ')[0].replace('\n', ""))  # 日付
                    Y.append(sum/24)  # 秒数の合計
                ax.set_xlabel('date')
                ax.set_ylabel('min')
                ax.plot(X, Y)
                ax.grid(which='major', axis='both',
                        color='#999999', linestyle='-.')

                plt.show()
            finally:
                f.close()
