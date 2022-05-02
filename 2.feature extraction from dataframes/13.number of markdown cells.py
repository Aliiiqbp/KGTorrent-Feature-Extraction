import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df_markdown = pd.read_csv('kg_markdowns_clean.csv')[['project_ID', 'cell_index']]

# drop rows without source code
df_markdown = df_markdown[df_markdown['cell_index'].notna()]

df_markdown = df_markdown.groupby(['project_ID'])['cell_index'].apply(list).reset_index()
df_markdown['MCEL'] = df_markdown['cell_index'].apply(lambda x: max(x))

df_markdown[['project_ID', 'MCEL']].to_csv('Features/13.MCEL.csv', index=False)
print(df_markdown.head(30))
