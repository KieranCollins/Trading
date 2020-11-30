import json
import numpy as np
from matplotlib import pyplot as plt

asks = np.load('asks.npy')
bids = np.load('bids.npy')

bids_C = np.cumsum(bids[:,1])
asks_C = np.cumsum(asks[:,1])


plt.plot(asks[:,0], asks[:,1])
plt.plot(bids[:,0], bids[:,1])
plt.plot(bids[:,0], bids_C )
plt.plot(asks[:,0], asks_C )
plt.xlabel("Price $")
plt.xlabel("Cumulative Volume")
plt.title("BTC-USD Orders Book")
print(bids)







