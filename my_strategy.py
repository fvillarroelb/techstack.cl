import backtrader as bt
import datetime

class MyStrategy():


    def estrategia_ema_5_anos(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=20)
        if self.data.close[0] > self.sma[0]:
            self.buy()
        elif self.data.close[0] < self.sma[0]:
            self.sell()
        cerebro = bt.Cerebro()
        data = bt.feeds.YahooFinanceData(dataname='MSFT', fromdate=datetime.datetime(2016, 1, 1), todate=datetime.datetime(2021, 3, 16))
        cerebro.adddata(data)
        cerebro.addstrategy(MyStrategy)
        cerebro.run()
        cerebro.plot()