import pandas as pd
import re

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df = pd.read_csv('kg_codes_clean.csv')[['project_ID', 'source']]
print(df.shape)

# drop rows without source code
df = df[df['source'].notna()]
print(df.shape)

df = df.groupby(['project_ID'])['source'].apply('\n'.join).reset_index()
df['DeF'] = df['source'].apply(lambda x: sum([len(re.findall('^(?!#).*def', y)) for y in x.split('\n')]))

df[['project_ID', 'DeF']].to_csv('Features/6.DeF.csv', index=False)
print(df.head(30))
print(df.iloc[246023]['source'])
