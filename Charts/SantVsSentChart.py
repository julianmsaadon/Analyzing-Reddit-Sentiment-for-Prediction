import matplotlib.pyplot as plt
from ethdataobject import ethdata
import san
import csv
import pandas as pd
from postobject import Post

PostsColumns = Post.GetSentimentCsvHeader()
Posts = pd.read_csv("postSentiment.csv", usecols=PostsColumns)

EthdataColumns = ethdata.GetEthdataCsvHeader()
Ethdata = pd.read_csv("MarketData.csv", usecols=EthdataColumns)

fig, ax1 = plt.subplots()

colorR = 'tab:red'
ax1.set_xlabel('Hour')
ax1.set_ylabel('Close Price', color=colorR)
ax1.plot(Ethdata.Date, Ethdata.Closeprice, color=colorR)
ax1.tick_params(axis='y', labelcolor=colorR)

ax2 = ax1.twinx()
colorB = 'tab:blue'
ax2.set_ylabel('Santiment Balance', color=colorB)
ax2.plot(Ethdata.Date, Ethdata.SentimentBalanceReddit, color=colorB)
ax2.tick_params(axis='y', labelcolor=colorB)

ax3 = ax1.twinx()
colorG = 'tab:green'
ax3.set_ylabel('Weighted AVG Sentiment', color=colorG)
ax3.plot(Ethdata.Date, Posts.WeightedAVG, color=colorG)
ax3.tick_params(axis='y', labelcolor=colorG)

fig.tight_layout()
plt.show()