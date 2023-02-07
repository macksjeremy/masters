import os
import pandas as pd
cwd = os.getcwd()
datapath = os.path.join(cwd,"humandata")
originalpath = datapath
sentences = []
for i in os.listdir(datapath):
    path = os.path.join(originalpath,i)
    path = os.path.join(path, "contents.txt")
    with open(path,encoding='utf-8') as f:
        contents = f.readlines()
        for sent in contents:
            sentences.append(sent)
consolidated = "".join(sentences)
consolidated = consolidated.split("[SEP]")
sr = pd.Series(consolidated)
sr.to_csv("fullhumandata.csv")
print(consolidated)
