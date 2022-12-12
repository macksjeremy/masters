import praw

from loadreddit import init

reddit=init()

allauthors = set()
for submission in reddit.subreddit("SubSimulatorGPT2").hot(limit=None):
    allauthors.add(submission.author)
for submission in reddit.subreddit("SubSimulatorGPT2").controversial(limit=None):
    allauthors.add(submission.author)
for submission in reddit.subreddit("SubSimulatorGPT2").new(limit=None):
    allauthors.add(submission.author)
for submission in reddit.subreddit("SubSimulatorGPT2").rising(limit=None):
    allauthors.add(submission.author)
for submission in reddit.subreddit("SubSimulatorGPT2").top(limit=None):
    allauthors.add(submission.author)
for submission in reddit.subreddit("SubSimulatorGPT2").gilded(limit=None):
    allauthors.add(submission.author)
print(len(allauthors),"Authors Found")