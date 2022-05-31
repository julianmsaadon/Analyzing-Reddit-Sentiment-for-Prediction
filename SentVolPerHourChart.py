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

fig, ax = plt.subplots()
# ax.hist(Posts, bins=Ethdata.Date)
bins_list = Ethdata.Date.tolist()
# posts_list = Posts.Date.tolist()
testlist = ['2022-05-18 06:00:00', '2022-05-18 09:00:00', '2022-05-18 12:00:00']
print(bins_list)

plt.bar(bins_list, testlist, align='center')
plt.show()
# plt.hist(testlist, bins=bins_list)
# plt.show()

# plt.plot(Ethdata.Date, Posts.SentimentBalanceReddit)
# plt.title('ClosePrice per Hour')
# plt.xlabel('Hour')
# plt.ylabel('Close Price')
# plt.show()

# print(Posts)