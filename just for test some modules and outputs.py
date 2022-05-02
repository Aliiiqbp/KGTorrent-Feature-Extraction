import pandas as pd
import re
import matplotlib as plt


desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


# text = '.....'
# print(text.split('.'))
#

# s = '# print(\'ali\'??!#).*print', s))

# df = pd.read_csv('code_batch_1_no_output.csv')[['project_ID', 'source']]
# print(len(re.findall('#.*?\n', df['source'].iloc[102])))
# print(len(re.findall('\'\'\'.*?\n', df['source'].iloc[102])))
#
# df = pd.read_csv('6.DeF.csv')
# print(df['DeF'].tail(100).head(30))
# df.rename(columns={"number_of_code_line": "LOC"}, inplace=True)
# df.to_csv('1.LOC.csv', index=False)

# print(df[df.number_of_comment_line <= 5])

# print(df['number_of_comment_line'])


# df = pd.read_csv('kg_codes_clean.csv')[['project_ID', 'output_type']]
# print(df['output_type'].unique())

# df = pd.read_csv('14.MedLC.16.MeanLC.csv')
# print(sorted(df['MedLC'].unique())[-100:-50])

# df = pd.read_csv('kg_codes_clean.csv')[['project_ID', 'source']]
# print(df['source'].dtypes)
# print(type(df['source'].iloc[5]))

# df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
# df['execution_count'] = df['execution_count'].fillna(0)
# df['cell_index'] = df['cell_index'].fillna(0)
# df['cell_index'] = df['cell_index'].astype('int64')
# df['execution_count'] = df['execution_count'].astype('int64')
#
# print(df.dtypes)
# df.to_csv('kg_codes_clean.csv', index=False)
# print(df.head())
#

# import nltk
# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize
#
# sentences = 'A Turning machine is a device that manipulates symbols on a strip of tape according to a table of rules. Despite its simplicity, a Turing machine can be adapted to simulate the logic of any computer algorithm, and is particularly useful in explaining the functions of a CPU inside a computer. The "Turing" machine was described by Alan Turing in 1936, who called it an "a(utomatic)-machine". The Turing machine is not intended as a practical computing technology, but rather as a hypothetical device representing a computing machine. Turing machines help computer scientists understand the limits of mechaniacl computation.'
#
# number_of_sentences = sent_tokenize(sentences)
#
# print(len(number_of_sentences))
#

df = pd.read_csv('2.feature extraction from dataframes/21.NDD.22.NExR.csv')
print(df.tail(20))

# columns = df.columns
#
# for column in columns:
#     print(column, len(df[column].unique()))
