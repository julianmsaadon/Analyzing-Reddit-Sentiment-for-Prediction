class ethdata:

    def __init__(self, Date, Closeprice, TransactionVolume, EthSpentOverTime, SocialVolumeReddit, GasUsed, SentimentPosReddit, SentimentNegReddit, SentimentBalanceReddit, SentimentVolumeConsumedReddit, SocialDomReddit, DailyAddresses):
        self.Date = Date
        self.Closeprice = Closeprice
        self.TransactionVolume = TransactionVolume
        self.EthSpentOverTime = EthSpentOverTime
        self.SocialVolumeReddit = SocialVolumeReddit
        self.GasUsed = GasUsed
        self.SentimentPosReddit = SentimentPosReddit
        self.SentimentNegReddit = SentimentNegReddit
        self.SentimentBalanceReddit = SentimentBalanceReddit
        self.SentimentVolumeConsumedReddit = SentimentVolumeConsumedReddit
        self.SocialDomReddit = SocialDomReddit
        self.DailyAddresses = DailyAddresses

    @staticmethod
    def GetEthdataCsvHeader():
        return ['Date', 'Closeprice', 'TransactionVolume', 'EthSpentOverTime', 'SocialVolumeReddit', 'GasUsed', 'SentimentPosReddit', 'SentimentNegReddit', 'SentimentBalanceReddit', 'SentimentVolumeConsumedReddit', 'SocialDomReddit', 'DailyAddresses']

    def GetEthdataCsvString(self):
        return [self.Date, self.Closeprice, self.TransactionVolume, self.EthSpentOverTime, self.SocialVolumeReddit, self.GasUsed, self.SentimentPosReddit, self.SentimentNegReddit, self.SentimentBalanceReddit, self.SentimentVolumeConsumedReddit, self.SocialDomReddit, self.DailyAddresses]

    def GetReadethdataCsv(row):
        return ethdata(row['Date'], row['Closeprice'], row['TransactionVolume'], row['EthSpentOverTime'], row['SocialVolumeReddit'], row['GasUsed'], row['SentimentPosReddit'], row['SentimentNegReddit'], row['SentimentBalanceReddit'], row['SentimentVolumeConsumedReddit'], row['SocialDomReddit'], row['DailyAddresses'])

    def GetEthdataInfo(self):
        return [self.Closeprice, self.TransactionVolume, self.EthSpentOverTime, self.SocialVolumeReddit, self.GasUsed,
                self.SentimentPosReddit, self.SentimentNegReddit, self.SentimentBalanceReddit,
                self.SentimentVolumeConsumedReddit, self.SocialDomReddit, self.DailyAddresses]

    def GetEthVal(self):
        return self.Closeprice, self.TransactionVolume, self.EthSpentOverTime, self.SocialVolumeReddit, self.GasUsed, self.SentimentPosReddit, self.SentimentNegReddit, self.SentimentBalanceReddit, self.SentimentVolumeConsumedReddit, self.SocialDomReddit, self.DailyAddresses
