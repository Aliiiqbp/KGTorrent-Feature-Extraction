import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df_code = pd.read_csv('kg_codes_clean.csv')[['project_ID', 'cell_index']]
print(df_code.head())

# drop rows without source code
df_code = df_code[df_code['cell_index'].notna()]


df_code = df_code.groupby(['project_ID'])['cell_index'].apply(list).reset_index()

df_code['CCEL'] = df_code['cell_index'].apply(lambda x: max(x))

df_code[['project_ID', 'CCEL']].to_csv('Features/7.CCEL.csv', index=False)
print(df_code.head(30))
