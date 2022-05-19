import san
import pandas as pd
import time
import datetime
from ethdataobject import ethdata
import csv

from_date = "2021-05-18"
to_date = "2022-05-18"
from_date_limited = "2021-05-18"
to_date_limited = "2022-05-18"
interval = "1h"

def GetDataFrameDictionary(dataframe, keyName, valueName):
    tempDict = dict()
    for index, row in dataframe.iterrows():
        tempDict[row[keyName]] = row[valueName]
    return tempDict
# ohlc_df = san.get("ohlc/ethereum", from_date=from_date, to_date=to_date, interval="1h")


Closeprice_df = san.get("price_usd/ethereum", from_date=from_date, to_date=to_date, interval=interval)
Ethspent_df = san.get("eth_spent_over_time/ethereum", from_date=from_date, to_date=to_date, interval=interval)
SocVolR_df = san.get("social_volume_reddit/ethereum", from_date=from_date, to_date=to_date, interval=interval) #no limit and no interval
GasUsed_df = san.get("avg_gas_used/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval=interval) #restrictedFrom: 2020-05-08T19:12:51Z', 'restrictedTo': '2022-04-08T19:12:51Z
SentPosR_df = san.get("sentiment_positive_reddit/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval=interval) #restrictedFrom': '2020-05-08T19:30:30Z', 'restrictedTo': '2022-04-08T19:30:30Z'
SentNegR_df = san.get("sentiment_negative_reddit/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval=interval) #'restrictedFrom': '2020-05-08T19:31:42Z', 'restrictedTo': '2022-04-08T19:31:42Z'
SentBalR_df = san.get("sentiment_balance_reddit/ethereum", from_date=from_date, to_date=to_date, interval=interval) #no limit and no interval
SentVolR_df = san.get("sentiment_volume_consumed_reddit/ethereum", from_date=from_date, to_date=to_date, interval=interval) #no limit and no interval
SocDomR_df = san.get("social_dominance_reddit/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval=interval) #restrictedFrom': '2020-05-08T19:45:11Z', 'restrictedTo': '2022-04-08T19:45:11Z'
DailyActiveAddresses_df = san.get("daily_active_addresses/ethereum", from_date=from_date, to_date=to_date, interval=interval) # 1d interval no limit
TransVolEth_df = san.get("transaction_volume/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval=interval) #'restrictedFrom': '2020-05-08T19:47:40Z', 'restrictedTo': '2022-04-08T19:47:40Z

# EthspentDict = Ethspent_df.to_dict('dict')
# Ethspent_df.assign(data=lambda x: x['index'].dt.date)[['data','value']].to_dict()
# print(EthspentDict)
# print(ClosepriceDict.keys())
# print(ClosepriceDict[datetime.datetime.strptime('2022-04-18 23:00:00', "%Y-%m-%d %H:%M:%S")])

ClosepriceDict = GetDataFrameDictionary(Closeprice_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
EthSpentdict = GetDataFrameDictionary(Ethspent_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','ethSpent']], 'data', 'ethSpent')
SocVolRDict = GetDataFrameDictionary(SocVolR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
GasUsedDict = GetDataFrameDictionary(GasUsed_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
SentPosRDict = GetDataFrameDictionary(SentPosR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
SentNegRDict = GetDataFrameDictionary(SentNegR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
SentBalRDict = GetDataFrameDictionary(SentBalR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
SentVolRDict = GetDataFrameDictionary(SentVolR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
SocDomRDict = GetDataFrameDictionary(SocDomR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
DailyActiveAddressesDict = GetDataFrameDictionary(DailyActiveAddresses_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
TransVolEthDict = GetDataFrameDictionary(TransVolEth_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']], 'data', 'value')
# print(ClosepriceDict)
# SocVolRDict = SocVolR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
# GasUsedDict = GasUsed_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
# SentPosRDict = SentPosR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
# SentNegRDict = SentNegR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
##  SentBalRDict = SentBalR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
## SentVolRDict = SentVolR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
# SocDomRDict = SocDomR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
# DailyActiveAddressesDict = DailyActiveAddresses_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
# TransVolEthDict = TransVolEth_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()

#For each data frame, convert into dictionary with Key = datetime, value = value

maxdate = pd.concat([Closeprice_df, Ethspent_df, SocVolR_df, GasUsed_df, SentPosR_df, SentNegR_df, SentBalR_df, SentVolR_df, SocDomR_df, DailyActiveAddresses_df, TransVolEth_df]).index.get_level_values(0).max()
mindate = pd.concat([Closeprice_df, Ethspent_df, SocVolR_df, GasUsed_df, SentPosR_df, SentNegR_df, SentBalR_df, SentVolR_df, SocDomR_df, DailyActiveAddresses_df, TransVolEth_df]).index.get_level_values(0).min()

# pd.date_range()
# minDate = min(all dictionary keys)
# maxDate = max(..)
# Time series list = Keys (mindate -> maxDate, increments of 3 hours)
timeSeries = pd.date_range(mindate, maxdate, freq="3H")
# print(timeSeries)

def GetEthDataValue(timeStamp, dictionary, nullValue):
    doesExist = timeStamp in ClosepriceDict
    value = dictionary[timeStamp] if doesExist else nullValue  # ternary operator
    return value

# For loop through each datetime in timeseries (i,.e. query each dictionary by date)
EthData = []
for i in range(len(timeSeries)-1):
    time = timeSeries[i]
    nullValue = ""
    Ethdata = ethdata(timeSeries[i], GetEthDataValue(time, ClosepriceDict, nullValue),
                      GetEthDataValue(time, TransVolEthDict, nullValue), GetEthDataValue(time, EthSpentdict, nullValue),
                      GetEthDataValue(time, SocVolRDict, nullValue), GetEthDataValue(time, GasUsedDict, nullValue),
                      GetEthDataValue(time, SentPosRDict, nullValue), GetEthDataValue(time, SentNegRDict, nullValue),
                      GetEthDataValue(time, SentBalRDict, nullValue), GetEthDataValue(time, SentVolRDict, nullValue),
                      GetEthDataValue(time, SocDomRDict, nullValue), GetEthDataValue(time, DailyActiveAddressesDict, nullValue))
    EthData.append(Ethdata)

print(EthData)
 #   Create an ethdata object and add it to the ethData list

with open('MarketData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(ethdata.GetEthdataCsvHeader())
    for i in range(len(EthData)-1):
        writer.writerow(EthData[i].GetEthdataCsvString())
