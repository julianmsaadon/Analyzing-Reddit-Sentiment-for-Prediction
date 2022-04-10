import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from postobject import Post

with open('redditData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    title = []
    posts = []
    for row in reader:
        posts.append(Post(row['Date'],row['ID'],row['Title'],row['Text'],row['Upvotes'],row['Downvotes']))
        print(row['Title'])
        title.append(row['Title'])

analyzer = SentimentIntensityAnalyzer()


sentiment = []
Compound = []
Neutral = []
Negative = []
Positive = []
for post in posts:
        vs = analyzer.polarity_scores(post.SentimentText())
        print("{:-<65} {}".format(post.SentimentText(), str(vs)))
        post.EnrichWithSentimentResult(vs)
        post.GetCompound()
        post.GetNeutral()
        post.GetPositive()
        post.GetNegative()
        Negative.append(post.GetNegative())
        Neutral.append(post.GetPositive())
        Compound.append(post.GetCompound())
        Positive.append(post.GetPositive())

