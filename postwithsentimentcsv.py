import csv
from main import dates, ids, titles, selftext, upvotes, downvotes
from SentimentAnalysis import sentiment
header = ['Date', 'ID', 'Title', 'Text', 'Sentiment', 'Upvotes', 'Downvotes']

with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(dates)-1):
        writer.writerow([dates[i], ids[i], titles[i], selftext[i], sentiment[i], upvotes[i], downvotes[i]])