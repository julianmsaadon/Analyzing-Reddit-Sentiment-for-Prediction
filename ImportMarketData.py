import san
import datetime

ohlc_df = san.get("ohlc/ethereum", from_date="2021-04-17", to_date="2022-04-18", interval="1h")
Ethspent_df = san.get("eth_spent_over_time/ethereum", from_date="2022-04-17", to_date="2022-04-18", interval="1h")
SocVolR_df = san.get("social_volume_reddit/ethereum", from_date="2022-04-17", to_date="2022-04-18", interval="1h")
GasUsed_df = san.get("gas_used/ethereum", from_date="2022-03-18", to_date="2022-03-18", interval="1h")
SentPosR_df = san.get("sentiment_positive_reddit/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1h")
SentNegR_df = san.get("sentiment_negative_reddit/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1h")
SentBalR_df = san.get("sentiment_balance_reddit/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1h")
SentVolR_df = san.get("sentiment_volume_consumed_reddit/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1h")
SocDomR_df = san.get("social_dominance_reddit/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1h")
DailyActiveAddresses_df = san.get("daily_active_addresses/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1d")
TransVolEth_df = san.get("transaction_volume/ethereum", from_date="2022-03-17", to_date="2022-03-18", interval="1h")


closeprice = ohlc_df['closePriceUsd'].tolist()
# time = ohlc_df['datetime'].tolist()
print(closeprice)
print(ohlc_df)
print(Ethspent_df)
print(SocVolR_df)
print(GasUsed_df)
print(SentPosR_df)
print(SentNegR_df)
print(SentBalR_df)
print(SentVolR_df)
print(SocDomR_df)
print(DailyActiveAddresses_df)
print(TransVolEth_df)
# need = san.metadata(
#     "avg_gas_used",
#     arr=['availableSlugs', 'defaultAggregation', 'humanReadableName', 'isAccessible', 'isRestricted', 'restrictedFrom', 'restrictedTo']
# )

# print(need)