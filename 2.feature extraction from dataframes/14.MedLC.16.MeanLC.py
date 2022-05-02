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
df['line_per_cell'] = df['source'].apply(lambda x: x.count('\n') + 1)
df = df.groupby(['project_ID'])['line_per_cell'].apply(list).reset_index()
df['MedLC'] = df['line_per_cell'].apply(lambda x: sts.median(x))
df['MeanLC'] = df['line_per_cell'].apply(lambda x: sts.mean(x))
df[['project_ID', 'MedLC', 'MeanLC']].to_csv('Features/14.MedLC.16.MeanLC.csv', index=False)
print(df.tail(30))
print(df['MedLC'].unique())
print(df['MeanLC'].unique())
