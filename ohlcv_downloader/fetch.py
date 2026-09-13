import yfinance as yf

intc = yf.download('', start='2025-01-01', end='2026-01-01')
intc.to_csv('/test_intc.csv')