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
            'entry_price': round(float(entry_price), 2),
            'exit_price': round(float(exit_price), 2),
            'pnl': round(float(pnl), 2)
            }

        return data
    
    def get_pnl(self, exit_price, entry_price, commission):
        """
        Calculates pnl for each trade
        
        :return: pnl computation
        """

        return (exit_price - entry_price) - commission
    
    def get_timestamp(self, data, index):
        """
        Gets the datetime of the trade
        
        :return: Datetime
        """

        return data.loc[index, 'Datetime'].values[0]
    
    def get_price(self, data, index, type):

        return data.loc[index, type].values[0]
        
