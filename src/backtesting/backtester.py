from .strategies import Strategy
from .strategies import ExampleStrategy
from analyzer import TradeAnalyzer
from utils import Utils

class Backtester:
    """Simple backtester that goes over the data in incremental time
    steps. The size of the time steps depend on the granularity of the
    data. When working with 1-minute interval data, each time step is
    taken 1 minute into the future.
    """

    def __init__(self,spx_future_data, spx_index_data, strategy: Strategy) -> None:
        self._strategy = strategy
        self.example_strategy = ExampleStrategy()
        self.utils = Utils()
        self.trade_position = []
        self.executed_trades = []
        self.trade_performance = {}
        self.spx_future_data = spx_future_data
        self.spx_index_data = spx_index_data
        self.cash = 100000
        self.commission = 2
        self.index = 0
        
    def run(self) -> None:
        """Loops through the function while next is still true"""

        while self.next():
            self.check_strategy()
            self.close_position()
        self.analyze_trade()
        self.print_performance()

    def next(self) -> bool:
        """Continue to the next time step.

        :return: True when there is a new time step, False otherwise
        """

        if self.index >= len(self.spx_future_data) - 1:
            return False
        self.index += 1
        return True

    def check_strategy(self) -> bool:
        """Check if the currently active strategy should take any
        action.

        :return: True if we need to buy or sell a position, False
        otherwise
        """

        current_data = self.spx_future_data.iloc[:self.index]
        action = self.example_strategy.check_strategies(current_data, self._strategy)
        if action != 0:
            self.open_position(action)
        return action != 0

    def open_position(self, action) -> bool:
        """Mock placing an OPENING order that trades yielding a new
        position.
        """

        price = self.utils.get_price(self.spx_index_data, self.index, 'Close')
        timestamp = self.utils.get_timestamp(self.spx_index_data, self.index)

        if action == "BUY":
            cost = price + self.commission
        else:
            short_position = 0.5 * self.cash
            cost = 0.05 * short_position

        self.trade_position.append((action, price, self.index + 10))
        self.cash -= cost

        print(f"{timestamp} Trade Executed: {action} at {price:.2f}")
        print(f"Current cash balance: {self.cash:.2f}")

    def close_position(self) -> None:
        """Mock placing a CLOSING order that trades to close an existing
        position.
        """

        to_close_positions = [pos for pos in self.trade_position if pos[2] == self.index]
        
        for action, entry_price, _ in to_close_positions:
            
            exit_price = self.utils.get_price(self.spx_index_data, self.index, 'Close')
            timestamp = self.utils.get_timestamp(self.spx_index_data, self.index)
            pnl = self.utils.get_pnl(exit_price, entry_price, self.commission)
            self.cash += entry_price + pnl

            print(f"{timestamp}  Closed {action} at {exit_price:.2f}, PnL: {pnl:.2f}")
            print(f"Current cash balance: {self.cash:.2f}")

            trade_data = self.utils.get_trade_data(timestamp, entry_price, exit_price, pnl)
            self.executed_trades.append(trade_data)
            
        self.trade_position = [pos for pos in self.trade_position if pos[2] > self.index]

    def analyze_trade(self)-> None:

        analyzer = TradeAnalyzer(self.executed_trades)
        summary = analyzer.get_summary_per_day()
        winners = analyzer.get_winners()
        losers = analyzer.get_losers()

        self.trade_performance['summary'] = summary
        self.trade_performance['winners'] = winners
        self.trade_performance['losers'] = losers
        
    def print_performance(self) -> None:
        """Print the realized performance to the console.

        Details to include:
        - Executed trades
        - Winners (positions making money)
        - Losers (positions losing money)
        - Geometric Profit/Loss (PnL)
        - Sharpe Ratio
        """
        print(f"summary per day: {self.trade_performance['summary']}")
        print(f"Data of winning trades: {self.trade_performance['winners']}")
        print(f"Data of Losing trades: {self.trade_performance['losers']}")
        print(f"Final Balance: {self.cash:.2f}")
    