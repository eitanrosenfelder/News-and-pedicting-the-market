import yfinance as yf
import pandas as pd
df = pd.read_pickle('C:\\Users\\eitan\\Downloads\\masters\\scores_for_all.pkl', compression='xz', storage_options=None)


df["index"] = df.index
start = "2006-10-01"
end = "2020-12-01"
prepared_data_x_y = df

sectors = ["XLE","XLB","XLI","XLY","XLP","XLV","XLF","XLK","VOX","XLU","VNQ"]
for s in range(0,len(sectors)):
    sector = str(sectors[s])
    df_sector = pd.DataFrame(yf.download(tickers=sector, start=start, end=end, interval="1d"))
    df_sector = df_sector.groupby(pd.Grouper(freq="M")).nth(0)
    df_sector = df_sector["Adj Close"]
    df_sector = pd.DataFrame(df_sector.pct_change().shift(-1))
    df_sector["index"] = df_sector.index
    df_sector.columns = [str(sector+" change"), "index"]
    print(df_sector.shape)
    prepared_data_x_y = pd.merge(prepared_data_x_y, df_sector, on="index", how='inner')
    prepared_data_x_y = prepared_data_x_y.set_index("index")
    sector = prepared_data_x_y[str(sector+" change")]

prepared_data_x_y.to_pickle(r'C:\\Users\\eitan\\Downloads\\masters\\x_y_cnbc.pkl', compression='xz')