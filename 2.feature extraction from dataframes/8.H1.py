import pandas as pd
import re

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df = pd.read_csv('kg_markdowns_clean.csv')[['project_ID', 'source']]
print(df.shape)

# drop rows without source code
df = df[df['source'].notna()]
print(df.shape)

df = df.groupby(['project_ID'])['source'].apply('\n'.join).reset_index()
df['H1'] = df['source'].apply(lambda x: x.split().count('#'))


df[['project_ID', 'H1']].to_csv('Features/8.H1.csv', index=False)
print(df.head(30))

