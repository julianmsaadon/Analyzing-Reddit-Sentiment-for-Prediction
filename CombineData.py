import csv
from SentimentObject import Sentiment
import math
import datetime
from datetime import timedelta
import pandas

sentiments = []

with open('postSentiment.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='�')
    for row in reader:
        sentiments.append(Sentiment.GetReadSentimentCsv(row))
print(len(sentiments))

for sentiment in sentiments:
    sentiment.Date = sentiment.GetStrptimeDate()
    if int(sentiment.Date.hour) + 3 >= 24:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=24)
    elif int(sentiment.Date.hour) + 3 >= 21:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=21)
    elif int(sentiment.Date.hour) + 3 >= 18:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=18)

    elif int(sentiment.Date.hour) + 3 >= 15:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=15)

    elif int(sentiment.Date.hour) + 3 >= 12:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=12)

    elif int(sentiment.Date.hour) + 3 >= 9:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=9)

    elif int(sentiment.Date.hour) + 3 >= 6:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=6)

    elif int(sentiment.Date.hour) + 3 >= 3:
        DateBefore = datetime.datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=3)

    # sentiment.Date = sentiment.Date.timestamp()
    print(sentiment.Date)
    # sentiment.Date = math.ceil(sentiment.Date)
    # sentiment.Date = pandas.Series(sentiment.Date).dt.round('3H')
    # sentiment.Date = sentiment.GetStrptimeDate()

# def ceil_dt(dt, delta):
#     return datetime.min + math.ceil((dt - datetime.min) / delta) * delta

# round(freq = 'D')
# print(ceil_dt(datetime(2012, 10, 25, 17, 32, 16), timedelta(minutes=15)))
# for sentiment in sentiments:
#     sentiment.Date = pandas.Series(sentiment.Date).dt.round('3H')
        # ceil(freq='3H')
    print(sentiment.Date)

# for sentiment in range(len(sentiments)-1):
#     sentiment.Date = sentiment.GetTupleDate()