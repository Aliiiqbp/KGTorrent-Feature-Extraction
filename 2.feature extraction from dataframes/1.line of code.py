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

df['LOC'] = df['source'].apply(lambda x: x.count('\n') + 1)
print(df.shape)
df[['project_ID', 'LOC']].to_csv('Features/1.LOC.csv', index=False)
# print(df.head(30))
