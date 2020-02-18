from alpha_vantage.timeseries import TimeSeries
import pandas as pd

from stock import Stock

key = ""

# Add stocks to follow
aapl = Stock("AAPL")
tsla = Stock("TSLA")

stocks = [aapl, tsla]

# Set TimeSeries up
ts = TimeSeries(key, output_format="pandas")

# Loop through Stocks
for stock in stocks:
    # Add data
    stock.df, stock.meta = ts.get_daily(symbol=stock.symbol, outputsize="full")

    # Print head
    print(stock.df.head())