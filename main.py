import praw
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import csv
from postobject import Post

reddit = praw.Reddit(
    client_id="4q7GydrrGfBg_QtzD-pp9w",
    client_secret="JMfywlSZkOSl2qcSLWIdlCyguuJZVQ",
    password="JMS6175!",
    user_agent="StockAPI",
    username="ComparisonOld1361",
)

titles = []
selftext = []
upvotes = []
downvotes = []
ids = []
dates = []

# Date = []
# ID = []
# Title = []
# Text = []
# Upvotes = []
# Downvotes = []

# 103513

# subreddit = reddit.subreddit('ethtrader')
# for submission in subreddit.new(limit=5):
#     date = datetime.utcfromtimestamp(submission.created_utc)
#     Submission = Post(submission, date, submission.id, submission.title, submission.selftext, submission.ups, submission.downs)
#
    # submission.GetDate()
    # submission.GetID()
    # submission.GetTitle()
    # submission.GetText()
    # submission.GetUpvotes()
    # submission.GetDownvotes()




    # submission.id, submission.title, submission.selftext, submission.ups, submission.downs

# subreddit = reddit.subreddit('ethtrader')
# for submission in subreddit.new(limit=103513):
#     Post.Title.append(submission.title)
#     Post.Text.append(submission.selftext)
#     Post.Upvotes.append(submission.ups)
#     Post.Downvotes.append(submission.downs)
#     Post.ID.append(submission.id)
#     date = datetime.utcfromtimestamp(submission.created_utc)
#     Post.Date.append(date)


subreddit = reddit.subreddit('ethtrader')
for submission in subreddit.new(limit=103513):
    titles.append(submission.title)
    selftext.append(submission.selftext)
    upvotes.append(submission.ups)
    downvotes.append(submission.downs)
    ids.append(submission.id)
    date = datetime.utcfromtimestamp(submission.created_utc)
    dates.append(date)

# data = {'Date': dates,
#         'ID': ids,
#         'Title': titles,
#         'Text': selftext,
#         'Upvotes': upvotes,
#         'Downvotes': downvotes}


header = ['Date', 'ID', 'Title', 'Text', 'Upvotes', 'Downvotes']
#
#
#
# with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     for i in range(len(Post.Date)-1):
#         writer.writerow([Post.Date[i], Post.ID[i], Post.Title[i], Post.Text[i], Post.Upvotes[i], Post.Downvotes[i]])

with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(dates)-1):
        writer.writerow([dates[i], ids[i], titles[i], selftext[i], upvotes[i], downvotes[i]])

# columns = ["Date", "ID", "Title", "Text", "Upvotes", "Downvotes"]
# df = pd.read_csv("redditData.csv", usecols=columns)

# y_axis = []
#
# for i in range(len(Post.Date)-1)[::-1]:
#     y_axis.append(int(str(Post.Date[i])[11:13]))
#
# # for i in range(len(df['Date'])-1)[::-1]:
# #     y_axis.append(int(str(df['Date'][i])[11:13]))
#
# plt.hist(y_axis, bins=8)
# plt.show()
