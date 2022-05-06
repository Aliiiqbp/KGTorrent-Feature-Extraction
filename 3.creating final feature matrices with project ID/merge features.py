import pandas as pd
import os


df = pd.read_csv('/home/ali/Documents/Term10/BSc Project/KGTorrent-Feature-Extraction/2.feature extraction from dataframes/1.LOC.csv')
# df = df.rename(columns={'KId': 'project_ID'})
print(df.columns)

directory = os.fsencode('/home/ali/Documents/Term10/BSc Project/KGTorrent-Feature-Extraction/2.feature extraction from dataframes/Features/')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    df_tmp = pd.read_csv('/home/ali/Documents/Term10/BSc Project/KGTorrent-Feature-Extraction/2.feature extraction from dataframes/Features/' + filename)
    df_tmp = df_tmp[df_tmp['project_ID'].notna()]
    df_tmp['project_ID'] = df_tmp['project_ID'].apply(lambda x: int(float(x)))
    print(filename, df_tmp.shape)

    df = pd.merge(left=df, right=df_tmp, how='left', left_on='project_ID', right_on='project_ID')
    print(df.shape)
    del df_tmp

df.to_csv('final_matrix.csv', index=False)
