from pymongo import MongoClient
import pandas as pd

client = MongoClient()
db = client['JiraRepos']

ls = []

for i, issue in enumerate(db['Apache'].find({'fields.issuetype.name': 'Story'}, {'fields.summary', 'fields.description', 'fields.issuetype.name'})):
    ls.append(issue)
    if i == 100:
        break
        
df = pd.DataFrame(pd.json_normalize(ls, sep='.'))
df.to_csv('data/prepared_data/stories_data.csv')