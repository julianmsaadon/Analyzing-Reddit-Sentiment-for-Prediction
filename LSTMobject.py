class LSTMobject:
    # def __init(self, ethVal, sentVal):
    #     self.Date = ethVal.Date



    def __init__(self, Date, WeightedAVG, TitleNegative, TitleNeutral, TitlePositive, TitleCompound, TextNegative, TextNeutral, TextPositive, TextCompound, Closeprice, TransactionVolume, EthSpentOverTime, SocialVolumeReddit, GasUsed, SentimentPosReddit, SentimentNegReddit, SentimentBalanceReddit, SentimentVolumeConsumedReddit, SocialDomReddit, DailyAddresses):
        self.Date = Date
        self.WeightedAVG = WeightedAVG
        self.TitleNegative = TitleNegative
        self.TitleNeutral = TitleNeutral
        self.TitlePositive = TitlePositive
        self.TitleCompound = TitleCompound
        self.TextNegative = TextNegative
        self.TextNeutral = TextNeutral
        self.TextPositive = TextPositive
        self.TextCompound = TextCompound
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

    # def GetSentVal(self):
    #     return self.WeightedAVG, self.TitleNegative, self.TitleNeutral, self.TitlePositive, self.TitleCompound, self.TextNegative, self.TextNeutral, self.TextPositive, self.TextCompound

    def GetEthVal(self):
        return self.Closeprice, self.TransactionVolume, self.EthSpentOverTime, self.SocialVolumeReddit, self.GasUsed, self.SentimentPosReddit, self.SentimentNegReddit, self.SentimentBalanceReddit, self.SentimentVolumeConsumedReddit, self.SocialDomReddit, self.DailyAddresses

    # def HydrateLSTM(self):
    #     return self.GetSentVal(), self.GetEthVal()
    def GetLSTMcsvString(self):
        return [self.Date, self.WeightedAVG, self.TitleNegative, self.TitleNeutral, self.TitlePositive, self.TitleCompound, self.TextNegative, self.TextNeutral, self.TextPositive, self.TextCompound, self.Closeprice, self.TransactionVolume, self.EthSpentOverTime, self.SocialVolumeReddit, self.GasUsed, self.SentimentPosReddit, self.SentimentNegReddit, self.SentimentBalanceReddit, self.SentimentVolumeConsumedReddit, self.SocialDomReddit, self.DailyAddresses]
    @staticmethod
    def GetLSTMCsvHeader():
        return ['Date', 'WeightedAVG', 'TitleNegative', 'TitleNeutral', 'TitlePositive', 'TitleCompound', 'TextNegative', 'TextNeutral', 'TextPositive', 'TextCompound', 'Closeprice', 'TransactionVolume', 'EthSpentOverTime', 'SocialVolumeReddit', 'GasUsed', 'SentimentPosReddit', 'SentimentNegReddit', 'SentimentBalanceReddit', 'SentimentVolumeConsumedReddit', 'SocialDomReddit', 'DailyAddresses']