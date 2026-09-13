import yfinance as yf

# extracting data from yfinance by utilizing the given conditions 

btc = yf.download('BTC-USD', start='2025-01-01', end='2026-01-01')
print(btc.info())
print("\n")
print(btc.head(5))

