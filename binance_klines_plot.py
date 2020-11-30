import numpy as np
import pandas as pd
import mplfinance as mpf
import datetime

klines = np.load('klines.npy')

klines = klines[-150:,:] #remove to use custom plot range


range_time = int(np.shape(klines)[0])
df = pd.DataFrame(data=klines[:,:], columns=["Date", "Open","High","Low","Close","Volume"])
for i in df.index:
    df.at[i, "Date"] = datetime.datetime.fromtimestamp(int(klines[i,0] )/ 1e3)

df = df.set_index('Date')

mpf.plot(df,type='candle',volume=True)
mpf.plot(df,type='candle',mav=(5, 30,100))

