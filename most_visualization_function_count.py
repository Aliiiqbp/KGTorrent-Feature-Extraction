import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

# read .csv files which contain code cells
df = pd.read_csv('kg_codes_clean.csv')[['project_ID', 'source']]
print(df.shape)

visualization_functions = ['show', 'plot', 'figure', 'subplots', 'legend', 'subplot', 'imshow', 'plotPerColumnDistribution',
                           'scatter', 'countplot', 'barplot', 'distplot', 'plotCorrelationMatrix', 'plotScatterMatrix',
                           'boxplot', 'bar', 'hist', 'grid', 'pie', 'factorplot', 'scatterplot', 'lineplot', 'kdeplot',
                           'violinplot', 'imread', 'barh', 'catplot', 'pairplot', 'regplot', 'pointplot', 'jointplot', 'colorbar']

# drop rows without source code
df = df[df['source'].notna()]
print(df.shape)

df = df.groupby(['project_ID'])['source'].apply('\n'.join).reset_index()

df['visulization'] = df['source'].apply(lambda x: sum([x.split().count(y) for y in visualization_functions]))
df[['project_ID', 'visulization']].to_csv('visualization.csv', index=False)
print(df.head(30))
