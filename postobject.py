
class Post:

    TitleSentimentResult = []
    TextSentimentResult = []

    def __init__(self, Date, ID, Title, Text, Upvotes, Downvotes):
        self.Date = Date
        self.ID = ID
        self.Title = Title
        self.Text = Text
        self.Upvotes = Upvotes
        self.Downvotes = Downvotes
        self.Weight = 0.7

    def SetWeight(self, x):
        self.Weight = x

    def GetRedditCsvString(self):
        return [self.Date, self.ID, self.Title, self.Text, self.Upvotes, self.Downvotes]

    def GetReadRedditCsv(row):
        return Post(row['Date'], row['ID'], row['Title'], row['Text'], row['Upvotes'], row['Downvotes'])
    @staticmethod
    def GetRedditCsvHeader():
        return ['Date', 'ID', 'Title', 'Text', 'Upvotes', 'Downvotes']

    def GetSentimentCsvString(self):
        return [self.Date, self.ID, self.GetWeightedAverageCompound(), self.Title, self.GetTitleNegative(), self.GetTitleNeutral(), self.GetTitlePositive(), self.GetTitleCompound(), self.Text, self.GetTextNegative(), self.GetTextNeutral(), self.GetTextPositive(), self.GetTextCompound(), self.Upvotes, self.Downvotes]

    @staticmethod
    def GetSentimentCsvHeader():
        return ['Date', 'ID', 'WeightedAVG', 'Title', 'TitleNegative', 'TitleNeutral', 'TitlePositive', 'TitleCompound', 'Text', 'TextNegative', 'TextNeutral', 'TextPositive', 'TextCompound', 'Upvotes', 'Downvotes']

    def Ratio(self):
        return self.Upvotes/self.Downvotes

    def SentimentText(self):
        return str(self.Text)

    def SentimentTitle(self):
        return str(self.Title)

    def EnrichWithTitleSentimentResult(self, TitlesentimentResult):
        self.TitleSentimentResult = TitlesentimentResult

    def EnrichWithTextSentimentResult(self, TextsentimentResult):
        self.TextSentimentResult = TextsentimentResult

    def GetWeightedAverageCompound(self):
        return (self.GetTitleCompound() * self.Weight) + (self.GetTextCompound() * (1 - self.Weight))

    def GetTitleCompound(self):
        return self.TitleSentimentResult['compound']

    def GetTitleNeutral(self):
        return self.TitleSentimentResult['neu']

    def GetTitlePositive(self):
        return self.TitleSentimentResult['pos']

    def GetTitleNegative(self):
        return self.TitleSentimentResult['neg']

    def GetTextCompound(self):
        return self.TextSentimentResult['compound']

    def GetTextNeutral(self):
        return self.TextSentimentResult['neu']

    def GetTextPositive(self):
        return self.TextSentimentResult['pos']

    def GetTextNegative(self):
        return self.TextSentimentResult['neg']

