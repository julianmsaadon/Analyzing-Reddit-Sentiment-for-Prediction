import praw
from datetime import datetime
import csv
from postobject import Post

reddit = praw.Reddit(
    client_id="4q7GydrrGfBg_QtzD-pp9w",
    client_secret="JMfywlSZkOSl2qcSLWIdlCyguuJZVQ",
    password="JMS6175!",
    user_agent="StockAPI",
    username="ComparisonOld1361",
)
# r = praw.Reddit(user_agent="StockAPI")

# searchreddit = r.search(sort='New', period='1Y')
# 103513
Posts = []
subreddit = reddit.subreddit('ethtrader')
for submission in subreddit.search(query=None, sort='New', time_filter='year'):
    date = datetime.utcfromtimestamp(submission.created_utc)
    post = Post(date, submission.id, submission.title, submission.selftext, submission.ups, submission.downs)
    Posts.append(post)

# for submission in subreddit.new(limit=103513):
#     date = datetime.utcfromtimestamp(submission.created_utc)
#     post = Post(date, submission.id, submission.title, submission.selftext, submission.ups, submission.downs)
#     Posts.append(post)



# subSearch = search(sort='New', period='1Y')
# print(subSearch)
# For  period of a day (for each day)
# Search by day
# append Posts with that specific search

with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(Post.GetRedditCsvHeader())
    for i in range(len(Posts)-1):
        writer.writerow(Posts[i].GetRedditCsvString())
