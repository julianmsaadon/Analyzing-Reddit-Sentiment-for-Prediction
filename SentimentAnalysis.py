import csv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from postobject import Post

with open('redditData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    title = []
    text = []
    date = []
    id = []
    upvotes = []
    downvotes = []

    posts = []
    for row in reader:
        posts.append(Post(row['Date'],row['ID'],row['Title'],row['Text'],row['Upvotes'],row['Downvotes']))
        # print(row['Title'])
        title.append(row['Title'])
        text.append(row['Text'])
        date.append(row['Date'])
        id.append(row['ID'])
        upvotes.append(row['Upvotes'])
        downvotes.append(row['Downvotes'])

print(len(title))
print(len(date))


analyzer = SentimentIntensityAnalyzer()


Titlesentiment = []
TitleCompound = []
TitleNeutral = []
TitleNegative = []
TitlePositive = []

Textsentiment = []
TextCompound = []
TextNeutral = []
TextNegative = []
TextPositive = []

index = 0
for post in posts:
    vsTitle = analyzer.polarity_scores(post.SentimentTitle())
    vsText = analyzer.polarity_scores(post.SentimentText())
    post.EnrichWithTitleSentimentResult(vsTitle)
    post.EnrichWithTextSentimentResult(vsText)
    print("{:-<65} {}".format(str(vsTitle), str(vsText)))
    # post.SentimentTitle(), ".  ", post.SentimentText()
    TitleNegative.append(post.GetTitleNegative())
    TitleNeutral.append(post.GetTitleNeutral())
    TitlePositive.append(post.GetTitlePositive())
    TitleCompound.append(post.GetTitleCompound())
    TextNegative.append(post.GetTextNegative())
    TextNeutral.append(post.GetTextNeutral())
    TextPositive.append(post.GetTextPositive())
    TextCompound.append(post.GetTextCompound())
    # print(TitleCompound)
    if TitleCompound[index] == 0.0 and TextCompound[index] == 0.0:
        del TitleCompound[index]
        del TitleNeutral[index]
        del TitleNegative[index]
        del TitlePositive[index]
        del TextCompound[index]
        del TextNeutral[index]
        del TextNegative[index]
        del TextPositive[index]
        del posts[index]
        del title[index]
        del text[index]
        del date[index]
        del id[index]
        del upvotes[index]
        del downvotes[index]
    else:
        index = index + 1


# print(posts)

print(len(TextNegative))
print(len(TextPositive))
print(len(TextCompound))
print(len(TitleCompound))
print(len(date))


# print(len(TextNegative))
print(len(title))
print(len(posts))

header = ['Date', 'ID', 'Title', 'TitleNegative', 'TitleNeutral', 'TitlePositive', 'TitleCompound', 'Text', 'TextNegative', 'TextNeutral', 'TextPositive', 'TextCompound','Upvotes', 'Downvotes']

with open('postSentiment.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(date)-1):
        writer.writerow([date[i], id[i], title[i], TitleNegative[i], TitleNeutral[i], TitlePositive[i], TitleCompound[i], text[i], TextNegative[i], TextNeutral[i], TextPositive[i], TextCompound[i], upvotes[i], downvotes[i]])

