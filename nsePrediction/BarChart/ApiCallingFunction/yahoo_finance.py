from BarChart.models import StocksHistory
import numpy as np
import pandas as pd
import datetime as dt
from decimal import *
train_df = pd.read_csv("C:/Users/Swagata Roy/Documents/Python_projects/nsePrediction/nsePrediction/STATIC_FILES/INFY.NS.csv",sep=',')
train_df["Open"] = train_df["Open"].apply(Decimal)
train_df["High"] = train_df["High"].apply(Decimal)
train_df["Low"] = train_df["Low"].apply(Decimal)
train_df["Close"] = train_df["Close"].apply(Decimal)
train_df["Adj Close"] = train_df["Adj Close"].apply(Decimal)
train_df["Open"] = train_df["Open"].round(6)
train_df["High"] = train_df["High"].round(6)
train_df["Low"] = train_df["Low"].round(6)
train_df["Close"] = train_df["Close"].round(6)
train_df["Adj Close"] = train_df["Adj Close"].round(6)
for ind in train_df.index:
	print(train_df["Open"][ind])
	# new_record = StocksHistory.objects.create(_companyName = "Infosys", _date = train_df["Date"][ind],_open = train_df["Open"][ind],_high = train_df["High"][ind],_low= train_df["Low"][ind],_close = train_df["Close"][ind],_adjacentClose = train_df["Adj Close"],_volume=train_df["Volume"])