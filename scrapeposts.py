import praw
from private.details import init
import os
def chomp(s):
    s = s.replace('\n','')
    return s
with open("authors.txt") as f:
    authors = f.readlines()

for i in range(len(authors)):
    authors[i] = chomp(authors[i])

print(authors)
cwd = os.getcwd()
datapath = os.path.join(cwd,"data")
if not os.path.exists(datapath):
    os.mkdir(datapath)
reddit = init()

for i in authors:
    print("Finding Comments for", i)
    allcontent = ""
    newpath = os.path.join(datapath,i)
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    allcomments = reddit.redditor(i).comments.hot(limit=None)
    for comment in allcomments:
        allcontent += "[SEP]"
        allcontent += comment.body
    savepath = os.path.join(newpath, "contents.txt")
    with open(savepath,'w',encoding="utf-8") as f:
        f.write(allcontent)

