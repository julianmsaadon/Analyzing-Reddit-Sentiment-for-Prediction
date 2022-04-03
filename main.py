import praw
import pandas as pd
from praw.models import MoreComments
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
from datetime import datetime, timedelta
import emoji
import re
import spacy
import matplotlib.pyplot as plt
import matplotlib.dates
import csv

reddit = praw.Reddit(
    client_id="4q7GydrrGfBg_QtzD-pp9w",
    client_secret="JMfywlSZkOSl2qcSLWIdlCyguuJZVQ",
    password="JMS6175!",
    user_agent="StockAPI",
    username="ComparisonOld1361",
)

# subreddit = reddit.subreddit('ethtrader')
# for submission in subreddit.new(limit=5):
#     print('submission ID = ', submission.id)
#     print(submission.title)
#     print(submission.selftext)
#     print('\n')

titles = []
selftext = []
upvotes = []
downvotes = []
ids = []
dates = []

subreddit = reddit.subreddit('ethtrader')
for submission in subreddit.new(limit=103513):
    titles.append(submission.title)
    selftext.append(submission.selftext)
    upvotes.append(submission.ups)
    downvotes.append(submission.downs)
    ids.append(submission.id)
    date = datetime.utcfromtimestamp(submission.created_utc)
    dates.append(date)

print(ids)
print(titles)
print(selftext)
print(upvotes)
print(downvotes)
print(dates)

data = {'Date': dates,
        'ID': ids,
        'Title': titles,
        'Text': selftext,
        'Upvotes': upvotes,
        'Downvotes': downvotes}
df = pd.DataFrame(data)


y_axis = []
for i in range(len(dates)-1)[::-1]:
    y_axis.append(int(str(dates[i])[11:13]))

plt.hist(y_axis, bins=24)
plt.show()