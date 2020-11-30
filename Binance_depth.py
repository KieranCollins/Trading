import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from binance.client import Client

api_key = 'kgpWFYsympqmVjSPHMuHj0nXcgOGsCpMvPNm99i3N0JxyeaxhYBqjBvOcUHCdnHt'
api_secret = 'B2TbctQvmTKkbG57Q43wI4cl2UzSZoEXKvqthdSrBShEcyE5CPuQUkN22KhFLSQJ'

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
  
