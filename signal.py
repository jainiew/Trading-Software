import Server.database as db
import pandas as pd

class Signal:
    def __init__(self):
        self.df = db.execute("SELECT date, ticker from *")
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df.set_index('Date', inplace=True)
        self.s = self.df

    def s_avg(self):
        """
        """
        windows = self.s.rolling('24H')
        mas = windows.mean().dropna()
        return mas

    def sigma(self, s):
        pass

    def strategy(self, t):
        """ the intraday price series of  a given stock
        """
        pos = []
        for i in range(len(self.s)):
            if self.s[i] > self.s_avg()[t] + self.s.std():
                pos[t+1] += 1
            elif self.s[i] < self.s_avg()[t] + self.s.std():
                pos[t + 1] -= 1
            else:
                pos[t + 1] = pos[t]

        return pos

    def pnl(self, pos, t, s):
        pnl_t = pos[t-1] * (s[t] - s[t-1])
        return pnl_t