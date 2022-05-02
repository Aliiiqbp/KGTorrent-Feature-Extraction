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


df['NDD'] = df['output_type'].apply(lambda x: x.count('display_data'))
df['NExR'] = df['output_type'].apply(lambda x: x.count('execute_result'))
df[['project_ID', 'NDD', 'NExR']].to_csv('Features/21.NDD.22.NExR.csv', index=False)
print(df.head(30))
print(df.shape)
