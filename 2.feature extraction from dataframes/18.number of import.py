import pandas as pd

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

df['NOI'] = df['source'].apply(lambda x: x.count('import'))
df[['project_ID', 'NOI']].to_csv('Features/18.NOI.csv', index=False)
print(df.head(30))
print(df['NOI'].unique())
