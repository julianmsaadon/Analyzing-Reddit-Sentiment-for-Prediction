from psaw import PushshiftAPI
from datetime import datetime
import praw
import csv
from postobject import Post

# api = PushshiftAPI()
# start_epoch = int(dt.datetime(2021, 5, 18).timestamp())
# subs = list(api.search_submissions(after=start_epoch, subreddit='ethtrader', limit=1))
# print(subs)

api = PushshiftAPI()

reddit = praw.Reddit(
    client_id="4q7GydrrGfBg_QtzD-pp9w",
    client_secret="JMfywlSZkOSl2qcSLWIdlCyguuJZVQ",
    password="JMS6175!",
    user_agent="StockAPI",
    username="ComparisonOld1361",
)

subreddit = ['ethtrader']
startTime = 2021
endTime = 2022

# ts_after = int(datetime.datetime(2021, 5, 18).timestamp())
# ts_before = int(datetime.datetime(2022, 5, 18).timestamp())
timeAfter = "2021-05-18"
timeBefore = "2022-05-18"

psawSearch = api.search_submissions(
            after=timeAfter,
            before=timeBefore,
            filter=['id'],
            subreddit=subreddit,
            limit=None
)
Posts = []
for submission_psaw in psawSearch:
    submission_id = submission_psaw.d_['id']
    submission = reddit.submission(id=submission_id)
    date = datetime.utcfromtimestamp(submission.created_utc)
    post = Post(date, submission.id, submission.title, submission.selftext, submission.ups, submission.downs)
    Posts.append(post)

with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(Post.GetRedditCsvHeader())
    for i in range(len(Posts)-1):
        writer.writerow(Posts[i].GetRedditCsvString())
