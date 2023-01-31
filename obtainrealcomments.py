import praw
import os

from praw.models import MoreComments

from private.details import init

reddit = init()

with open("authors2.txt") as f:
    authors = f.readlines()

cwd = os.getcwd()
datapath = os.path.join(cwd,"humandata")
originalpath = datapath

for i in range(len(authors)):
    authors[i] = authors[i].replace("GPT2Bot\n","")
    allcontent = ""
    newpath = os.path.join(datapath, authors[i])
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    posts = reddit.subreddit(authors[i]).hot(limit=10000)
    print(authors[i])
    for num,submission in enumerate(posts):
        if num % 1000 == 0:
            print(num)
        for comment in submission.comments:
            if isinstance(comment, MoreComments): continue
            allcontent += "[SEP]"
            allcontent += comment.body
    savepath = os.path.join(newpath, "contents.txt")
    with open(savepath, 'w', encoding="utf-8") as f:
        f.write(allcontent)

