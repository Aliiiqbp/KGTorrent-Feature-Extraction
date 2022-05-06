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

df['import_not_used'] = df['source'].apply(lambda x: [re.findall('^import.*', y) for y in x.split('\n')])
print(df.shape)
df[['project_ID', 'import_not_used']].to_csv('Features/24.import_not_used.csv', index=False)
print(df.tail(1000).head(20))
