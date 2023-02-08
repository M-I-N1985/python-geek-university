import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.candlestick_ohlc import candlestick_ohlc
from talib import BBANDS, MACD


def plot_candlestick_bollinger_macd(symbol, start, end):
    df = pdr.DataReader(symbol, 'yahoo', start, end)
    df['21d_upper'], df['21d_middle'], df['21d_lower'] = BBANDS(df['Close'], timeperiod=21)
    df['macd'], df['macd_signal'], df['macd_hist'] = MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df = df.dropna()

    fig, ax = plt.subplots()
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    candle_data = [tuple([mdates.date2num(d), o, c, h, l]) for d, o, h, l, c in
                   zip(df.index, df['Open'], df['High'], df['Low'], df['Close'])]

    color = 'g'
    for i, (d, o, c, h, l) in enumerate(candle_data):
        if i > 0:
            prev_c = candle_data[i - 1][2]
            if c < prev_c:
                color = 'r'
            else:
                color = 'g'
        if c < df.loc[df.index[i], '21d_lower'] and df.loc[df.index[i], 'macd'] > df.loc[df.index[i], 'macd_signal']:
            color = 'r'
            width = 2.0
        else:
            width = 0.5
        candlestick_ohlc(ax, [(d, o, c, h, l)], colorup=color, width=width)

    ax.plot(df.index, df['21d_upper'], 'b-')
    ax.plot(df.index, df['21d_middle'], 'b-')
    ax.plot(df.index, df['21d_lower'], 'b-')
    ax.plot(df.index, df['macd'], 'k-')
    ax.plot(df.index, df['macd_signal'], 'r-')

    plt.show()


plot_candlestick_bollinger_macd('PETR4.SA', '2010-01-01', '2022-12-31')
