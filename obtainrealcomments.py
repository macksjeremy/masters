import praw

from private.details import init

reddit = init()

allauthors = []
with open("authors2.txt") as f:
    authors = f.readlines()

[]
for i in range(len(authors)):
    authors[i] = authors[i].replace("GPT2Bot\n","")
    print(authors[i])
    for submission in reddit.subreddit(authors[i]).hot(limit=None):
        allauthors.append(submission)

print(allauthors)