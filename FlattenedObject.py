class FlatSent:

    def __init__(self, WeightedAVG, TitleNegative, TitleNeutral, TitlePositive, TitleCompound, TextNegative, TextNeutral, TextPositive, TextCompound):
        self.WeightedAVG = WeightedAVG
        self.TitleNegative = TitleNegative
        self.TitleNeutral = TitleNeutral
        self.TitlePositive = TitlePositive
        self.TitleCompound = TitleCompound
        self.TextNegative = TextNegative
        self.TextNeutral = TextNeutral
        self.TextPositive = TextPositive
        self.TextCompound = TextCompound

    def GetSentVal(self):
        return self.WeightedAVG, self.TitleNegative, self.TitleNeutral, self.TitlePositive, self.TitleCompound, self.TextNegative, self.TextNeutral, self.TextPositive, self.TextCompound
