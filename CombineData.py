import csv
import pandas as pd
from SentimentObject import Sentiment
from ethdataobject import ethdata
from datetime import timedelta, datetime


sentiments = []

with open('postSentiment.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='�')
    for row in reader:
        sentiments.append(Sentiment.GetReadSentimentCsv(row))
print(len(sentiments))

ethdatas = []

with open('MarketData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ethdatas.append(ethdata.GetReadethdataCsv(row))
print(len(ethdatas))

timeSeries = []
for sentiment in sentiments:
    sentiment.Date = sentiment.GetStrptimeDate()
    if int(sentiment.Date.hour) + 3 >= 24:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=24)

    elif int(sentiment.Date.hour) + 3 >= 21:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=21)

    elif int(sentiment.Date.hour) + 3 >= 18:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=18)

    elif int(sentiment.Date.hour) + 3 >= 15:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=15)

    elif int(sentiment.Date.hour) + 3 >= 12:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=12)

    elif int(sentiment.Date.hour) + 3 >= 9:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=9)

    elif int(sentiment.Date.hour) + 3 >= 6:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=6)

    elif int(sentiment.Date.hour) + 3 >= 3:
        DateBefore = datetime(sentiment.Date.year,
                                       sentiment.Date.month,
                                       sentiment.Date.day,
                                       0, 0)
        sentiment.Date = DateBefore + timedelta(hours=3)
    timeSeries.append(sentiment.Date)

# print(sentiment.Date)
# for i in timeSeries:
#     timeSeries[i] = datetime.datetime.strptime(timeSeries[i], "%Y-%m-%d %H:%M:%S")
# mindate = datetime.datetime(2021, 5, 18, 0, 0, 0)
# maxdate = datetime.datetime(2022, 5, 19, 0, 0, 0)
# print(maxdate)
# timeSeries = pandas.date_range(mindate, maxdate, freq="3H")
# timeSeries.to_pydatetime()
# print(timeSeries)
    # .strftime("%Y-%m-%d %H:%M:%S")
# for i in timeSeries:
#     timeSeries[i].replace("'","")
# print(timeSeries)
ethSeries = []
for ethdata in ethdatas:
    # print(type(datetime.strptime('2022-05-18 15:00:00', '%Y-%m-%d %H:%M:%S')))
    # print(ethdata.Date[0:4])
    # ethdata.Date = datetime.datetime(int(ethdata.Date[0:4]),
    #                                  int(ethdata.Date[5:7]),
    #                                  int(ethdata.Date[8:10]),
    #                                  int(ethdata.Date[11:13]),
    #                                  int(ethdata.Date[14:16]),
    #                                  int(ethdata.Date[17:19]))

    ethdata.Date = datetime.strptime(ethdata.Date, '%Y-%m-%d %H:%M:%S')
    ethSeries.append(ethdata.Date)
    # print(ethdata.Date)
# for i in range(len(timeSeries)-1):
#     for n in ethSeries:
#         if ethSeries[n] == timeSeries[i]:
#             print("yaay")


ethDict = {}
for i in ethSeries:
    ethDict[i] = []

sentDict = {}
for i in timeSeries:
    sentDict[i] = []


# for ethdata in ethdatas:
#     ethDict[ethdata.Date] = [ethdata.GetEthdataInfo()]

def add_values_in_dict(dict, key, list_of_values):
    if key not in dict:
        dict[key] =  [] # list()
    dict[key].extend(list_of_values)
    return dict

# sentDict = {datetime.datetime : [], ...}
for key in sentDict:
    for sentiment in sentiments:
        if sentiment.Date == key:
            sentDict = add_values_in_dict(sentDict, key, sentiment.GetSentimentInfo())
# x = 0
# if x < 10:

# print(sentDict)
            # extend(sentiment.GetSentimentInfo())

# Adds key date and values for ethdata
for key in ethDict:
    for ethdata in ethdatas:
        if ethdata.Date == key:
            ethDict = add_values_in_dict(ethDict, key, ethdata.GetEthdataInfo())
# print(ethDict)

# masterDict = {}
# for ethKey in ethDict:
#     for sentKey in sentDict:
#         if ethDict.get(ethKey) == sentDict.get(sentKey):
#             print("yay")
            # masterDict = {ethKey: [sentDict[sentKey], ethDict[ethKey]]}
# print(masterDict)
# print(sentDict)



# print(timeSeries)
# SentimentDict = {}

# print(SentimentDict)
