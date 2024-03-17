
# Technical Indicator Visualization

## Introduction

This project was conceived as my final project for a Python programming course focused on financial computations, part of my master's curriculum in 2021. It's primarily an exercise in using Python to visualize technical indicators for stock market data. Technical indicators, as key references for conducting technical analysis on stock prices, should serve as a comprehensive assessment for entering and exiting the stock market. However, the measurement of a single indicator often has its limitations and is particularly prone to losing its predictive power during major events. Therefore, this study aims to explore the predictive capability of technical indicators during the nationwide Level 3 epidemic alert period (May, 2021 - Jul, 2021), to see if any indicator could capture such intense fluctuations in advance.

## About Data

The data used in this study comes from the Taiwan Stock Exchange (TWSE). To avoid selecting stocks with poor financial health, extreme price volatility, and low trading volume, and to ensure a certain degree of industry diversity, I chose the constituents of the Taiwan 50 index as the research subjects. The constituents of the index are adjusted quarterly, and the data used in this report are from the constituents adjusted in June 2021. The data, sourced from TWSE, are daily records including opening price, highest price, lowest price, closing price, price change, and trading volume. The time span of the data covers all trading days from May to July 2021.

## Packages Used

- **NumPy**: Essential for numerical computations, NumPy provides support for working with large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
    
- **Pandas**: Utilized for data manipulation and analysis, pandas offers data structures and operations for manipulating numerical tables and time series. It's particularly useful for handling and cleaning the stock data.
    
- **Matplotlib**: A plotting library that allows for the creation of static, animated, and interactive visualizations in Python. Matplotlib is used here to plot various technical indicators and stock price movements.
    
- **mplfinance**: Built on top of Matplotlib, mplfinance facilitates the plotting of financial data. It simplifies creating candlestick charts, which are crucial for visualizing price movements over time.
    
- **TA-Lib**: Stands for Technical Analysis Library, a Python wrapper for a technical analysis library that provides tools for analyzing financial markets, including indicators and computation of trading strategies. This project uses TA-Lib to calculate various technical indicators like moving averages, MACD, and Bollinger Band.

## Technical Indicators Definition

1. **Candlestick** 
   Candlesticks are price indicators within a specific timeframe, consisting of the highest, opening, closing, and lowest prices. Technical analysis often interprets "Cross" lines as indicators of potential price reversals; "T" lines suggest a resurgence of buying interest, possibly indicating an upward price reversal.
    
2. **Moving Average (MA)** 
   A moving average is an arithmetic line calculated by adding the prices over a certain period and dividing by the frequency of that period. For daily data, a 5MA is the sum of the past five days' closing prices divided by five. Common moving averages for daily data include 5MA (equivalent to a weekly line), 20MA (equivalent to a monthly line), and 60MA (equivalent to a quarterly line). The general belief in technical analysis is that when a long-term moving average crosses over a short-term moving average, it signals a breakout.
    
3. **Moving Average Convergence Divergence (MACD)** 
   MACD utilizes the difference between short-term and long-term EMA (Exponential Moving Average) lines to base its calculations, determining future price movements through the crossover of these lines. The difference between the short-term EMA and long-term EMA is termed "DIF."
   
   - Fast line: Short-term EMA - Long-term EMA = DIF
   - Slow line: EMA of DIF (usually over 9 days)
   - MACD Bar: Fast line - Slow line
   
   A transition from negative to positive MACD values, or when the fast line crosses above the slow line, is known as a "golden cross," considered a buying signal. Conversely, a shift from positive to negative values, or the fast line crossing below the slow line, is known as a "death cross," indicating a selling signal.
    
4. **Stochastic Oscillator (KD)** 
   The KD indicator begins with the calculation of the Raw Stochastic Value (RSV), followed by deriving the K and D values. Incorporating the highest, lowest, and closing prices in its calculations, it's broadly applied in technical analysis.
   
   - RSV = (Today's closing price - Lowest price in the last 9 days) / (Highest price in the last 9 days - Lowest price in the last 9 days) × 100
   - Today's K value = Yesterday's K value × 2/3 + Today's RSV × 1/3
   - Today's D value = Yesterday's D value × 2/3 + Today's K value × 1/3
   
   A golden cross, where the K value crosses above the D value, suggests a buying opportunity; a death cross, where the K value drops below the D value, signals a selling opportunity.
    
5. **Bollinger Bands** 
   Bollinger Bands are created by adding and subtracting a standard deviation (usually two standard deviations) to a specific day's moving average (commonly 10MA or 20MA), forming a band.
   
   - Middle line = Moving average of a specific number of days (usually 10MA or 20MA)
   - Upper line (also known as the resistance line) = Middle line + 2 standard deviations
   - Lower line (also known as the support line) = Middle line - 2 standard deviations

   The width of the Bollinger Bands increases with greater price volatility and decreases when the price volatility is lower. The indicator is used as a signal for potential price reversals when the price touches the upper or lower bands.
    
6. **Average True Range (ATR)** 
   ATR measures price volatility using the highest, lowest, and closing prices, though it does not indicate trend direction. It calculates the True Range (TR) from three price differences, then takes the moving average of these TR values (typically a 14-day MA).
   
   - a = Today's highest price - Today's lowest price
   - b = Today's highest price - Yesterday's closing price
   - c = Today's lowest price - Yesterday's closing price
   - ⟹ TR = max(a, b, c). Taking the moving average of TR yields the ATR
   
   A larger ATR indicates higher recent price volatility, whereas a smaller ATR suggests lower volatility.

## How to Use

After running the `main.py` file, the program first lists the stock codes and their corresponding company names available for analysis (all constituents of the Taiwan 50 index). Users can then enter the stock code they wish to view. Upon pressing enter, if the entered stock code is valid (belongs to the Taiwan 50 index), the program will calculate various technical indicators based on the individual stock's daily data for May, June, and July 2021, stored in the `data` folder, and plot them as separate charts. If the entered stock code is incorrect or does not exist, the program will print an error message and prompt the user to enter another stock code. Typing `exit` will terminate the program.