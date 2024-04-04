from pymongo import MongoClient
import pandas as pd
import re

def clean_string(s):
    s = re.sub(r'\[.+?\]', '', s)
    s = re.sub(r'\(.+\)', '', s)
    s = re.sub(r'[^A-Za-z0-9., ]+', '', s)
    return s

client = MongoClient()
db = client['JiraRepos']

ls = []

PROJECT_NAME = 'Apache'
project_descriptions = {'Apache': '''The Apache HTTP Server (/əˈpætʃi/ ə-PATCH-ee) is a free and open-source cross-platform web server software, released under the terms of Apache License 2.0. It is developed and maintained by a community of developers under the auspices of the Apache Software Foundation.
The vast majority of Apache HTTP Server instances run on a Linux distribution,[5] but current versions also run on Microsoft Windows,[6] OpenVMS,[7] and a wide variety of Unix-like systems. Past versions also ran on NetWare, OS/2 and other operating systems,[8] including ports to mainframes.[9]'''}
project_descriptions = {k: clean_string(v) for k, v in project_descriptions.items()}

for i, issue in enumerate(db[PROJECT_NAME].find({'fields.issuetype.name': 'Story'}, {'fields.summary', 'fields.description', 'fields.issuetype.name'})):
    ls.append(issue)
    if i == 100:
        break
        
df = pd.DataFrame(pd.json_normalize(ls, sep='.'))

df_out = pd.DataFrame(columns=['context', 'instruction', 'response'])
df_out['instruction'] = df['fields.description']
df_out['response'] = df['fields.summary']
df_out['context'] = project_descriptions[PROJECT_NAME]
df_out = df_out.dropna()

df_out.to_csv('data/prepared_data/stories_data.csv')