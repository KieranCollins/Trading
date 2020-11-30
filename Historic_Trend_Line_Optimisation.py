import numpy as np
import pandas as pd
import mplfinance as mpf
import datetime
import matplotlib
import matplotlib.pyplot as plt
import math

klines = np.load('klines.npy')
range_time = int(np.shape(klines)[0])

klines[:,5]=np.zeros(range_time)


diff = 1-(klines[0,1]-klines[-1,4])/klines[0,1]

percent_key = 0.15
for i in range(range_time):
    if abs((klines[i,1] - klines[i,4])/klines[i,1]) >= percent_key:
        klines[i,5] = -(klines[i,1] - klines[i,4])/klines[i,1]
    if i > 0:
        if abs(klines[i-1,5]) >= percent_key:
            klines[i,5] = -(klines[i,1] - klines[i,4])/klines[i,1]
    #if i > 1:
    #    if abs(klines[i-2,5]) >= percent_key:
    #        klines[i,5] = -(klines[i,1] - klines[i,4])/klines[i,1]
    else:
        klines[i,1:5]=np.zeros(4)
     
    
df = pd.DataFrame(data=klines[:,:], columns=["Date", "Open","High","Low","Close","Volume"])
for i in df.index:
    df.at[i, "Date"] = datetime.datetime.fromtimestamp(int(klines[i,0] )/ 1e3)


8,31,99

df['avg'] = df[['Open', 'Close']].mean(axis=1)
df['mean10'] = df['avg'].rolling(8).mean()
df['mean30'] = df['avg'].rolling(31).mean()
df['mean100'] = df['avg'].rolling(99).mean()





money = 1000
buy = 0
flip = 2
buy = 0
sell = 0

for i in df.index:
    #starting
    if i > 100:
     if flip == 2:  
        if int(df["mean10"][i]) < int(df['mean100'][i]):

            if int(df['mean30'][i]) < int(df['mean100'][i]):
                
                flip = 0
                #ready
     
     #buy            
     elif flip == 0:                    
        if int(df["mean10"][i]) > int(df['mean100'][i]):
            if int(df['mean30'][i]) > int(df['mean100'][i]):
              if int(df['mean10'][i]) > int(df['mean30'][i]):  
                #if int(df['mean10'][i]) < int(df['mean10'][i-5]):
                #if int(df['mean30'][i]) < int(df['mean30'][i-5]):    
                #if int(df['mean100'][i]) < int(df['mean100'][i-5]):
                money = money/int(df['avg'][i])*0.995
                print("buy",int(df['avg'][i]),money*int(df['avg'][i]),df["Date"][i])
                flip = 1
                buy = int(df['avg'][i])              
    
     #sell           
     elif flip ==1:# and int(df['avg'][i])>buy: 
         if int(df["mean10"][i]) < int(df['mean30'][i]):
             money = money * int(df['avg'][i])*0.995
             print("sell",int(df['avg'][i]),money,df["Date"][i])
             flip = 0
             sell = int(df['avg'][i])


                
#print(money*int(df['avg'][range_time-1]))
print("sell",int(df['avg'][range_time-1]),money*int(df['avg'][range_time-1])*0.995)                
                
                
    
    





