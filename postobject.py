class Post:
    def __init__(self, Date, ID, Title, Text, Upvotes, Downvotes):
        self.Date = Date
        self.ID = ID
        self.Title = Title
        self.Text = Text
        self.Upvotes = Upvotes
        self.Downvotes = Downvotes

    def Ratio(self):
        return self.Upvotes/self.Downvotes

