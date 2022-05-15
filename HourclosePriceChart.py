import matplotlib.pyplot as plt
from ethdataobject import ethdata
import san
import csv
import pandas as pd
Columns = ethdata.GetEthdataCsvHeader()
Ethdata = pd.read_csv("MarketData.csv", usecols=Columns)

# with open('MarketData.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     Ethdata = []
#     EthdataCloseprice = []
#     for row in reader:
#         Ethdata.append(ethdata.GetReadethdataCsv(row))

from_date = "2020-04-17"
to_date = "2022-04-18"
interval = "1h"
Closeprice_df = san.get("price_usd/ethereum", from_date=from_date, to_date=to_date, interval=interval)

plt.plot(Closeprice_df.index, Closeprice_df.value)
plt.title('ClosePrice per Hour')
plt.xlabel('Hour')
plt.ylabel('Close Price')
plt.show()
