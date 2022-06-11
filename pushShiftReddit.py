from psaw import PushshiftAPI
from datetime import datetime
import praw
import csv
import pandas as pd
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
# startTime = 2021
# endTime = 2022

# ts_after = int(datetime.datetime(2021, 5, 18).timestamp())
# ts_before = int(datetime.datetime(2022, 5, 18).timestamp())
# timeAfter = "2021-05-18"
# timeBefore = "2022-05-18"
# with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(Post.GetRedditCsvHeader())
#     for i in range(len(Posts)-1):
#         if Posts[i].Text != '[removed]' or Posts[i].Text != '[deleted]':
#             writer.writerow(Posts[i].GetRedditCsvString())
Posts = []
timeSeries = pd.date_range(start="2021-05-18", end="2022-05-18")
timeSeriesBEtter = pd.date_range("2021-05-18", "2022-05-18", freq="D").strftime('%Y-%m-%d %H:%M:%S')
ModifiedTimeSeries = pd.date_range("2021-12-25", "2022-05-18", freq="D").strftime('%Y-%m-%d %H:%M:%S')
print(timeSeriesBEtter)
# with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(Post.GetRedditCsvHeader())
with open('2ndHalfredditData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(Post.GetRedditCsvHeader())
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
            post = Post(date, submission.id, submission.title, submission.selftext, submission.ups, submission.downs)
            Posts.append(post)

    # with open('redditData.csv', 'a', encoding='UTF8', newline='') as csvfile:
        for ii in range(len(Posts)-1):
            if (Posts[ii].Text != '[removed]') or (Posts[ii].Text != '[deleted]'):
                # writer = csv.writer(file)
                writer.writerow(Posts[ii].GetRedditCsvString())
        Posts = []
    # for i in range(len(Posts) - 1):
    #     if Posts[i].Text != '[removed]' or Posts[i].Text != '[deleted]':
    #         writer.writerow(Posts[i].GetRedditCsvString())


# psawSearch = api.search_submissions(
#             # after=timeAfter,
#             # before=timeBefore,
#             filter=['id'],
#             subreddit=subreddit,
#             limit=200000
# )
# Posts = []
# for submission_psaw in psawSearch:
#     submission_id = submission_psaw.d_['id']
#     submission = reddit.submission(id=submission_id)
#     date = datetime.utcfromtimestamp(submission.created_utc)
#     post = Post(date, submission.id, submission.title, submission.selftext, submission.ups, submission.downs)
#     Posts.append(post)
#
# with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(Post.GetRedditCsvHeader())
#     for i in range(len(Posts)-1):
#         if Posts[i].Text != '[removed]' or Posts[i].Text != '[deleted]':
#             writer.writerow(Posts[i].GetRedditCsvString())
