import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df = pd.read_csv('kg_codes_clean.csv')[['project_ID', 'output_type']]
print(df.shape)

# drop rows without source code
# df = df[df['source'].notna()]

df = df.groupby(['project_ID'])['output_type'].apply(list).reset_index()

df['EIO'] = df['output_type'].apply(lambda x: x.count('error'))
df[['project_ID', 'EIO']].to_csv('Features/12.EIO.csv', index=False)
print(df.head(30))
print(df.shape)
