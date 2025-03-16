import pandas as pd

class TradeAnalyzer:
    """Class to analyze trade performance and extract winning trades."""
    
    def __init__(self, trades):
        """
        Initialize the analyzer with trade data.
        
        :param trades: List of trade dictionaries containing 'timestamp', 'entry_price', 
                       'exit_price', and 'pnl'.
        """
        
        self.trades = pd.DataFrame(trades)
        self.calculate_geometric_pnl()
        self.calculate_sharpe_ratio()

    def calculate_geometric_pnl(self):
        """Compute geometric PnL for each trade individually."""

        self.trades["geometric_pnl"] = ((self.trades["exit_price"] / self.trades["entry_price"]) - 1) * 100

    def get_winners(self) -> pd.DataFrame:
        """
        Returns only winning trades

        :return: DataFrame containing only winning trades
        """

        return self.trades[self.trades["pnl"] > 0].copy()
    
    def get_losers(self) -> pd.DataFrame:
        """
        Returns only lossing trades

        :return: DataFrame containing only losing trades
        """

        return self.trades[self.trades["pnl"] < 0].copy()
    
    def calculate_sharpe_ratio(self) -> float:
        """Compute Sharpe Ratio for the trade returns"""

        self.trades["sharpe_ratio"] = self.trades["geometric_pnl"] / self.trades["geometric_pnl"].std()

    def get_summary_per_day(self) -> pd.DataFrame:
        """
        Returns the summary data per day 
        
        :return: DataFrame containing date, total_pnl and total_trades
        """

        self.trades['timestamp'] = pd.to_datetime(self.trades['timestamp'])

        # Extract the date part
        self.trades['date'] = self.trades['timestamp'].dt.date

        # Group by date
        grouped = {date: group for date, group in self.trades.groupby('date')}

        day_summary = {}
        # Print results
        for date, group in grouped.items():
            date = date.strftime("%d-%m-%Y")
            day_summary[date] = {}
            day_summary[date]['total_pnl'] = float(group["pnl"].sum())
            day_summary[date]['total_trades'] = len(group)

        return pd.DataFrame(day_summary)
    