import matplotlib.pyplot as plt
from ethdataobject import ethdata
import san
import csv
import pandas as pd
from postobject import Post


EthdataColumns = ethdata.GetEthdataCsvHeader()
# PostsColumns = Post.GetRedditCsvHeader()
Ethdata = pd.read_csv("MarketData.csv", usecols=EthdataColumns)

# plt.plot(Ethdata.Date, Ethdata.Closeprice, Ethdata.SentimentBalanceReddit)
# plt.title('ClosePrice per Hour')
# plt.xlabel('Hour')
# plt.ylabel('Close Price')
# plt.show()

fig, ax1 = plt.subplots()

colorR = 'tab:red'
ax1.set_xlabel('Hour')
ax1.set_ylabel('Close Price', color=colorR)
ax1.plot(Ethdata.Date, Ethdata.Closeprice, color=colorR)
ax1.tick_params(axis='y', labelcolor=colorR)

ax2 = ax1.twinx()
colorB = 'tab:blue'
ax2.set_ylabel('Sentiment Balance', color=colorB)
ax2.plot(Ethdata.Date, Ethdata.SentimentBalanceReddit, color=colorB)
ax2.tick_params(axis='y', labelcolor=colorB)

# ax3 = ax1.twinx()
# colorG = 'tab:green'
# ax3.set_ylabel('Sentiment Positive', color=colorG)
# ax3.plot(Ethdata.Date, Ethdata.SentimentPosReddit, color=colorG)
# ax3.tick_params(axis='y', labelcolor=colorG)
#
# ax4 = ax1.twinx()
# colorO = 'tab:orange'
# ax4.set_ylabel('Sentiment Negative', color=colorO)
# ax4.plot(Ethdata.Date, Ethdata.SentimentNegReddit, color=colorO)
# ax4.tick_params(axis='y', labelcolor=colorO)
fig.tight_layout()

plt.legend(handles=['ClosePrice', 'SentimentBalance'])
plt.show()
