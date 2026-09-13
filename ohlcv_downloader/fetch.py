import yfinance as yf

# extracting data from yfinance by utilizing the given conditions 

btc = yf.download('BTC-USD', start='2025-01-01', end='2026-01-01')
btc.to_csv('/home/priyansh/Documents/d/learning_python/ohlcv_downloader/db/btc_test.csv')
# print(btc.info())
# print("\n")
# print(btc.head(5))
# print(btc.index)
print(btc.columns)

# using the above, we find that there are 6 columns in total titled: 
# Price, Close, High, Low, Open, Volume 
# further: the top 2 rows are non-functional as they just have BTC-USD values repeated all over 
# with the exception of the price column which is actually not price but the date 
# however it is already the datetimeindex 

