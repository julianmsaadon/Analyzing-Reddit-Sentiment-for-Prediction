import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from postobject import Post
import pandas as pd


# print(repr(open('/Users/JMSaadon/PycharmProjects/PycharmRedditSentimentAnalysis/redditData.csv', 'rb').read(200))) # dump 1st 200 bytes of file
# data = open('/Users/JMSaadon/PycharmProjects/PycharmRedditSentimentAnalysis/redditData.csv', 'rb').read()
# print(data.find('\x00'))
# print(data.count('\x00'))
#
# with open('OfficialRedditPosts.csv') as csvfile:
#     uncleanedPosts = []
#     count = 0
#     reader = csv.DictReader(csvfile, delimiter='�')
#     for row in reader:
#         uncleanedPosts.append(Post.GetReadRedditCsv(row))
#         count = count + 1
#         if count == 75000:
#             break
#         print(count)
# print(len(uncleanedPosts))

# 2nd half
with open('Last15000Posts.csv') as csvfile:
    uncleanedPosts = []
    count = 0
    reader = csv.DictReader(csvfile, delimiter='�')
    for row in reader:
        uncleanedPosts.append(Post.GetReadRedditCsv(row))
        count = count + 1
        print(count)
print(len(uncleanedPosts))

# need logic for removing duplicate posts
posts = []
for post in uncleanedPosts:
    if post.ID not in posts:
        posts.append(post)
print(len(posts))

#
analyzer = SentimentIntensityAnalyzer()
for post in posts:
    vsTitle = analyzer.polarity_scores(post.SentimentTitle())
    vsText = analyzer.polarity_scores(post.SentimentText())
    post.EnrichWithTitleSentimentResult(vsTitle)
    post.EnrichWithTextSentimentResult(vsText)

# with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file, delimiter='�')
#     writer.writerow(Post.GetSentimentCsvHeader())
#     for i in range(len(posts)-1):
#         if (posts[i].GetTitleCompound() != 0.0) or (posts[i].GetTextCompound() != 0.0):
#             posts[i].SetWeight(0.7)
#             if posts[i].GetTitleCompound() == 0.0:
#                 posts[i].SetWeight(0.0)
#             elif posts[i].GetTextCompound() == 0.0:
#                 posts[i].SetWeight(1.0)
#             writer.writerow(posts[i].GetSentimentCsvString())

# 2nd half
with open('postSentiment.csv', 'a', encoding='UTF8', newline='') as file:
    writer = csv.writer(file, delimiter='�')
    # writer.writerow(Post.GetSentimentCsvHeader())
    for i in range(len(posts)-1):
        if (posts[i].GetTitleCompound() != 0.0) or (posts[i].GetTextCompound() != 0.0):
            posts[i].SetWeight(0.7)
            if posts[i].GetTitleCompound() == 0.0:
                posts[i].SetWeight(0.0)
            elif posts[i].GetTextCompound() == 0.0:
                posts[i].SetWeight(1.0)
            writer.writerow(posts[i].GetSentimentCsvString())

