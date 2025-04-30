import yfinance as yf

# Get data for an Indian stock (NSE)
stock = yf.Ticker("TCS.NS")
stock_info = stock.history(period="1d")
print(stock_info)

# Get data for a global stock
stock_global = yf.Ticker("AAPL")
stock_global_info = stock_global.history(period="1d")
print(stock_global_info)
