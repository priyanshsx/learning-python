import yfinance as yf


# list of available assets you can download historical data for from yfinance
available_assets = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'HYPE-USD', 'USDT-USD', 'BNB-USD', 'XRP-USD',
    'ZEC-USD', 'WETH-USD', 'TRX-USD', 'NEAR-USD', 'LSK-USD', '^VIX', '^GSPC']

def fetch_asset(ticker, start_date, end_date):

    # downloads the raw data 
    asset = yf.download(ticker, start=start_date, end=end_date)

    # handles if yf.download did not work/failed 
    if asset.empty:
        print(f"Looks like an error from Yahoo Finance in downloading the data. Please try again.")
        return None
    else:
        # formats the columns into a standard from the raw downloaded data   
        asset.columns = asset.columns.droplevel(1).str.lower()
        asset.index.name = 'date'
        asset.columns.name = None 
        asset.to_csv()
        print(asset.info())
        print("\n")
        print("The top 5 rows from the downloaded dataframe: ")
        print(asset.head(5))
    return asset 

print(f"Available assets to download: {available_assets}")
print("\n")

while True:
    user_ticker = input("Enter asset in the given format (TICKER-USD eg: BTC-USD): ")

    # check for correct ticker 
    if user_ticker in available_assets:
        break 
    else:
        print("Please only select from the given list. If you've already selected the correct asset, ensure it follows the format: BTC-USD.")

user_start = input("Please enter beginning date (format: YYYY-MM-DD): ")
user_end = input("Please enter end date (format: YYYY-MM-DD): ")

downloaded_data = fetch_asset(user_ticker, user_start, user_end)

# saving to csv 

if downloaded_data is not None:
    userchoice = input("Would you like to download the csv?(y/n) ").strip().lower()

    if userchoice == 'y':
        print(f"The file will be saved as {user_ticker}_data.csv. You can edit the name later.")

        filename = f'{user_ticker}_data.csv'
        downloaded_data.to_csv(filename)
        print(f"File successfully saved!")

    else:
        print("File kept in memory. Exiting program.")

