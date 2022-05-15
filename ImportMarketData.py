import san
import pandas as pd
from ethdataobject import ethdata
import datetime
import csv
from_date = "2020-04-17"
to_date = "2022-04-18"
from_date_limited = "2020-05-08"
to_date_limited = "2022-04-08"
interval = "1h"
# add

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

ClosepriceDict = Closeprice_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
Ethdict = Ethspent_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','ethSpent']].to_dict()
# print(Ethdict)
SocVolRDict = SocVolR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
GasUsedDict = GasUsed_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
SentPosRDict = SentPosR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
SentNegRDict = SentNegR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
SentBalRDict = SentBalR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
SentVolRDict = SentVolR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
SocDomRDict = SocDomR_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
DailyActiveAddressesDict = DailyActiveAddresses_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
TransVolEthDict = TransVolEth_df.reset_index().assign(data=lambda x: x['datetime'].dt.tz_localize(None))[['data','value']].to_dict()
#For each data frame, convert into dictionary with Key = datetime, value = value

maxdate = pd.concat([Ethspent_df, SocVolR_df, GasUsed_df, SentPosR_df, SentNegR_df, SentBalR_df, SentVolR_df, SocDomR_df, DailyActiveAddresses_df, TransVolEth_df]).index.get_level_values(0).max()
# print(maxdate)
mindate = pd.concat([Ethspent_df, SocVolR_df, GasUsed_df, SentPosR_df, SentNegR_df, SentBalR_df, SentVolR_df, SocDomR_df, DailyActiveAddresses_df, TransVolEth_df]).index.get_level_values(0).min()
# print(mindate)
# pd.date_range()
# minDate = min(all dictionary keys)
# maxDate = max(..)
# Time series list = Keys (mindate -> maxDate, increments of 3 hours)
timeseries = pd.date_range(mindate, maxdate, freq="3H")
print(timeseries)

# For loop through each datetime in timeseries (i,.e. query each dictionary by date)
EthData = []
for i in range(len(timeseries)-1):
    # Ethdata = ethdata(Date, Closeprice, TransactionVolume, EthSpentOverTime, SocialVolumeReddit, GasUsed, SentimentPosReddit, SentimentNegReddit, SentimentBalanceReddit, SentimentVolumeConsumedReddit, SocialDomReddit, DailyAddresses)
    # EthData.append(Ethdata)

 #   Create an ethdata object and add it to the ethData list

# closeprice = ohlc_df['closePriceUsd'].tolist()




# for item in ohlc_df:
#     value = ethdata(ohlc_df['datetime'].iloc['value'], ohlc_df['closePriceUsd'], TransVolEth_df['value'], Ethspent_df['value'], SocVolR_df['value'], GasUsed_df['value'], SentPosR_df['value'], SentNegR_df['value'], SentBalR_df['value'], SentVolR_df['value'], SocDomR_df['value'], DailyActiveAddresses_df['value'])
#     Ethdata.append(value)
#
with open('MarketData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(ethdata.GetEthdataCsvHeader())
    for i in range(len(EthData)-1):
        writer.writerow(EthData[i].GetEthdataCsvString())
