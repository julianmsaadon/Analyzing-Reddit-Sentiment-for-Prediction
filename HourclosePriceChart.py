import matplotlib.pyplot as plt
from ethdataobject import ethdata
import csv

with open('MarketData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    Ethdata = []
    EthdataCloseprice = []
    for row in reader:
        Ethdata.append(ethdata(row['Date']), ethdata(row['Closeprice']))

plt.plot(Ethdata(row['Date']), Ethdata(row['Date']))
plt.title('ClosePrice per Hour')
plt.xlabel('Hour')
plt.ylabel('Close Price')
plt.show()
