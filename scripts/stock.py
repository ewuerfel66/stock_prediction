"""
Class for Stocks

Attributes:
    - Stock symbol
    - DataFrame
    - MetaData
"""

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = None
        self.meta = None