import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset

MarketDf = pd.read_csv('MarketData.csv')
RedditDf = pd.read_csv('postSentiment.csv')

MarketDf.index = pd.to_datetime(MarketDf['Date'])
print(MarketDf)
timeSeries = pd.date_range("2021-05-18", "2022-05-19", freq="3H").strftime('%Y-%m-%d %H:%M:%S')
# for i in RedditDf:
#     trying to change the date of the post to the closest timeseries item ahead of it,
#     then i can join the redditdf with the marketdf
