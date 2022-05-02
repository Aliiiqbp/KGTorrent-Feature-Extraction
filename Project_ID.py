import json
import csv
import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

df = pd.read_csv('user-kernel.csv')
df['project_name'] = df['UserName'] + '_' + df['CurrentUrlSlug'] + '.ipynb'
df_id = df[['project_name', 'KId']]
df_id = df_id.sort_values(by='project_name', ascending=True)

df_id.to_csv('project_name_ID.csv', index=False)
print(df_id.head())
