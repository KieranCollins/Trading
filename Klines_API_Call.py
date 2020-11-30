import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from binance.client import Client

api_key = ''
api_secret = ''

client = Client(api_key, api_secret)


klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "20 Nov, 2017", "30 Nov, 2020")
                            

klines = np.array(klines, dtype=float)
print(klines[:,:])
klines = klines[:,0:6]
print(klines)
np.save('klines', klines)

