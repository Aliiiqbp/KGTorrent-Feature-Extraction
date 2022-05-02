import pandas as pd
import statistics as sts


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

df['ALLC'] = df['source'].apply(lambda x: sts.mean([len(y) for y in x.split('\n')]))
df[['project_ID', 'ALLC']].to_csv('Features/20.ALLC.csv', index=False)
print(df.head(30))
