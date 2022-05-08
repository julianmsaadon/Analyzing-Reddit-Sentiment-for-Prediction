import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from postobject import Post


with open('redditData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    posts = []
    for row in reader:
        posts.append(Post(row['Date'],row['ID'],row['Title'],row['Text'],row['Upvotes'],row['Downvotes']))

analyzer = SentimentIntensityAnalyzer()
# Sentiments = []
for post in posts:
    vsTitle = analyzer.polarity_scores(post.SentimentTitle())
    vsText = analyzer.polarity_scores(post.SentimentText())
    post.EnrichWithTitleSentimentResult(vsTitle)
    post.EnrichWithTextSentimentResult(vsText)
    # post.GetTitleCompound()
    # post.GetTextCompound()
    # post.GetTitleNeutral()
    # post.GetTextNeutral()
    # post.GetTitlePositive()
    # post.GetTextPositive()
    # post.GetTitleNegative()
    # post.GetTitleNegative()

    # sentiment = [post.GetTitleCompound(), post.GetTitleNeutral(), post.GetTitlePositive(), post.GetTitleNegative(), post.GetTextCompound(), post.GetTextNeutral(), post.GetTextPositive(), post.GetTitleNegative()]
    # Sentiments.append(sentiment)

for i in range(len(posts)-1):
    print(posts[i].GetTitleCompound())

with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(Post.GetSentimentCsvHeader())
    for i in range(len(posts)-1):
        if posts[i].GetTitleCompound() != 0.0 and posts[i].GetTextCompound() != 0.0:
            writer.writerow(posts[i].GetSentimentCsvString())
