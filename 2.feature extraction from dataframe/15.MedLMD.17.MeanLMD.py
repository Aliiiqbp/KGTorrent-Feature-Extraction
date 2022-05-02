import pandas as pd
import statistics as sts
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df = pd.read_csv('kg_markdowns_clean.csv')[['project_ID', 'source']]
print(df.shape)

# drop rows without source code
df = df[df['source'].notna()]
print(df.shape)
df['line_per_cell'] = df['source'].apply(lambda x: len(sent_tokenize(x)))
df = df.groupby(['project_ID'])['line_per_cell'].apply(list).reset_index()
df['MedLMD'] = df['line_per_cell'].apply(lambda x: sts.median(x))
df['MeanLMD'] = df['line_per_cell'].apply(lambda x: sts.mean(x))
df[['project_ID', 'MedLMD', 'MeanLMD']].to_csv('Features/15.MedLMD.17.MeanLMD.csv', index=False)
print(df.tail(30))
print(df['MedLMD'].unique())
print(df['MeanLMD'].unique())
