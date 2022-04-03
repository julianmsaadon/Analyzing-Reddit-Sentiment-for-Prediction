header = ['Date', 'ID', 'Title', 'Text', 'Upvotes', 'Downvotes']
with open('redditData.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in range(len(dates)-1):
        writer.writerow([dates[i], ids[i], titles[i], selftext[i], upvotes[i], downvotes[i]])