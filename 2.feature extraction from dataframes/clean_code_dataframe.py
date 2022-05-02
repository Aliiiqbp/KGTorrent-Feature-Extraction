import pandas as pd


df = pd.read_csv('kg_codes.csv')

df.dropna(axis=0, how='all', inplace=True)
df = df[df['project_ID'].notna()]
df = df[df.project_ID != 'train_emb']
df['project_ID'] = df['project_ID'].astype('int')

df['execution_count'] = df['execution_count'].fillna(0)
df['cell_index'] = df['cell_index'].fillna(0)
df['cell_index'] = df['cell_index'].astype('int64')
df['execution_count'] = df['execution_count'].astype('int64')

print(df.dtypes)
df.to_csv('kg_codes_clean.csv', index=False)
print(df.head())

