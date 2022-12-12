import praw

from private.details import init

reddit = init()

allauthors = set()
for submission in reddit.subreddit("SubSimulatorGPT2").hot(limit=None):
    allauthors.add(submission.author.name)
for submission in reddit.subreddit("SubSimulatorGPT2").controversial(limit=None):
    allauthors.add(submission.author.name)
for submission in reddit.subreddit("SubSimulatorGPT2").new(limit=None):
    allauthors.add(submission.author.name)
for submission in reddit.subreddit("SubSimulatorGPT2").rising(limit=None):
    allauthors.add(submission.author.name)
for submission in reddit.subreddit("SubSimulatorGPT2").top(limit=None):
    allauthors.add(submission.author.name)
for submission in reddit.subreddit("SubSimulatorGPT2").gilded(limit=None):
    allauthors.add(submission.author.name)

allauthors = list(allauthors)
allauthors.sort()
print(len(allauthors),"Authors Found")
print(allauthors)
with open("newauthors.txt","w") as f:
    for i in allauthors:
        if "GPT2Bot" in i:
            f.write(i + "\n")
