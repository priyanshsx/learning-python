import yfinance as yf

# extracting data from yfinance by utilizing the given conditions 

btc = yf.download('BTC-USD', start='2025-01-01', end='2026-01-01')
# 
# use the below only if you want to save the file as a csv in your folder 
# btc.to_csv('/path/[asset_name].csv')

# use the below to figure out how the raw extracted csv file actually looks 
# print(btc.info())
# print("\n")
# print(btc.head(5))
# print(btc.index)
# print(btc.columns)

# using the above, we find that there are 6 columns in total titled: 
# Price, Close, High, Low, Open, Volume 
# further: the top 2 rows are non-functional as they just have BTC-USD values repeated all over 
# with the exception of the price column which is actually not price but the date 
# however it is already the datetimeindex 

# formatting the index to drop the ticker level & lowercasing all the column names 

btc.columns = btc.columns.droplevel(1).str.lower()
btc.index.name = 'date'
btc.columns.name = None

