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
df['H3'] = df['source'].apply(lambda x: x.split().count('###'))


df[['project_ID', 'H3']].to_csv('Features/10.H3.csv', index=False)
print(df.head(30))

