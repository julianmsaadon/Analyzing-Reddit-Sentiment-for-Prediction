import pandas as pd
import matplotlib.pyplot as plt
from postobject import Post

y_axis = []
Columns = Post.GetRedditCsvHeader()
Posts = pd.read_csv("redditData.csv", usecols=Columns)

for i in range(len(Posts.Date)-1)[::-1]:
    y_axis.append(int(str(Posts.Date[i])[11:13]))

plt.hist(y_axis, bins=8)
plt.show()