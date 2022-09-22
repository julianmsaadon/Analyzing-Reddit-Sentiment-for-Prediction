class LSTM:

    def __init__(self, Date, ID, WeightedAVG, Title, TitleNegative, TitleNeutral, TitlePositive, TitleCompound, Text, TextNegative, TextNeutral, TextPositive, TextCompound, Upvotes, Downvotes, Closeprice, TransactionVolume, EthSpentOverTime, SocialVolumeReddit, GasUsed, SentimentPosReddit, SentimentNegReddit, SentimentBalanceReddit, SentimentVolumeConsumedReddit, SocialDomReddit, DailyAddresses):
        self.Date = Date
        self.ID = ID
        self.WeightedAVG = WeightedAVG
        self.Title = Title
        self.TitleNegative = TitleNegative
        self.TitleNeutral = TitleNeutral
        self.TitlePositive = TitlePositive
        self.TitleCompound = TitleCompound
        self.Text = Text
        self.TextNegative = TextNegative
        self.TextNeutral = TextNeutral
        self.TextPositive = TextPositive
        self.TextCompound = TextCompound
        self.Upvotes = Upvotes
        self.Downvotes = Downvotes
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
