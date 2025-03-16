import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from backtesting.backtester import Backtester
from backtesting.strategies.base_strategy import Strategy


def fetch_data(symbol):
    """Fetches the 2-week interval data for future and index"""
    
    today_date = datetime.now() 
    end_date = today_date - timedelta(days=7)
    start_date = today_date - timedelta(days=14)

    try: 
        data1 = yf.download(symbol, period="7d", interval="1m", start=start_date, end=end_date)
        data2 = yf.download(symbol, period="7d", interval="1m")
        data = pd.concat([data1, data2]).drop_duplicates()
        data = data.reset_index()

        return data
    
    except Exception as e:
        raise RuntimeError(f"Error fetching data: {e}")

if __name__ == "__main__":
    strategies = [Strategy.MOMENTUM]
    future_symbol = "ES=F"
    index_symbol = "^GSPC"

    spx_future_data = fetch_data(future_symbol)
    spx_index_data = fetch_data(index_symbol)
    
    spx_future_data = spx_future_data.merge(spx_index_data[["Datetime"]], on="Datetime")

    for strat in strategies: 
        backtester = Backtester(spx_future_data, spx_index_data, strat)
        backtester.run()
        