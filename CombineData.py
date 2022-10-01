import csv
import pandas as pd
from SentimentObject import Sentiment
from ethdataobject import ethdata
from datetime import timedelta, datetime
from FlattenedObject import FlatSent
from LSTMobject import LSTM
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
    # ethdata.Date = datetime.strptime(ethdata.Date, '%Y-%m-%d %H:%M:%S')
    ethSeries.append(ethdata.Date)

ethDict = {}
for i in ethSeries:
    ethDict[i] = None #[]

# sentDict = {}
# for i in timeSeries:
#     sentDict[i] = []

# for ethdata in ethdatas:
#     ethDict[ethdata.Date] = [ethdata.GetEthdataInfo()]

# def add_values_in_dict(dict, key, list_of_values):
#     if key not in dict:
#         dict[key] =  [] # list()
#     dict[key].extend(list_of_values)
#     return dict

# sentDict = {datetime.datetime : [], ...}
sentDict = {}
# sentDict = {sentiment.Date: [] for sentiment in sentiments}
# for i in sentDict:
#     if SentDict[i] ==
# for key in sentDict:
#     for sentiment in sentiments:
#         if sentiment.Date == key:
#             sentDict[key] = sentiment.GetSentimentInfo()
#
for sentiment in sentiments:
    key = sentiment.Date.strftime('%Y-%m-%d %H:%M:%S')
    tempArray = sentDict.get(key)
    if tempArray is None:
        # print(f"{key} is not in the dict yet!")
        sentDict[key] = [sentiment] #.GetSentimentInfo()
    else:
        tempArray.append(sentiment) #.GetSentimentInfo()
        sentDict[key] = tempArray
        # sentDict[key] = tempArray.append(sentiment.GetSentimentInfo())
        # print(f"{key} is now {sentDict[key]}")

# print(sentDict)
# x = 0
# if x < 10:

# print(sentDict)
            # extend(sentiment.GetSentimentInfo())

# Adds key date and values for ethdata
ethDict = {}
for ethdata in ethdatas:
    key = ethdata.Date
    tempArray = ethDict.get(key)
    if tempArray is None:
        ethDict[key] = ethdata #[ethdata.GetEthdataInfo()]
    else:
        print("Two lines items exist for " + key)
        ethDict[key] = tempArray.append(ethdata) #tempArray.append(ethdata.GetEthdataInfo())
# print(ethDict)

flattenedSentDict = {}
#USE THIS FOR FLATTENING
for i in sentDict:
    # sentDict[i] = [post1, post2,post3...]
    weightedAverageNumerator = 0
    weightedAverageDenominator = 0
    titleNegAverageNumerator = 0
    titleNegAverageDenominator = 0
    titleNeutAverageNumerator = 0
    titleNeutAverageDenominator = 0
    titlePosAverageNumerator = 0
    titlePosAverageDenominator = 0
    titleCompAverageNumerator = 0
    titleCompAverageDenominator = 0
    textNegAverageNumerator = 0
    textNegAverageDenominator = 0
    textNeutAverageNumerator = 0
    textNeutAverageDenominator = 0
    textPosAverageNumerator = 0
    textPosAverageDenominator = 0
    textCompAverageNumerator = 0
    textCompAverageDenominator = 0
    for j in sentDict[i]:
        # print(j)
        sentiment = j
        # print(post[10])
        weight = (1 + int(sentiment.Upvotes) + int(sentiment.Downvotes))
        weightedAverageNumerator = weightedAverageNumerator + (weight * float(sentiment.WeightedAVG))
        weightedAverageDenominator = weightedAverageDenominator + weight
        titleNegAverageNumerator = titleNegAverageNumerator + (weight * float(sentiment.TitleNegative))
        titleNegAverageDenominator = titleNegAverageDenominator + weight
        titleNeutAverageNumerator = titleNeutAverageNumerator + (weight * float(sentiment.TitleNeutral))
        titleNeutAverageDenominator = titleNeutAverageDenominator + weight
        titlePosAverageNumerator = titlePosAverageNumerator + (weight * float(sentiment.TitlePositive))
        titlePosAverageDenominator = titlePosAverageDenominator + weight
        titleCompAverageNumerator = titleCompAverageNumerator + (weight * float(sentiment.TitleCompound))
        titleCompAverageDenominator = titleCompAverageDenominator + weight
        textNegAverageNumerator = titleNegAverageNumerator + (weight * float(sentiment.TextNegative))
        textNegAverageDenominator = textNegAverageDenominator + weight
        textNeutAverageNumerator = titleNeutAverageNumerator + (weight * float(sentiment.TextNeutral))
        textNeutAverageDenominator = textNeutAverageDenominator + weight
        textPosAverageNumerator = titlePosAverageNumerator + (weight * float(sentiment.TextPositive))
        textPosAverageDenominator = textPosAverageDenominator + weight
        textCompAverageNumerator = titleCompAverageNumerator + (weight * float(sentiment.TextCompound))
        textCompAverageDenominator = textCompAverageDenominator + weight
    flattenedSentDict[i] = FlatSent(weightedAverageNumerator/weightedAverageDenominator,
                                    titleNegAverageNumerator/titleNegAverageDenominator,
                                    titleNeutAverageNumerator/titleNeutAverageDenominator,
                                    titlePosAverageNumerator/titlePosAverageDenominator,
                                    titleCompAverageNumerator/titleCompAverageDenominator,
                                    textNegAverageNumerator/textNegAverageDenominator,
                                    textNeutAverageNumerator/textNeutAverageDenominator,
                                    textPosAverageNumerator/textPosAverageDenominator,
                                    textCompAverageNumerator/textCompAverageDenominator)
# print(flattenedSentDict)
masterDict = {}
# for ethKey in ethDict:
#     for sentKey in sentDict:
#         if ethDict.get(ethKey) == sentDict.get(sentKey):
#             print("yay")
#             masterDict = {ethKey: [sentDict[sentKey], ethDict[ethKey]]} <-- flatten this into an object
# counter = 0
for i in timeSeries:
    i = i.strftime('%Y-%m-%d %H:%M:%S')
    # counter = counter + 1
    # print(i)
    # print(counter)
    ethVal = ethDict.get(i)
    sentVal = flattenedSentDict.get(i)
    # print(ethVal)
    print(sentVal)
    if ethVal is not None and sentVal is not None:
        # FlatSent.GetSentVal(sentVal)
        # ethdata.GetEthVal(ethVal)
        masterDict[i] = LSTM(i, sentVal.WeightedAVG, sentVal.TitleNegative, sentVal.TitleNeutral, sentVal.TitlePositive,
                             sentVal.TitleCompound, sentVal.TextNegative, sentVal.TextNeutral, sentVal.TextPositive,
                             sentVal.TextCompound, ethVal.Closeprice, ethVal.TransactionVolume, ethVal.EthSpentOverTime,
                             ethVal.SocialVolumeReddit, ethVal.GasUsed, ethVal.SentimentPosReddit, ethVal.SentimentNegReddit,
                             ethVal.SentimentBalanceReddit, ethVal.SentimentVolumeConsumedReddit, ethVal.SocialDomReddit,
                             ethVal.DailyAddresses)
                             #LSTM.GetEthVal(ethVal))
        # print(FlatSent)
        # LSTM = LSTM.HydrateLSTM()
        # masterDict[i] = LSTM(LSTM.GetSentVal(sentVal), LSTM.GetEthVal(ethVal))
print(masterDict)
with open('FullData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file, delimiter='�')# print(masterDict)
    writer.writerow(LSTM.GetLSTMCsvHeader())
    for i in masterDict:
        LSTMVal = masterDict.get(i)
        writer.writerow(LSTMVal.GetLSTMcsvString())
# print(sentDict)



# print(timeSeries)
# SentimentDict = {}

# print(SentimentDict)
