import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

with open('redditData.csv') as csvfile:
    reader = csv.DictReader(csvfile)


    title = []
    for row in reader:
        print(row['Title'])
        title.append(row['Title'])

analyzer = SentimentIntensityAnalyzer()


sentiment = []
for sentence in title:
        vs = analyzer.polarity_scores(sentence)
        print("{:-<65} {}".format(sentence, str(vs)))
        sentiment.append(vs)
# print(sentiment)




