import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf, pacf
from pandas.plotting import autocorrelation_plot
# pandas.plotting.autocorrelation_plot

import matplotlib.pyplot as plt

df1 = np.log(pd.read_csv("Crude_Oil_monthly_10.csv", usecols=["Price_Oil"]))

df2 = np.log(pd.read_csv("USD_JPY_monthly_10.csv", usecols=["Price_JPY"]))

df3 = pd.read_csv("Nikkei_monthly_10.csv", usecols=["Price_Nikkei"])
df3['Price_Nikkei'] = np.log(df3['Price_Nikkei'].str.replace(',','').astype(float))

df4 = np.log(pd.read_csv("Exp_JP.csv", usecols=["Exp_JP"]))

# Auto Corrilation function
# acf_1 = acf(df1)[1:20]
# test_df = pd.DataFrame([acf_1]).T
# test_df.columns = ['Autocorrelation']
# test_df.index += 1
# test_df.plot(kind='bar')
# plt.show()

pacf_1 = pacf(df1)[1:20]
test_df = pd.DataFrame([pacf_1]).T
test_df.column = ['Partial Autocorricaltion']
test_df.index += 1
test_df.plot(kind='bar')
plt.show()

# print(df3)
# plt.plot(df1, 'r--', df2, 'g--',df3, 'b--',df4)
# plt.show()

# combined = pd.concat([df1, df2, df3, df4], axis=1)
#
# combined.plot()
#
# plt.show()
