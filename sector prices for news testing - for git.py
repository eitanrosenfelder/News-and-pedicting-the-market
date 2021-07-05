import pandas as pd
import yfinance as yf

tickers = ["XLE","XLB","XLI","XLY","XLP","XLV","XLF","XLK","VOX","XLU","VNQ"]
df = pd.DataFrame()
for tick in tickers:
  tick_df = yf.download(tickers=tick,start="2006-11-30", end="2019-1-30", interval="1d")["Adj Close"]
  tick_df = tick_df.groupby(pd.Grouper(freq="M")).nth(0)
  tick_df['Date'] = tick_df.index
  df[tick] = tick_df
  df.index = tick_df.index
df.to_csv('C:\\Users\\eitan\\Downloads\\masters\\prices_sectors.csv')