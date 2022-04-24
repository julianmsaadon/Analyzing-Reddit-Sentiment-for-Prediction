from datetime import datetime
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

    # def GetDate(self):
    #     return str(datetime.utcfromtimestamp(self.created_utc))
    #
    # def GetID(self):
    #     return str(self.id)
    #
    # def GetTitle(self):
    #     return str(self.title)
    #
    # def GetText(self):
    #     return str(self.selftext)
    #
    # def GetUpvotes(self):
    #     return str(self.ups)
    #
    # def GetDownvotes(self):
    #     return str(self.downs)

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