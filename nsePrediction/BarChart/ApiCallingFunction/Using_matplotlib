import numpy as np;
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

train_df = pd.read_csv("C:/Users/Swagata Roy/Documents/Python_projects/nsePrediction/nsePrediction/STATIC_FILES/INFY.NS.csv",sep=',')
x = train_df['Date'].to_numpy()
y = train_df['Date'].to_numpy()
now = dt.datetime.now()
then = now + dt.timedelta(days=-len(y))
days = mdates.drange(then,now,dt.timedelta(days=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.plot(days,x)
plt.show()
y = train_df['Close'].to_numpy()
plt.plot(days,y)
plt.show()