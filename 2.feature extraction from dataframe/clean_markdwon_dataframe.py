import pandas as pd
import re

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df = pd.read_csv('kg_markdowns.csv')
print(df.shape)
df.dropna(axis=0, how='all', inplace=True)
print(df.shape)
df = df[df['project_ID'].notna()]
print(df.shape)
df = df[df.project_ID != 'train_emb']
print(df.shape)
df['project_ID'] = df['project_ID'].astype('int')
df['cell_index'] = df['cell_index'].astype('int')
df.to_csv('kg_markdowns_clean.csv', index=False)




