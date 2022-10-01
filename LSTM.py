from LSTMobject import LSTM
import scipy
import numpy
from matplotlib import pyplot
import pandas as pd
import statsmodels
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import csv

# Dataset
# Data = ['2022-05-18 00:00:00', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
# with open('FullData.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file, delimiter='�')
#     writer.writerow(['Date', 'WeightedAVG', 'TitleNegative', 'TitleNeutral', 'TitlePositive', 'TitleCompound', 'TextNegative', 'TextNeutral', 'TextPositive', 'TextCompound', 'Closeprice', 'TransactionVolume', 'EthSpentOverTime', 'SocialVolumeReddit', 'GasUsed', 'SentimentPosReddit', 'SentimentNegReddit', 'SentimentBalanceReddit', 'SentimentVolumeConsumedReddit', 'SocialDomReddit', 'DailyAddresses'])
#     i = 0
#     if i < 1:
#         writer.writerow(Data)
#         i = i + 1


#LOAD dataset
dataset = pd.read_csv('FullData.csv', delimiter='�', usecols=LSTM.GetLSTMCsvHeader(), index_col=0)
# print(dataset)
values = dataset.values
# specify columns to plot
groups = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
n = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, n)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    n += 1
# pyplot.show()

# DATA Preparations
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


# integer encode direction
encoder = LabelEncoder()
values[:, 4] = encoder.fit_transform(values[:, 4])
# ensure all data is float
values = values.astype('float32')
# normalize features
scaler = MinMaxScaler(feature_range=(0, 1))
scaled = scaler.fit_transform(values)
# frame as supervised learning
reframed = series_to_supervised(scaled, 1, 1)
# drop columns we don't want to predict
reframed.drop(reframed.columns[[21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]], axis=1, inplace=True)
print(reframed.head())

# DEFINE AND FIT MODEL
# split into train and test sets
values = reframed.values
n_train_hours =  * 24
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
train_X, train_y = train[:, :-1], train[:, -1]
test_X, test_y = test[:, :-1], test[:, -1]
# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)