import matplotlib.pyplot as plt
from ethdataobject import ethdata
import san
import csv
import pandas as pd
from postobject import Post


EthdataColumns = ethdata.GetEthdataCsvHeader()
# PostsColumns = Post.GetRedditCsvHeader()
Ethdata = pd.read_csv("MarketData.csv", usecols=EthdataColumns)
# Posts = pd.read_csv("postSentiment.csv", usecols=PostsColumns)
# with open('MarketData.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     Ethdata = []
#     for row in reader:
#         Ethdata.append(ethdata.GetReadethdataCsv(row))

# from_date = "2020-04-17"
# to_date = "2022-04-18"
# interval = "1h"
# Closeprice_df = san.get("price_usd/ethereum", from_date=from_date, to_date=to_date, interval=interval)

plt.plot(Ethdata.Date, Ethdata.Closeprice, Ethdata.SentimentBalanceReddit)
plt.title('ClosePrice per Hour')
plt.xlabel('Hour')
plt.ylabel('Close Price')
plt.show()

fig, ax1 = plt.subplots()

colorR = 'tab:red'
ax1.set_xlabel('Hour')
ax1.set_ylabel('Close Price', color=colorR)
ax1.plot(Ethdata.Date, Ethdata.Closeprice, color=colorR)
ax1.tick_params(axis='y', labelcolor=colorR)

ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis
ax3 = ax1.twinx()
colorB = 'tab:blue'
ax2.set_ylabel('Sentiment Balance', color=colorB)  # we already handled the x-label with ax1
ax2.plot(Ethdata.Date, Ethdata.SentimentBalanceReddit, color=colorB)
ax2.tick_params(axis='y', labelcolor=colorB)

colorG = 'tab:green'
ax3.set_ylabel('Sentiment Positive', color=colorG)  # we already handled the x-label with ax1
ax3.plot(Ethdata.Date, Ethdata.SentimentPosReddit, color=colorG)
ax3.tick_params(axis='y', labelcolor=colorG)

colorO = 'tab:orange'
ax3.set_ylabel('Sentiment Negative', color=colorO)  # we already handled the x-label with ax1
ax3.plot(Ethdata.Date, Ethdata.SentimentNegReddit, color=colorO)
ax3.tick_params(axis='y', labelcolor=colorO)
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()