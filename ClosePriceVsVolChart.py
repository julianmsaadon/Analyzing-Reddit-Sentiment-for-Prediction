import matplotlib.pyplot as plt
from ethdataobject import ethdata
import san
import csv
import pandas as pd
from postobject import Post


EthdataColumns = ethdata.GetEthdataCsvHeader()
# PostsColumns = Post.GetRedditCsvHeader()
Ethdata = pd.read_csv("MarketData.csv", usecols=EthdataColumns)


fig, ax1 = plt.subplots()

colorR = 'tab:red'
ax1.set_xlabel('Hour')
ax1.set_ylabel('Close Price', color=colorR)
CP = ax1.plot(Ethdata.Date, Ethdata.Closeprice, color=colorR, label='Close Price')
ax1.tick_params(axis='y', labelcolor=colorR)

ax2 = ax1.twinx()
colorB = 'tab:blue'
ax2.set_ylabel('Transaction Volume', color=colorB)
TV = ax2.plot(Ethdata.Date, Ethdata.TransactionVolume, color=colorB, label='Transaction Volume')
ax2.tick_params(axis='y', labelcolor=colorB)

lines = CP+TV
labs = [l.get_label() for l in lines]
ax1.legend(lines, labs, loc=0)

# ax3 = ax1.twinx()
# colorG = 'tab:green'
# ax3.set_ylabel('Social Reddit Volume', color=colorG)
# ax3.plot(Ethdata.Date, Ethdata.SocialVolumeReddit, color=colorG)
# ax3.tick_params(axis='y', labelcolor=colorG)
#
# ax4 = ax1.twinx()
# colorO = 'tab:orange'
# ax4.set_ylabel('Sentiment Volume Reddit', color=colorO)
# ax4.plot(Ethdata.Date, Ethdata.SentimentVolumeConsumedReddit, color=colorO)
# ax4.tick_params(axis='y', labelcolor=colorO)
#
# ax5 = ax1.twinx()
# colorP = 'tab:purple'
# ax3.set_ylabel('Social Dominance Reddit', color=colorP)
# ax3.plot(Ethdata.Date, Ethdata.SocialDomReddit, color=colorP)
# ax3.tick_params(axis='y', labelcolor=colorP)

fig.tight_layout()
plt.show()