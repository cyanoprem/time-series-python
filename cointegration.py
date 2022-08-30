import pandas as pd
from johansen import coint_johansen
import numpy as np
import matplotlib.pyplot as plt  
import statsmodels.api as sm
df_a = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\PHDPaper\\TCS.NS.csv",index_col=0)
df_b = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\PHDPaper\\INFY.NS.csv",index_col=0)
#df_c = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\PHDPaper\\ICICIBANK.NS.csv",index_col=0)
#df_d = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\PHDPaper\\GLD2.csv",index_col=0)
#df_e = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\PHDPaper\\GDX2.csv",index_col=0)
#df_f = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\PHDPaper\\USO2.csv",index_col=0)
# Type your code below
# Create dataframe df
#df = pd.DataFrame({'a':df_a['Close'],'b':df_b['Close'],'c':df_c['Close'],'d':df_d['Close'],'e':df_e['Close'],'f':df_f['Close']})
# Call coint_johansen and save it in results
df = pd.DataFrame({'a':df_a['Close'],'b':df_b['Close']})
results = coint_johansen(df,0,1)

#storing the eigenvectors
d = results.evec
ev=d[0]
#normalizing the eigenvectors
ev=ev/ev[0]
#printing the mean reverting spread
#print("\nSpread = {}.GLD + ({}).GDX + ({}).USO".format(ev[0],ev[1],ev[2]))
print("\nspread = ({}).TCS + ({}).INFY".format(ev[0],ev[1]))
df['spread'] = df.a + ev[1]*df.b
df.spread.plot(figsize=(10,5))
plt.ylabel("TCS - 0.14 * INFY")
plt.show()


adf = ts.adfuller(df.spread)
# Print ADF t-stat
print(adf[0])
print('p-value: %f'% adf[1])
print("Critical Values:")
for key, value in adf[4].items():
    print('\t%s: %.3f' % (key, value))

if adf[0]<adf[4]['5%']:
    print("Reject Ho - Time series is stationary")
else:
    print("Failed to reject H0- Time series is Non-stationary") 

lookback=5
# Moving Average and Moving Standard Deviation
df['moving_average'] = df.spread.rolling(lookback).mean()
df['moving_std_dev'] = df.spread.rolling(lookback).std()
# Upper band and lower band
df['upper_band'] = df.moving_average + 0.5*df.moving_std_dev
df['lower_band'] = df.moving_average - 0.5*df.moving_std_dev
df.tail(7)

# Long
df['long_entry'] = df.spread < df.lower_band   
df['long_exit'] = df.spread >= df.moving_average
# Short
df['short_entry'] = df.spread > df.upper_band   
df['short_exit'] = df.spread <= df.moving_average
df.tail(15)