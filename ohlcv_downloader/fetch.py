import yfinance as yf

def fetch_asset(ticker, start_date, end_date):

    asset = yf.download(ticker, start=start_date, end=end_date)
    asset.columns = asset.columns.droplevel(1).str.lower()
    asset.index.name = 'date'
    asset.columns.name = None 
    asset.to_csv()

    print(asset.info()) 

user_ticker = input("Please enter the asset you want to search for(format: TICKER-USD eg: BTC-USD): ")
user_start = input("Please enter beginning date: ")
user_end = input("Please enter end date: ")

fetch_asset(user_ticker, user_start, user_end)



# extracting data from yfinance by utilizing the given conditions 


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

# btc.columns = btc.columns.droplevel(1).str.lower()
# btc.index.name = 'date'
# btc.columns.name = None

