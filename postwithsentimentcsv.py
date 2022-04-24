import csv
from main import dates, ids, titles, selftext, upvotes, downvotes
header = ['Date', 'ID', 'Title', 'Text', 'Upvotes', 'Downvotes']

with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(dates)-1):
        writer.writerow([dates[i], ids[i], titles[i], selftext[i], upvotes[i], downvotes[i]])






# import csv
# from main import dates, ids, titles, selftext, upvotes, downvotes
# from SentimentAnalysis import sentiment, Negative, Neutral, Positive, Compound
#
#
# header = ['Date', 'ID', 'Title', 'Text', 'Sentiment', 'Negative', 'Neutral', 'Positive', 'Compound','Upvotes', 'Downvotes']
#
# with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     for i in range(len(dates)-1):
#         writer.writerow([dates[i], ids[i], titles[i], selftext[i], sentiment[], Negative[i], Neutral[i], Positive[i], Compound[i], upvotes[i], downvotes[i]])
#

#
