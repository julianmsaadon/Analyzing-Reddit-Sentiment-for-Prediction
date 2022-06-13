import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dataset

MarketDf = pd.read_csv('MarketData.csv')
RedditDf = pd.read_csv('postSentiment.csv')

MarketDf.index = pd.to_datetime(MarketDf['Date'])
print(MarketDf)