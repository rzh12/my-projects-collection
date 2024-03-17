import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from talib import abstract
from final import FN  # Import the FN module containing functions for fetching and processing stock data

# Set NumPy print options to suppress scientific notation for small numbers
np.set_printoptions(suppress=True)

# Load available stock codes, here are the constituents of 0050
indices = {}
with open('./data/0050.txt', encoding='UTF-8') as f:
    for line in f:
        (key, val) = line.split()
        indices[key] = val

print("資料庫所涵蓋的範圍為台灣50中的個股：", indices)
print("請輸入要檢視的股票代碼")
# Initialize a loop control variable
a = True
while a:
    id = str(input())
    if id in indices:
        # Plot the candlestick chart
        Kbar = FN.GetData(id)

        fig = plt.figure(1)
        ax1 = fig.add_subplot(111)
        plt.title("KBar")
        plt.xlabel("Day_N (May,2021 - Jul,2021)")
        plt.ylabel("Price")
        candlestick_ohlc(ax1, Kbar, width=0.7, colorup='r', colordown='g')

        # Plot 5MA, 10MA, 20MA
        TaKbar = FN.GetTaKbar(id)
        print(type(TaKbar))
        print('5MA:\n', abstract.MA(TaKbar, timeperiod=5))
        print('10MA:\n', abstract.MA(TaKbar, timeperiod=10))
        print('20MA:\n', abstract.MA(TaKbar, timeperiod=20))

        fig = plt.figure(2)
        ax2 = fig.add_subplot(111)
        day_MA = list(range(1, 65))
        plt.title("Moving Average")
        plt.xlabel("Day_N (May,2021 - Jul,2021)")
        plt.ylabel("Price")
        ax2.plot(day_MA, abstract.MA(TaKbar, timeperiod=5), 'm-', label='5MA')
        ax2.plot(day_MA, abstract.MA(TaKbar, timeperiod=10), 'c-', label='10MA')
        ax2.plot(day_MA, abstract.MA(TaKbar, timeperiod=20), 'y-', label='20MA')
        ax2.legend()

        # Plot MACD (Fast Line, Slow Line, MACD Bar)
        fast, slow, bar = abstract.MACD(TaKbar, fastperiod=12, slowperiod=26, singleperiod=9)
        print('快線:\n', fast)
        print('慢線:\n', slow)
        print('MACD柱:\n', bar)

        fig = plt.figure(3)
        ax3 = fig.add_subplot(111)
        day_minus1 = list(range(0, 64))
        plt.title("MACD")
        plt.xlabel("Day_N (May,2021 - Jul,2021)")
        plt.ylabel("Difference")
        ax3.plot(fast, 'r-', label='FAST')
        ax3.plot(slow, 'g-', label='SLOW')
        plt.bar(day_minus1, bar)
        ax3.legend()

        # Plot KD (K , D )
        K, D = abstract.STOCH(TaKbar)
        print('K值:\n', K)
        print('D值:\n', D)

        fig = plt.figure(4)
        ax4 = fig.add_subplot(111)
        plt.title("KD")
        plt.xlabel("Day_N (May,2021 - Jul,2021)")
        plt.ylabel("KD value")
        ax4.plot(K, 'r-', label='K')
        ax4.plot(D, 'g-', label='D')
        ax4.legend()

        # Plot Bollinger Band (one for 10MA, one for 20MA)
        Up_10, Mid_10, Down_10 = abstract.BBANDS(TaKbar, timeperiod=10, nbdevup=2., nbdevdn=2., matype=0)
        Up_20, Mid_20, Down_20 = abstract.BBANDS(TaKbar, timeperiod=20, nbdevup=2., nbdevdn=2., matype=0)

        fig = plt.figure(5)
        ax5 = fig.add_subplot(111)
        plt.title("Bollinger Bands")
        plt.xlabel("Day_N (May,2021 - Jul,2021)")
        plt.ylabel("Price")
        ax5.plot(Mid_10, 'r-', label='Mid_t=10')
        ax5.plot(Up_10, color='m', ls='-.', label='Up_t=10')
        ax5.plot(Down_10, color='m', ls='-.', label='Down_t=10')
        ax5.plot(Up_20, color='c', ls='-.', label='Up_t=20')
        ax5.plot(Down_20, color='c', ls='-.', label='Down_t=20')
        ax5.legend()

        # Plot ATR
        atr = abstract.ATR(TaKbar, timeperiod=14)
        print('ATR為:\n', atr)

        fig = plt.figure(6)
        ax6 = fig.add_subplot(111)
        plt.title("ATR")
        plt.xlabel("Day_N (May,2021 - Jul,2021)")
        plt.ylabel("ATR")
        ax6.plot(atr, 'r-')

        plt.show()

        a = False

    elif id == 'exit':
        a = False

    else:
        print("股票代碼不存在資料庫")
        print("輸入其他股票代碼，或輸入exit以結束")

