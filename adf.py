
# Import library
import pandas as pd
import statsmodels.tsa.stattools as ts
# Read CSV into data frame
prices_df = pd.read_csv("C:\\Users\\VIPLSORENTAL45\\Downloads\\INFY.NS.csv",index_col=0)
# Type your code below
# Compute ADF test statistics
adf = ts.adfuller(prices_df.Close)
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

#Adf statistic: -2.314274
#p-value: 0.167406
#Critical Values:
 #       1%: -3.458
  #      5%: -2.874
   #     10%: -2.573
#Failed to reject H0- Time series is Non-stationary
