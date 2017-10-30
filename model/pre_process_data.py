import numpy as np
import pandas as pd

DATA_FILE = '../data_examples/btc_price_2017-09-13T03:45:28+00:00.csv'
DATA = pd.read_csv(DATA_FILE, sep=',', parse_dates=True, index_col=0)

TRADING_HORIZON = 6300  # x ticks ahead.

np.set_printoptions(threshold=np.nan)
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def run(trading_horizon=TRADING_HORIZON, data=DATA):
    d = pd.DataFrame(DATA[['timestamp', 'bid', 'ask']])
    d['bid_future'] = d['bid'].shift(-trading_horizon)
    d['fees_buy'] = - 0.25 / 100 * d['ask']
    d['fees_sell'] = - 0.25 / 100 * d['bid_future']
    d['profitability'] = d['bid_future'] - d['ask'] + - 0.25 / 100 * (d['ask'] + d['bid_future'])
    d.dropna(inplace=True)
    print(d)
    return d['profitability'].sum()


if __name__ == '__main__':
    print(run())
    # for i in range(1, 150000, 1000):
    #     print(i, run(trading_horizon=i))
