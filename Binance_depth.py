import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from binance.client import Client

api_key = ''
api_secret = ''

client = Client(api_key, api_secret)


# get market depth
depth = client.get_order_book(symbol='BTCUSDT',limit = 10000)
                              
print(depth)

asks = depth["asks"]
asks = np.array(asks, dtype=float)

bids = depth["bids"]
bids = np.array(bids, dtype=float)

    
np.save('asks', asks)
np.save('bids', bids)
  
