from psaw import PushshiftAPI
from datetime import datetime
import praw
import csv
import pandas as pd
from postobject import Post


api = PushshiftAPI()

reddit = praw.Reddit(
    client_id="4q7GydrrGfBg_QtzD-pp9w",
    client_secret="JMfywlSZkOSl2qcSLWIdlCyguuJZVQ",
    password="JMS6175!",
    user_agent="StockAPI",
    username="ComparisonOld1361",
)

subreddit = ['ethtrader']

Posts = []
timeSeries = pd.date_range("2021-05-18", "2022-05-19", freq="D").strftime('%Y-%m-%d %H:%M:%S')
ModifiedTimeSeries = pd.date_range("2021-11-11", "2022-05-19", freq="D").strftime('%Y-%m-%d %H:%M:%S')
print(timeSeries)

# 'a' instead of 'w'
# with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file, delimiter='�')
#     writer.writerow(Post.GetRedditCsvHeader())
#     for i in range(len(timeSeries) - 1):
#         psawSearch = api.search_submissions(
#             after=timeSeries[i],
#             before=timeSeries[i + 1],
#             filter=['id'],
#             subreddit=subreddit,
#             limit=None
#         )
#         for submission_psaw in psawSearch:
#             submission_id = submission_psaw.d_['id']
#             submission = reddit.submission(id=submission_id)
#             date = datetime.utcfromtimestamp(submission.created_utc)
#             post = Post(date,
#                         submission.id,
#                         submission.title.replace("\n", " ").replace(" ", " "),
#                         submission.selftext.replace("\n", " ").replace(" ", " "),
#                         submission.ups,
#                         submission.downs)
#             Posts.append(post)
#
#     # with open('redditData.csv', 'a', encoding='UTF8', newline='') as csvfile:
#         for n in range(len(Posts)-1):
#             if (str(Posts[n].Text) != "[removed]") and (str(Posts[n].Text) != "[deleted]"):
#                 writer.writerow(Posts[n].GetRedditCsvString())
#         Posts = []

#### For second runthru if needed
with open('redditData.csv', 'a', encoding='UTF8', newline='') as file:
    writer = csv.writer(file, delimiter='�')
    for i in range(len(ModifiedTimeSeries) - 1):
        psawSearch = api.search_submissions(
            after=ModifiedTimeSeries[i],
            before=ModifiedTimeSeries[i + 1],
            filter=['id'],
            subreddit=subreddit,
            limit=None
        )
        for submission_psaw in psawSearch:
            submission_id = submission_psaw.d_['id']
            submission = reddit.submission(id=submission_id)
            date = datetime.utcfromtimestamp(submission.created_utc)
            post = Post(date,
                        submission.id,
                        submission.title.replace("\n", " "),
                        submission.selftext.replace("\n", " "),
                        submission.ups,
                        submission.downs)
            Posts.append(post)

    # with open('redditData.csv', 'a', encoding='UTF8', newline='') as csvfile:
        for n in range(len(Posts)-1):
            if (Posts[n].Text != '[removed]') and (Posts[n].Text != '[deleted]'):
                # writer = csv.writer(file)
                writer.writerow(Posts[n].GetRedditCsvString())
        Posts = []
