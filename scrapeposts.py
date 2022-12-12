import praw
from private.details import init

def chomp(s):
    s = s.replace('\n','')
    return s
with open("authors.txt") as f:
    authors = f.readlines()

for i in range(len(authors)):
    authors[i] = chomp(authors[i])

print(authors)
reddit = init()