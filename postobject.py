class Post:
    SentimentResult = []

    def __init__(self, Date, ID, Title, Text, Upvotes, Downvotes):
        self.Date = Date
        self.ID = ID
        self.Title = Title
        self.Text = Text
        self.Upvotes = Upvotes
        self.Downvotes = Downvotes

    def Ratio(self):
        return self.Upvotes/self.Downvotes

    def SentimentText(self):
        return str(self.Title) + '. ' + str(self.Text)

    def EnrichWithSentimentResult(self, sentimentResult):
        self.SentimentResult = sentimentResult

    # def GetCompound(self, sentimentResult):
    #     self.sentimentResult = sentimentResult['compound']
    def GetCompound(self):
        return self.SentimentResult['compound']

    def GetNeutral(self):
        return self.SentimentResult['neu']

    def GetPositive(self):
        return self.SentimentResult['pos']

    def GetNegative(self):
        return self.SentimentResult['neg']