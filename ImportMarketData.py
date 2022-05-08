import san
from ethdataobject import ethdata
import datetime
import csv
from_date = "2020-04-17"
to_date = "2022-04-18"
from_date_limited = "2020-05-08"
to_date_limited = "2022-04-08"
# add

ohlc_df = san.get("ohlc/ethereum", from_date=from_date, to_date=to_date, interval="1h")
Ethspent_df = san.get("eth_spent_over_time/ethereum", from_date=from_date, to_date=to_date, interval="1h")
SocVolR_df = san.get("social_volume_reddit/ethereum", from_date=from_date, to_date=to_date, interval="1h") #no limit and no interval
GasUsed_df = san.get("avg_gas_used/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval="1h") #restrictedFrom: 2020-05-08T19:12:51Z', 'restrictedTo': '2022-04-08T19:12:51Z
SentPosR_df = san.get("sentiment_positive_reddit/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval="1h") #restrictedFrom': '2020-05-08T19:30:30Z', 'restrictedTo': '2022-04-08T19:30:30Z'
SentNegR_df = san.get("sentiment_negative_reddit/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval="1h") #'restrictedFrom': '2020-05-08T19:31:42Z', 'restrictedTo': '2022-04-08T19:31:42Z'
SentBalR_df = san.get("sentiment_balance_reddit/ethereum", from_date=from_date, to_date=to_date, interval="1h") #no limit and no interval
SentVolR_df = san.get("sentiment_volume_consumed_reddit/ethereum", from_date=from_date, to_date=to_date, interval="1h") #no limit and no interval
SocDomR_df = san.get("social_dominance_reddit/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval="1h") #restrictedFrom': '2020-05-08T19:45:11Z', 'restrictedTo': '2022-04-08T19:45:11Z'
DailyActiveAddresses_df = san.get("daily_active_addresses/ethereum", from_date=from_date, to_date=to_date, interval="1h") # 1d interval no limit
TransVolEth_df = san.get("transaction_volume/ethereum", from_date=from_date_limited, to_date=to_date_limited, interval="1h") #'restrictedFrom': '2020-05-08T19:47:40Z', 'restrictedTo': '2022-04-08T19:47:40Z


closeprice = ohlc_df['closePriceUsd'].tolist()
# time = ohlc_df['datetime'].tolist()
# print(closeprice)
print(ohlc_df)
# print(Ethspent_df)
# print(SocVolR_df)
# print(GasUsed_df)
# print(SentPosR_df)
# print(SentNegR_df)
# print(SentBalR_df)
# print(SentVolR_df)
# print(SocDomR_df)
# print(DailyActiveAddresses_df)
# print(TransVolEth_df)
need = san.metadata(
    "transaction_volume",
    arr=['availableSlugs', 'defaultAggregation', 'humanReadableName', 'isAccessible', 'isRestricted', 'restrictedFrom', 'restrictedTo']
)
# print(need)


Ethdata = []

for item in ohlc_df:
    value = ethdata(ohlc_df['datetime'].iloc['value'], ohlc_df['closePriceUsd'], TransVolEth_df['value'], Ethspent_df['value'], SocVolR_df['value'], GasUsed_df['value'], SentPosR_df['value'], SentNegR_df['value'], SentBalR_df['value'], SentVolR_df['value'], SocDomR_df['value'], DailyActiveAddresses_df['value'])
    Ethdata.append(value)

with open('MarketData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(ethdata.GetEthdataCsvHeader())
    for i in range(len(Ethdata)-1):
        writer.writerow(Ethdata[i].GetEthdataCsvString())
