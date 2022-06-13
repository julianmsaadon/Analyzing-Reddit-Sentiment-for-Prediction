import csv
from postobject import Post
from collections import OrderedDict
import pandas as pd


# with open('redditData.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     posts = []
#     for row in reader:
#         posts.append(Post.GetReadRedditCsv(row))
#
# print(len(posts))
PostsColumns = Post.GetRedditCsvHeader()
Posts1st = pd.read_csv("redditData.csv", usecols=PostsColumns)
Posts2nd = pd.read_csv("2ndHalfredditData.csv", usecols=PostsColumns)

Posts = Posts1st.append(Posts2nd, ignore_index=True)
# print(Posts[7])
PostsLIST = []
for i in range(len(Posts.Date)):
    PostsLIST.append([Posts['Date'][i],
                     Posts['ID'][i],
                     Posts['Title'][i],
                     Posts['Text'][i],
                     Posts['Upvotes'][i],
                     Posts['Downvotes'][i]]
                     )
# print(len(PostsLIST))

with open('POSTS2021-2022.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(Post.GetRedditCsvHeader())
    for i in range(len(PostsLIST)):
        if str(PostsLIST[i][3]) != "[removed]" or str(PostsLIST[i][3]) != "[deleted]":
            writer.writerow([PostsLIST[i][0],
                             PostsLIST[i][1],
                             PostsLIST[i][2],
                             PostsLIST[i][3],
                             PostsLIST[i][4],
                             PostsLIST[i][5]
                             ])

# with open('POSTS2021-2022.csv', 'w', encoding='UTF8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(Post.GetRedditCsvHeader())
#     for i in range(len(Posts.Date)-1):
#         if Posts.Text[i] != "[removed]" or Posts.Text[i] != "[removed]":
#             writer.writerow(Posts[i].GetRedditCsvString())

print(type(str(PostsLIST[0][3])))
