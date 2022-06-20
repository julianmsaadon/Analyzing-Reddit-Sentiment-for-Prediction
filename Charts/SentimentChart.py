import pandas as pd
import matplotlib.pyplot as plt
from postobject import Post

y_axis = []
Columns = Post.GetSentimentCsvHeader()
Posts = pd.read_csv("postSentiment.csv", usecols=Columns)
PostsTitles = Posts.TitleCompound
PostsTexts = Posts.TextCompound
PostsWeights = Posts.WeightedAVG

PostsTitles.plot.hist(bins=8, color='#DF0101', rwidth=0.98)
plt.title('Number of Posts vs. Title Compound Sentiment')
plt.xlabel('Title Compound Sentiment')
plt.ylabel('Number of Posts')
plt.grid(axis='y', alpha=0.75)
plt.show()

PostsTexts.plot.hist(bins=8, color='#01DF01', rwidth=0.98)
plt.title('Number of Posts vs. Text Compound Sentiment')
plt.xlabel('Text Compound Sentiment')
plt.ylabel('Number of Posts')
plt.grid(axis='y', alpha=0.75)
plt.show()

PostsWeights.plot.hist(bins=8, color='#0045a5', rwidth=0.98)
plt.title('Number of Posts vs. Weighted Compound Sentiment')
plt.xlabel('Weighted Compound Sentiment')
plt.ylabel('Number of Posts')
plt.grid(axis='y', alpha=0.75)
plt.show()
