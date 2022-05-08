import pandas as pd
import matplotlib.pyplot as plt
from postobject import Post

y_axis = []
Columns = Post.GetSentimentCsvHeader()
Posts = pd.read_csv("postSentiment.csv", usecols=Columns)
PostsTitles = Posts.TitleCompound
PostsTexts = Posts.TextCompound

PostsTitles.plot.hist(grid=True, bins=8, rwidth=0.95)
plt.title('Number of Titles vs. Compound Sentiment')
plt.xlabel('Compound Sentiment')
plt.ylabel('Number of Titles')
plt.grid(axis='y', alpha=0.75)
plt.show()

PostsTexts.plot.hist(grid=True, bins=8, color='#607c8e', rwidth=0.95)
plt.title('Number of Texts vs. Compound Sentiment')
plt.xlabel('Compound Sentiment')
plt.ylabel('Number of Texts')
plt.grid(axis='y', alpha=0.75)
plt.show()