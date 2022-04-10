import san

ohlc_df = san.get("ohlc/ethereum", from_date="2022-04-17", to_date="2022-04-18", interval="1h")

print(ohlc_df)
closeprice = ohlc_df['closePriceUsd'].tolist()
print(closeprice)


