import datetime
# from datetime import datetime, timedelta

class Sentiment:

    def __init__(self, Date, ID, WeightedAVG, Title, TitleNegative, TitleNeutral, TitlePositive, TitleCompound, Text, TextNegative, TextNeutral, TextPositive, TextCompound, Upvotes, Downvotes):
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

    def GetReadSentimentCsv(row):
        return Sentiment(row['Date'], row['ID'], row['WeightedAVG'], row['Title'], row['TitleNegative'], row['TitleNeutral'], row['TitlePositive'], row['TitleCompound'], row['Text'], row['TextNegative'], row['TextNeutral'], row['TextPositive'], row['TextCompound'], row['Upvotes'], row['Downvotes'])

    def GetStrptimeDate(self):
        return datetime.datetime.strptime(self.Date, "%Y-%m-%d %H:%M:%S")

    def GetRoundedTime(self):
        return datetime.datetime(self.year,
                                 self.month,
                                 self.day,
                                 0, 0)

    # def hour_rounder(self):
    #     return (self.replace(second=0, microsecond=0, minute=0, hour=self.hour)
    #            + timedelta(hours=self.minute//30))
