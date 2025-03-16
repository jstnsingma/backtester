import pandas as pd

class Utils:

    def get_trade_data(self, timestamp, entry_price, exit_price, pnl):
        """
        Saves the data in a dict format for each trade
        
        :return: Dict containing of trade datas
        """
        data = {}

        data = {
            'timestamp': pd.Timestamp(timestamp).strftime('%Y-%m-%d %H:%M'),
            'entry_price': entry_price,
            'exit_price': exit_price,
            'pnl': pnl
            }

        return data
    
    def get_pnl(self, exit_price, entry_price):
        """
        Calculates pnl for each trade
        
        :return: pnl computation
        """
        
        return round(float(exit_price - entry_price), 2)
    
    def get_timestamp(self, data, index):
        """
        Gets the datetime of the trade
        
        :return: Datetime
        """

        return data.loc[index, 'Datetime'].values[0]
    
    def get_price(self, data, index, type):

        return round(float(data.loc[index, type].values[0]), 2)
    
    def get_notional(self, price):
        notional_value = 0.5 * price

        return round(float(notional_value), 2)
        
    def cover_short(self, entry_price, pnl, cash):
        
        notional = self.get_notional(entry_price)
        cash = cash + (notional + pnl) -2 

        return cash, notional


