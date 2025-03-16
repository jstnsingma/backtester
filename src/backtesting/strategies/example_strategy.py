from .base_strategy import Strategy
import numpy as np

class ExampleStrategy():

    def check_strategies(self, data, strategy: Strategy):
        """Call the strategy function"""

        try: 
            if strategy == Strategy.MOMENTUM:
                computed = self.compute_momentum(data)
            if strategy == Strategy.SWING:
                computed = self.compute_swing(data)
            return computed
        except Exception as e:
            raise RuntimeError(f"Error: {e}")

    def compute_momentum(self, data) -> float:
        """Calculate rolling momentum strategy"""
        threshold = 0.0005
        data = np.array(data['Close'])
        if len(data) < 6:
            return 0 
        X_n = sum(data[-5:]) / len(data[-5:]) if len(data[-5:]) > 0 else 0
        X_n1 = sum(data[-6:-1]) / len(data[-6:-1]) if len(data[-6:-1]) > 0 else 0
        momentum = (X_n - X_n1) / X_n

        if momentum > threshold:
            return "BUY" 
        elif momentum < -threshold:
            return "SELL"
        return 0
    
    
