import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from postobject import Post
import pandas as pd


with open('redditData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    posts = []
    for row in reader:
        # add in removed and deleted logic
        posts.append(Post.GetReadRedditCsv(row))

analyzer = SentimentIntensityAnalyzer()
for post in posts:
    vsTitle = analyzer.polarity_scores(post.SentimentTitle())
    vsText = analyzer.polarity_scores(post.SentimentText())
    post.EnrichWithTitleSentimentResult(vsTitle)
    post.EnrichWithTextSentimentResult(vsText)

with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(Post.GetSentimentCsvHeader())
    for i in range(len(posts)-1):
        if (posts[i].GetTitleCompound() != 0.0) or (posts[i].GetTextCompound() != 0.0):
            posts[i].SetWeight(0.7)
            if posts[i].GetTitleCompound() == 0.0:
                posts[i].SetWeight(0.0)
            elif posts[i].GetTextCompound() == 0.0:
                posts[i].SetWeight(1.0)
            writer.writerow(posts[i].GetSentimentCsvString())

